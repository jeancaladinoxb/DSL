# Generated from DeepLearning.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DeepLearningParser import DeepLearningParser
else:
    from DeepLearningParser import DeepLearningParser

# This class defines a complete listener for a parse tree produced by DeepLearningParser.
class DeepLearningListener(ParseTreeListener):

    # Enter a parse tree produced by DeepLearningParser#program.
    def enterProgram(self, ctx:DeepLearningParser.ProgramContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#program.
    def exitProgram(self, ctx:DeepLearningParser.ProgramContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#statement.
    def enterStatement(self, ctx:DeepLearningParser.StatementContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#statement.
    def exitStatement(self, ctx:DeepLearningParser.StatementContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#assignment.
    def enterAssignment(self, ctx:DeepLearningParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#assignment.
    def exitAssignment(self, ctx:DeepLearningParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#assignNoSemi.
    def enterAssignNoSemi(self, ctx:DeepLearningParser.AssignNoSemiContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#assignNoSemi.
    def exitAssignNoSemi(self, ctx:DeepLearningParser.AssignNoSemiContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#matrixDecl.
    def enterMatrixDecl(self, ctx:DeepLearningParser.MatrixDeclContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#matrixDecl.
    def exitMatrixDecl(self, ctx:DeepLearningParser.MatrixDeclContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#matrixLiteral.
    def enterMatrixLiteral(self, ctx:DeepLearningParser.MatrixLiteralContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#matrixLiteral.
    def exitMatrixLiteral(self, ctx:DeepLearningParser.MatrixLiteralContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#row.
    def enterRow(self, ctx:DeepLearningParser.RowContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#row.
    def exitRow(self, ctx:DeepLearningParser.RowContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#modelDecl.
    def enterModelDecl(self, ctx:DeepLearningParser.ModelDeclContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#modelDecl.
    def exitModelDecl(self, ctx:DeepLearningParser.ModelDeclContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#mlpDecl.
    def enterMlpDecl(self, ctx:DeepLearningParser.MlpDeclContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#mlpDecl.
    def exitMlpDecl(self, ctx:DeepLearningParser.MlpDeclContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:DeepLearningParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:DeepLearningParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#printStmt.
    def enterPrintStmt(self, ctx:DeepLearningParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#printStmt.
    def exitPrintStmt(self, ctx:DeepLearningParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#args.
    def enterArgs(self, ctx:DeepLearningParser.ArgsContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#args.
    def exitArgs(self, ctx:DeepLearningParser.ArgsContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#ifStmt.
    def enterIfStmt(self, ctx:DeepLearningParser.IfStmtContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#ifStmt.
    def exitIfStmt(self, ctx:DeepLearningParser.IfStmtContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#forStmt.
    def enterForStmt(self, ctx:DeepLearningParser.ForStmtContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#forStmt.
    def exitForStmt(self, ctx:DeepLearningParser.ForStmtContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#whileStmt.
    def enterWhileStmt(self, ctx:DeepLearningParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#whileStmt.
    def exitWhileStmt(self, ctx:DeepLearningParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#doWhileStmt.
    def enterDoWhileStmt(self, ctx:DeepLearningParser.DoWhileStmtContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#doWhileStmt.
    def exitDoWhileStmt(self, ctx:DeepLearningParser.DoWhileStmtContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#funcDecl.
    def enterFuncDecl(self, ctx:DeepLearningParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#funcDecl.
    def exitFuncDecl(self, ctx:DeepLearningParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#params.
    def enterParams(self, ctx:DeepLearningParser.ParamsContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#params.
    def exitParams(self, ctx:DeepLearningParser.ParamsContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#returnStmt.
    def enterReturnStmt(self, ctx:DeepLearningParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#returnStmt.
    def exitReturnStmt(self, ctx:DeepLearningParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#block.
    def enterBlock(self, ctx:DeepLearningParser.BlockContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#block.
    def exitBlock(self, ctx:DeepLearningParser.BlockContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#expr.
    def enterExpr(self, ctx:DeepLearningParser.ExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#expr.
    def exitExpr(self, ctx:DeepLearningParser.ExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#equalityExpr.
    def enterEqualityExpr(self, ctx:DeepLearningParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#equalityExpr.
    def exitEqualityExpr(self, ctx:DeepLearningParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#relationalExpr.
    def enterRelationalExpr(self, ctx:DeepLearningParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#relationalExpr.
    def exitRelationalExpr(self, ctx:DeepLearningParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#addExpr.
    def enterAddExpr(self, ctx:DeepLearningParser.AddExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#addExpr.
    def exitAddExpr(self, ctx:DeepLearningParser.AddExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#mulExpr.
    def enterMulExpr(self, ctx:DeepLearningParser.MulExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#mulExpr.
    def exitMulExpr(self, ctx:DeepLearningParser.MulExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#powExpr.
    def enterPowExpr(self, ctx:DeepLearningParser.PowExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#powExpr.
    def exitPowExpr(self, ctx:DeepLearningParser.PowExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#unaryExpr.
    def enterUnaryExpr(self, ctx:DeepLearningParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#unaryExpr.
    def exitUnaryExpr(self, ctx:DeepLearningParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#primary.
    def enterPrimary(self, ctx:DeepLearningParser.PrimaryContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#primary.
    def exitPrimary(self, ctx:DeepLearningParser.PrimaryContext):
        pass


    # Enter a parse tree produced by DeepLearningParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:DeepLearningParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by DeepLearningParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:DeepLearningParser.ArrayLiteralContext):
        pass



del DeepLearningParser