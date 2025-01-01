# Generated from scheme.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .schemeParser import schemeParser
else:
    from schemeParser import schemeParser

# This class defines a complete generic visitor for a parse tree produced by schemeParser.

class schemeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by schemeParser#root.
    def visitRoot(self, ctx:schemeParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#definitions.
    def visitDefinitions(self, ctx:schemeParser.DefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#main.
    def visitMain(self, ctx:schemeParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#expression.
    def visitExpression(self, ctx:schemeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#listCreation.
    def visitListCreation(self, ctx:schemeParser.ListCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#carExpression.
    def visitCarExpression(self, ctx:schemeParser.CarExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#cdrExpression.
    def visitCdrExpression(self, ctx:schemeParser.CdrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#consExpression.
    def visitConsExpression(self, ctx:schemeParser.ConsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#nullExpression.
    def visitNullExpression(self, ctx:schemeParser.NullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#appendExpression.
    def visitAppendExpression(self, ctx:schemeParser.AppendExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#lengthExpression.
    def visitLengthExpression(self, ctx:schemeParser.LengthExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#displayExpression.
    def visitDisplayExpression(self, ctx:schemeParser.DisplayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#defineFunction.
    def visitDefineFunction(self, ctx:schemeParser.DefineFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#defineConstant.
    def visitDefineConstant(self, ctx:schemeParser.DefineConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#ifExpression.
    def visitIfExpression(self, ctx:schemeParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#condExpression.
    def visitCondExpression(self, ctx:schemeParser.CondExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#letExpression.
    def visitLetExpression(self, ctx:schemeParser.LetExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#functionCall.
    def visitFunctionCall(self, ctx:schemeParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#readExpression.
    def visitReadExpression(self, ctx:schemeParser.ReadExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:schemeParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:schemeParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#logicalExpression.
    def visitLogicalExpression(self, ctx:schemeParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#consultExpression.
    def visitConsultExpression(self, ctx:schemeParser.ConsultExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#newLine.
    def visitNewLine(self, ctx:schemeParser.NewLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#editConstantExpression.
    def visitEditConstantExpression(self, ctx:schemeParser.EditConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#numberLiteral.
    def visitNumberLiteral(self, ctx:schemeParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:schemeParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#stringLiteral.
    def visitStringLiteral(self, ctx:schemeParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#identifierLiteral.
    def visitIdentifierLiteral(self, ctx:schemeParser.IdentifierLiteralContext):
        return self.visitChildren(ctx)



del schemeParser