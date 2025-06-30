# Generated from grammar/ComparaProd.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComparaProdParser import ComparaProdParser
else:
    from ComparaProdParser import ComparaProdParser

# This class defines a complete generic visitor for a parse tree produced by ComparaProdParser.

class ComparaProdVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComparaProdParser#program.
    def visitProgram(self, ctx:ComparaProdParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComparaProdParser#comparison.
    def visitComparison(self, ctx:ComparaProdParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComparaProdParser#product.
    def visitProduct(self, ctx:ComparaProdParser.ProductContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComparaProdParser#quantity.
    def visitQuantity(self, ctx:ComparaProdParser.QuantityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComparaProdParser#unit.
    def visitUnit(self, ctx:ComparaProdParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComparaProdParser#price.
    def visitPrice(self, ctx:ComparaProdParser.PriceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComparaProdParser#promotion.
    def visitPromotion(self, ctx:ComparaProdParser.PromotionContext):
        return self.visitChildren(ctx)



del ComparaProdParser