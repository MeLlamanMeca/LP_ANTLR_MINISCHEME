from generated.schemeVisitor import schemeVisitor
from generated.schemeParser import schemeParser


class TreeVisitor(schemeVisitor):

    Data = {}  # Global data dictionary
    DataStack = [{}]  # Stack of data dictionaries

    def splitParametersAndBody(self, ParametersAndBody):
        open_parens = 0
        split_index = 0

        for i, item in enumerate(ParametersAndBody):
            if item.getText() == '(':
                open_parens += 1
            elif item.getText() == ')':
                open_parens -= 1
                if open_parens == -1:
                    split_index = i
                    break
        
        parameters = ParametersAndBody[:split_index]
        body = ParametersAndBody[split_index + 1:]
        return parameters, body

    def visitRoot(self, ctx):
        self.visitChildren(ctx)

    def visitDefinitions(self, ctx):
        self.visitChildren(ctx)

    def visitMain(self, ctx):
        self.visitChildren(ctx)

    def visitExpression(self, ctx):
        return self.visitChildren(ctx)

    def visitListCreation(self, ctx):
        _, _, *expressions, _ = ctx.getChildren()
        lista = []
        for expression in expressions:
            lista.append(self.visit(expression))
        return lista

    def visitCarExpression(self, ctx):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        else:
            return result

    def visitCdrExpression(self, ctx):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)
        if isinstance(result, list) and len(result) > 1:
            return result[1:]
        else:
            return []

    def visitConsExpression(self, ctx):
        _, _, expression1, expression2, _ = ctx.getChildren()
        result1 = self.visit(expression1)
        result2 = self.visit(expression2)
        if not isinstance(result2, list):
            result2 = [result2]
        return [result1] + result2

    def visitAppendExpression(self, ctx):
        _, _, expression1, expression2, _ = ctx.getChildren()
        result1 = self.visit(expression1)
        result2 = self.visit(expression2)
        if not isinstance(result1, list):
            result1 = [result1]
        if not isinstance(result2, list):
            result2 = [result2]
        return result1 + result2

    def visitLengthExpression(self, ctx):
        _, _, expression, _ = ctx.getChildren()
        result = self.visit(expression)
        if not isinstance(result, list):
            return 1
        return len(result)

    def visitNullExpression(self, ctx):
        _, _, expression, _ = ctx.getChildren()
        return self.visit(expression) == []

    def visitDisplayExpression(self, ctx):
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

    def visitBeginExpression(self, ctx):
        _, _, *expressions, _ = ctx.getChildren()
        result = None
        for expression in expressions:
            result = self.visit(expression)
        return result

    def visitDefineFunction(self, ctx):
        _, _, _, functionName, *functionParametersAndBody, _ = ctx.getChildren()
        functionParameters, functionBody = self.splitParametersAndBody(functionParametersAndBody)
        self.Data[functionName.getText()] = (functionParameters, functionBody)

    def visitDefineConstant(self, ctx):
        _, _, constantName, constantValue, _ = ctx.getChildren()
        self.Data[constantName.getText()] = self.visit(constantValue)

    def visitIfExpression(self, ctx):
        _, _, condition, ifTrue, ifFalse, _ = ctx.getChildren()
        return self.visit(ifTrue) if self.visit(condition) else self.visit(ifFalse)

    def visitCondExpression(self, ctx):
        _, _, *conditions = ctx.getChildren()
        conditions = [(conditions[i], conditions[i + 1]) for i in range(1, len(conditions), 4)]
        for condition in conditions:
            if self.visit(condition[0]):
                return self.visit(condition[1])

    def visitLetExpression(self, ctx):
        _, _, _, *parametersAndBody, _ = ctx.getChildren()
        letParameters, letBody = self.splitParametersAndBody(parametersAndBody)
        letParameters = [(letParameters[i], letParameters[i + 1]) for i in range(1, len(letParameters), 4)]
        self.DataStack.append(self.Data.copy())

        for parameter in letParameters:
            self.Data[parameter[0].getText()] = self.visit(parameter[1])
        result = None
        for instruction in letBody:
            result = self.visit(instruction)

        self.Data.update(self.DataStack.pop())
        return result

    def visitFunctionCall(self, ctx):
        _, functionName, *parameters, _ = ctx.getChildren()
        functionParameters, functionBody = self.Data[functionName.getText()]
        self.DataStack.append(self.Data.copy())

        for parameter, value in zip(functionParameters, parameters):
            self.Data[parameter.getText()] = self.visit(value)
        result = None
        for instruction in functionBody:
            result = self.visit(instruction)
    
        self.Data = self.DataStack.pop()
        return result

    def visitReadExpression(self, ctx):
        entry = input().strip()

        def format_entry(item):

            if item.isdigit():
                return int(item)

            elif item in ('#t', '#f', 'else'):
                return item == '#t' or item == 'else'

            elif item.startswith('"') and item.endswith('"'):
                return item[1:-1]

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

    def visitArithmeticExpression(self, ctx):
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

        result = self.visit(expressions[0])
        for expr in expressions[1:]:
            result = operations[operator](result, self.visit(expr))
        return result

    def visitComparisonExpression(self, ctx):
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

    def visitConsultExpression(self, ctx):
        _, operator, expression, _ = ctx.getChildren()
        operator = operator.getText()

        operations = {
            'not': lambda x: not x,
            'number?': lambda x: isinstance(x, int),
            'boolean?': lambda x: isinstance(x, bool),
            'string?': lambda x: isinstance(x, str),
            'list?': lambda x: isinstance(x, list)
        }

        return operations[operator](self.visit(expression))

    def visitLogicalExpression(self, ctx):
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

    def visitEditConstantExpression(self, ctx):
        _, _, constantName, constantValue, _ = ctx.getChildren()
        self.Data[constantName.getText()] = self.visit(constantValue)

    def visitNewLine(self, ctx):
        print()

    def visitNumberLiteral(self, ctx):
        return int(ctx.getText())

    def visitBooleanLiteral(self, ctx):
        return ctx.getText() == '#t' or ctx.getText() == 'else'

    def visitStringLiteral(self, ctx):
        return ctx.getText()[1:-1]

    def visitIdentifierLiteral(self, ctx):
        return self.Data[ctx.getText()]
