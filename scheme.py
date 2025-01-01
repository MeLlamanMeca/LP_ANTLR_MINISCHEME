import sys
from antlr4 import *
from generated.schemeLexer import schemeLexer
from generated.schemeParser import schemeParser
from generated.schemeVisitor import schemeVisitor
from antlr4.error.ErrorListener import ErrorListener

Data = {}  # Global data dictionary
DataStack = [{}]  # Stack of data dictionaries


class TreeVisitor(schemeVisitor):

    # Visit a parse tree produced by schemeParser#root.
    def visitRoot(self, ctx: schemeParser.RootContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by schemeParser#definitions.
    def visitDefinitions(self, ctx: schemeParser.DefinitionsContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by schemeParser#main.
    def visitMain(self, ctx: schemeParser.MainContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by schemeParser#expression.
    def visitExpression(self, ctx: schemeParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by schemeParser#listCreation.
    def visitListCreation(self, ctx: schemeParser.ListCreationContext):
        _, _, *expressions, _ = ctx.getChildren()
        lista = []
        for expression in expressions:
            lista.append(self.visit(expression))
        return lista

    def visitCarExpression(self, ctx: schemeParser.CarExpressionContext):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        else:
            return result
    
    def visitCdrExpression(self, ctx: schemeParser.CdrExpressionContext):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)
        if isinstance(result, list) and len(result) > 1:
            return result[1:]
        else:
            return []

    # Visit a parse tree produced by schemeParser#consExpression.
    def visitConsExpression(self, ctx: schemeParser.ConsExpressionContext):
        _, _, expression1, expression2, _ = ctx.getChildren()
        result1 = self.visit(expression1)
        result2 = self.visit(expression2)
        if not isinstance(result2, list):
            result2 = [result2]
        return [result1] + result2
    
    def visitAppendExpression(self, ctx: schemeParser.AppendExpressionContext):
        _, _, expression1, expression2, _ = ctx.getChildren()
        result1 = self.visit(expression1)
        result2 = self.visit(expression2)
        if not isinstance(result1, list):
            result1 = [result1]
        if not isinstance(result2, list):
            result2 = [result2]
        return result1 + result2
    
    def visitLengthExpression(self, ctx: schemeParser.LengthExpressionContext):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)
        if not isinstance(result, list):
            return 1
        return len(result)

    # Visit a parse tree produced by schemeParser#nullExpression.
    def visitNullExpression(self, ctx: schemeParser.NullExpressionContext):
        _, _, expression, _ = ctx.getChildren()
        return self.visit(expression) == []

    # Visit a parse tree produced by schemeParser#displayExpression.
    def visitDisplayExpression(self, ctx: schemeParser.DisplayExpressionContext):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)

        def format_result(item):
            if isinstance(item, bool):
                return '#t' if item else '#f'
            elif isinstance(item, list):
                return f"({' '.join(map(format_result, item))})"
            else:
                return str(item)

        print(format_result(result), end='')

    # Visit a parse tree produced by schemeParser#defineFunction.
    def visitDefineFunction(self, ctx: schemeParser.DefineFunctionContext):
        global Data
        _, _, _, functionName, *functionParameters, _, functionBody, _ = ctx.getChildren()
        Data[functionName.getText()] = (functionParameters, functionBody)

    # Visit a parse tree produced by schemeParser#defineConstant.
    def visitDefineConstant(self, ctx: schemeParser.DefineConstantContext):
        global Data
        _, _, constantName, constantValue, _ = ctx.getChildren()
        Data[constantName.getText()] = self.visit(constantValue)

    # Visit a parse tree produced by schemeParser#ifExpression.
    def visitIfExpression(self, ctx: schemeParser.IfExpressionContext):
        _, _, condition, ifTrue, ifFalse, _ = ctx.getChildren()
        return self.visit(ifTrue) if self.visit(condition) else self.visit(ifFalse)

    # Visit a parse tree produced by schemeParser#condExpression.
    def visitCondExpression(self, ctx: schemeParser.CondExpressionContext):
        _, _, *conditions = ctx.getChildren()
        conditions = [(conditions[i], conditions[i + 1]) for i in range(1, len(conditions), 4)]
        for condition in conditions:
            if self.visit(condition[0]):
                return self.visit(condition[1])

    # Visit a parse tree produced by schemeParser#letExpression.
    def visitLetExpression(self, ctx: schemeParser.LetExpressionContext):
        global Data
        _, _, _, *definitions, _, expression, _ = ctx.getChildren()
        definitions = [(definitions[i], definitions[i + 1]) for i in range(1, len(definitions), 4)]
        DataStack.append(Data.copy())
        for definition in definitions:
            Data[definition[0].getText()] = self.visit(definition[1])
        result = self.visit(expression)
        Data.update(DataStack.pop())
        return result

    # Visit a parse tree produced by schemeParser#functionCall.
    def visitFunctionCall(self, ctx: schemeParser.FunctionCallContext):
        global Data
        _, functionName, *parameters, _ = ctx.getChildren()
        functionParameters, functionBody = Data[functionName.getText()]
        
        DataStack.append(Data.copy())
        for parameter, value in zip(functionParameters, parameters):
            Data[parameter.getText()] = self.visit(value)
        result = self.visit(functionBody)
        Data = DataStack.pop()
        
        return result

    # Visit a parse tree produced by schemeParser#readExpression.
    def visitReadExpression(self, ctx: schemeParser.ReadExpressionContext):
        entry = input()

        def format_entry(item):

            if item.isdigit():
                return int(item)
            
            elif item in ('#t', '#f', 'else'):
                return item == '#t' or item == 'else'
            
            elif item.startswith("'"):
                tokens = item.replace('(', ' ( ').replace(')', ' ) ').split()[2:-1]
                stack, result = [], []
                for token in tokens:
                    if token == '(':
                        stack.append(result)
                        result = []
                    elif token == ')':
                        temp = result
                        result = stack.pop()
                        result.append(temp)
                    else:
                        result.append(format_entry(token))
                return result
            
            else:
                return item

        return format_entry(entry)


    # Visit a parse tree produced by schemeParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx: schemeParser.ArithmeticExpressionContext):
        _, operator, *expressions, _ = ctx.getChildren()
        operator = operator.getText()
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
            'mod': lambda x, y: x % y,
            '^': lambda x, y: x ** y,
            'max': lambda x, y: max(x, y),
            'min': lambda x, y: min(x, y),
        }
        
        if len(expressions) == 1 and operator == '-':
            return -self.visit(expressions[0])
        
        result = self.visit(expressions[0])
        for expr in expressions[1:]:
            result = operations[operator](result, self.visit(expr))
        return result

    # Visit a parse tree produced by schemeParser#comparisonExpression.
    def visitComparisonExpression(self, ctx: schemeParser.ComparisonExpressionContext):
        _, operator, expr1, expr2, _ = ctx.getChildren()
        operator = operator.getText()
        
        operations = {
            '<': lambda x, y: x < y,
            '<=': lambda x, y: x <= y,
            '>': lambda x, y: x > y,
            '>=': lambda x, y: x >= y,
            '=': lambda x, y: x == y,
            '<>': lambda x, y: x != y,
        }
        return operations[operator](self.visit(expr1), self.visit(expr2))
        
    def visitConsultExpression(self, ctx: schemeParser.ConsultExpressionContext):
        _, operator, expression, _ = ctx.getChildren()
        operator = operator.getText()
        operations = {
            'not': lambda x: not x,
            'number?' : lambda x: isinstance(x, int),
            'boolean?' : lambda x: isinstance(x, bool),
            'string?' : lambda x: isinstance(x, str),
            'list?' : lambda x: isinstance(x, list)
        }
        return operations[operator](self.visit(expression))
    
    def visitLogicalExpression(self, ctx: schemeParser.LogicalExpressionContext):
        _, operator, *expressions, _ = ctx.getChildren()
        operator = operator.getText()
        operations = {
            'and': lambda args: all(args),
            'or': lambda args: any(args),
            'nor': lambda args: not any(args),
            'xor': lambda args: sum(args) % 2 == 1,
            'nand': lambda args: not all(args),
            'xnor': lambda args: sum(args) % 2 == 0,
            'implies': lambda args: all(not x or y for x, y in zip(args, args[1:])),
        }
        
        return operations[operator]([self.visit(expr) for expr in expressions])

    def visitEditConstantExpression(self, ctx: schemeParser.EditConstantExpressionContext):
        _, _, constantName, constantValue, _ = ctx.getChildren()
        Data[constantName.getText()] = self.visit(constantValue)
    
    def visitNewLine(self, ctx: schemeParser.NewLineContext):
        print()

    def visitNumberLiteral(self, ctx: schemeParser.NumberLiteralContext):
        return int(ctx.getText())

    def visitBooleanLiteral(self, ctx: schemeParser.BooleanLiteralContext):
        return ctx.getText() == '#t' or ctx.getText() == 'else'

    def visitStringLiteral(self, ctx: schemeParser.StringLiteralContext):
        return ctx.getText()[1:-1]

    def visitIdentifierLiteral(self, ctx: schemeParser.IdentifierLiteralContext):
        return Data[ctx.getText()]


class ConsoleErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        sys.exit(1)
        print(f"Syntax error at line {line}, column {column}: {msg}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scheme.py <filename>")
        sys.exit(1)
    else:
        nom_fitxer = sys.argv[1]
        input_stream = FileStream(nom_fitxer, encoding='utf-8')
        lexer = schemeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = schemeParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ConsoleErrorListener())
        tree = parser.root()
        visitor = TreeVisitor()
        visitor.visit(tree)