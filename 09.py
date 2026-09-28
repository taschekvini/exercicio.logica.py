valor = float(input("Digite o valor da compra: "))
if valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"O valor final com desconto é: R$ {valor_final:.2f}")    