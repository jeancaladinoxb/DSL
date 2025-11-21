# Generated from DeepLearning.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DeepLearningParser import DeepLearningParser
else:
    from DeepLearningParser import DeepLearningParser

# This class defines a complete generic visitor for a parse tree produced by DeepLearningParser.

class DeepLearningVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeepLearningParser#program.
    def visitProgram(self, ctx:DeepLearningParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#statement.
    def visitStatement(self, ctx:DeepLearningParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#assignment.
    def visitAssignment(self, ctx:DeepLearningParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#assignNoSemi.
    def visitAssignNoSemi(self, ctx:DeepLearningParser.AssignNoSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#matrixDecl.
    def visitMatrixDecl(self, ctx:DeepLearningParser.MatrixDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#matrixLiteral.
    def visitMatrixLiteral(self, ctx:DeepLearningParser.MatrixLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#row.
    def visitRow(self, ctx:DeepLearningParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#modelDecl.
    def visitModelDecl(self, ctx:DeepLearningParser.ModelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#mlpDecl.
    def visitMlpDecl(self, ctx:DeepLearningParser.MlpDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:DeepLearningParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#printStmt.
    def visitPrintStmt(self, ctx:DeepLearningParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#args.
    def visitArgs(self, ctx:DeepLearningParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#ifStmt.
    def visitIfStmt(self, ctx:DeepLearningParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#forStmt.
    def visitForStmt(self, ctx:DeepLearningParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#whileStmt.
    def visitWhileStmt(self, ctx:DeepLearningParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:DeepLearningParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#funcDecl.
    def visitFuncDecl(self, ctx:DeepLearningParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#params.
    def visitParams(self, ctx:DeepLearningParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#returnStmt.
    def visitReturnStmt(self, ctx:DeepLearningParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#block.
    def visitBlock(self, ctx:DeepLearningParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#expr.
    def visitExpr(self, ctx:DeepLearningParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#equalityExpr.
    def visitEqualityExpr(self, ctx:DeepLearningParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#relationalExpr.
    def visitRelationalExpr(self, ctx:DeepLearningParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#addExpr.
    def visitAddExpr(self, ctx:DeepLearningParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#mulExpr.
    def visitMulExpr(self, ctx:DeepLearningParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#powExpr.
    def visitPowExpr(self, ctx:DeepLearningParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#unaryExpr.
    def visitUnaryExpr(self, ctx:DeepLearningParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#primary.
    def visitPrimary(self, ctx:DeepLearningParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:DeepLearningParser.ArrayLiteralContext):
        return self.visitChildren(ctx)



del DeepLearningParser