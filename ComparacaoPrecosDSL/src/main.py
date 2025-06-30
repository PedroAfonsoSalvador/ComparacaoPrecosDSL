import sys
import os
from comparaprod.interpreter import interpret

def main():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py <arquivo.cprod>")
        return
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        results = interpret(content)
        
        print("\nResultado da Comparação:")
        print("-" * 60)
        for product in results:
            status = " (MELHOR OPÇÃO)" if product.get('is_best', False) else ""
            promotion_info = f" [PROMOÇÃO: {product['discount']*100:.0f}% off]" if product['has_promotion'] else ""
            
            print(f"{product['name']}{promotion_info}:")
            print(f"  Quantidade: {product['quantity']}{product['unit']}")
            print(f"  Preço original: R${product['original_price']:.2f}")
            if product['has_promotion']:
                print(f"  Preço com desconto: R${product['discounted_price']:.2f}")
            print(f"  Preço efetivo por {product['base_unit']}: R${product['effective_price_per_unit']:.4f}{status}")
            print("-" * 60)
            
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro durante a interpretação: {str(e)}")

if __name__ == "__main__":
    # Adiciona o diretório src ao PATH
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()