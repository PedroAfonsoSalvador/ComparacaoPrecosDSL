from .ComparaProdVisitor import ComparaProdVisitor
from .ComparaProdParser import ComparaProdParser

class ComparaProdVisitorImpl(ComparaProdVisitor):
    def __init__(self):
        self.products = []
        self.conversion_rates = {
            'ml': 1,
            'l': 1000,
            'g': 1,
            'kg': 1000,
            'oz': 28.3495
        }

    def visitProgram(self, ctx: ComparaProdParser.ProgramContext):
        for comparison in ctx.comparison():
            if comparison.getChildCount() > 0:  # Ignora linhas vazias
                self.visitComparison(comparison)
        return self.products

    def visitComparison(self, ctx: ComparaProdParser.ComparisonContext):
        products = []
        for product_ctx in ctx.product():
            products.append(self.visitProduct(product_ctx))
        
        best_product = min(products, key=lambda x: x['effective_price_per_unit'])
        best_product['is_best'] = True
        for p in products:
            if p != best_product:
                p['is_best'] = False
        
        self.products.extend(products)
        return products

    def visitProduct(self, ctx: ComparaProdParser.ProductContext):
        name = ctx.STRING().getText().strip('"')
        quantity_info = self.visitQuantity(ctx.quantity())
        price = float(ctx.price().NUMBER().getText())
        
        # Processar promoção se existir
        discount = 0.0
        if ctx.promotion():
            discount = float(ctx.promotion().NUMBER().getText()) / 100
            discounted_price = price * (1 - discount)
        else:
            discounted_price = price
        
        # Determinar unidade base
        if quantity_info['unit'] in ['ml', 'l', 'oz']:
            base_unit = 'ml'
        else:
            base_unit = 'g'
            
        converted_quantity = quantity_info['value'] * self.conversion_rates[quantity_info['unit']]
        effective_price_per_unit = discounted_price / converted_quantity
        
        return {
            'name': name,
            'quantity': quantity_info['value'],
            'unit': quantity_info['unit'],
            'original_price': price,
            'discount': discount,
            'discounted_price': discounted_price,
            'converted_quantity': converted_quantity,
            'base_unit': base_unit,
            'effective_price_per_unit': effective_price_per_unit,
            'is_best': False,
            'has_promotion': ctx.promotion() is not None
        }

    def visitQuantity(self, ctx: ComparaProdParser.QuantityContext):
        value = float(ctx.NUMBER().getText())
        unit = ctx.unit().getText()
        return {'value': value, 'unit': unit}

    def visitPrice(self, ctx: ComparaProdParser.PriceContext):
        return float(ctx.NUMBER().getText())

    def visitPromotion(self, ctx: ComparaProdParser.PromotionContext):
        return float(ctx.NUMBER().getText())