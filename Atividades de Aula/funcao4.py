def calcular_desconto(preco, porcentagem):
    valor_desconto = preco * (porcentagem / 100)
    preco_final = preco - valor_desconto

    print("\n===== RESUMO DA COMPRA =====")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto: {porcentagem:.0f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")


preco = float(input("Digite o valor do produto: R$ ").replace(",", "."))
porcentagem = float(input("Digite a porcentagem de desconto (%): ").replace(",", "."))

calcular_desconto(preco, porcentagem)