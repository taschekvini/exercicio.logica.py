import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um número de 1 a 100: "))
    tentativas += 1

    if palpite == numero:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        break
    elif palpite < numero:
        print("Dica: maior")
    else:
        print("Dica: menor") 