# Generated from .\ExprParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

from ExprLexer import ExprLexer

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        # self.visitChildren(ctx)
        print(ctx.getText())
        print("the expr is ",ctx.expr().getText())
        return self.visit(ctx.expr())


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        # 永远不要直接操作terminal
        print("enter Expr",ctx.getText())
        if ctx.LPAREN():
            return self.visit(ctx.expr(0))
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.MUL():
            return self.visit(ctx.getChild(0)) * self.visit(ctx.getChild(2)) 
        elif ctx.DIV():
            return self.visit(ctx.getChild(0)) / self.visit(ctx.getChild(2)) 
        elif ctx.POW():
            return self.visit(ctx.getChild(0)) ** self.visit(ctx.getChild(2)) 
        elif ctx.PLUS():
            return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(2)) 
        elif ctx.MINUS():
            return self.visit(ctx.getChild(0)) - self.visit(ctx.getChild(2)) 
        print("not caught")
        return self.visitChildren(ctx)
    


if __name__ == "__main__":
    import sys
    from io import *
    print("receive ",sys.argv[1])
    tree = ExprParser(CommonTokenStream( ExprLexer(  InputStream(sys.argv[1])))).program()
    l = ExprParserVisitor()
    print(type(tree))
    print(l.visitProgram(tree))   # 在这里 tree 只是这棵树的根，通过visit需要顺便将其所有子节点也visit 因此我们需要在方法里visit 所有子节点


del ExprParser