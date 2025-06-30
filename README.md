# DSL para Comparação de Preços

## Equipe
- **Pedro Afonso Cavalcanti Salvador**

---

## Motivação
Comparar preços de produtos com diferentes embalagens e unidades é uma tarefa tediosa e propensa a erros. Esta linguagem de domínio específico (DSL) foi criada para automatizar esse processo, permitindo que consumidores e empresas tomem decisões de compra mais inteligentes calculando automaticamente o melhor custo-benefício.
A ferramenta é especialmente útil para:
- Comparar produtos com unidades diferentes (ml, l, g, kg).
- Identificar promoções e descontos reais.
- Encontrar a opção mais econômica em uma lista de produtos.

---

## Descrição Informal da Linguagem
A DSL foi projetada para ser clara e acessível. Seu funcionamento é baseado no comando `compare`, seguido de uma lista de produtos com suas quantidades e preços.

Cada produto é descrito como:
- Nome (entre aspas).
- Quantidade numérica seguida da unidade (`ml`, `l`, `g`, `kg`, `oz`).
- Preço antecedido por `R$`.

---

## Passo a Passo da Execução
1. Pré-requisitos:
- Python 3.7 ou superior
- ANTLR 4 instalado e configurado
- Dependência ANTLR para Python:
```bash
pip install antlr4-python3-runtime
```
2. Clone o repositório:
```bash
git clone https://github.com/PedroAfonsoSalvador/ComparacaoPrecosDSL.git
cd ComparacaoPrecosDSL
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Gere os analisadores(caso já não existam):
```bash
antlr4 -Dlanguage=Python3 -o src/comparaprod -visitor -no-listener grammar/ComparaProd.g4
```
5. Execute com um arquivo de exemplo:
```bash
python src/main.py examples/exemplo1.cprod
```

---

## Exemplo de Programas
Exemplo 01:
Entrada
```bash
compare "Leite Integral" de 1l por R$ 5.90,
        "Leite Desnatado" de 900ml por R$ 5.50
```
Saída
```bash
Leite Integral:
  Quantidade: 1.0l
  Preço: R$5.90
  Preço por ml: R$0.0059 (MELHOR OPÇÃO)
----------------------------------------
Leite Desnatado:
  Quantidade: 900.0ml
  Preço: R$5.50
  Preço por ml: R$0.0061
```

Exemplo 02:
Entrada
```bash
compare "Sabão em Pó A" de 1kg por R$ 15.90 com 10% off,
        "Sabão em Pó B" de 800g por R$ 12.50,
        "Sabão em Pó C" de 1.2kg por R$ 18.00 com 15% off
```
Saída
```bash
Sabão em Pó A [PROMOÇÃO: 10% off]:
  Quantidade: 1.0kg
  Preço original: R$15.90
  Preço com desconto: R$14.31
  Preço por g: R$0.0143
----------------------------------------
Sabão em Pó B:
  Quantidade: 800.0g
  Preço: R$12.50
  Preço por g: R$0.0156
----------------------------------------
Sabão em Pó C [PROMOÇÃO: 15% off]:
  Quantidade: 1.2kg
  Preço original: R$18.00
  Preço com desconto: R$15.30
  Preço por g: R$0.0127 (MELHOR OPÇÃO)
```

Exemplo 03
Entrada
```bash
compare "Café X" de 250g por R$ 12.90,
        "Café Y" de 300g por R$ 15.50,
        "Café Z" de 1kg por R$ 45.00
```
Saída
```bash
Café X:
  Quantidade: 250.0g
  Preço: R$12.90
  Preço por g: R$0.0516
----------------------------------------
Café Y:
  Quantidade: 300.0g
  Preço: R$15.50
  Preço por g: R$0.0517
----------------------------------------
Café Z:
  Quantidade: 1.0kg
  Preço: R$45.00
  Preço por g: R$0.0450 (MELHOR OPÇÃO)
```
