import random

while True:
    print("\nEscolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Número aleatório")
    print("6 - Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '6':
        print("Até logo, e vê se estuda...")
        break
    elif escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            print(f"O resultado da adição é: {resultado}. Conta nos dedos na próxima...")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}. Ai ai, espero que não esteja triste com isso!")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}. Olha só, você multiplicou sua sabedoria!")
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida. Se soubesse o básico...")
            else:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}. Cuidado para não se perder na matemática!")
    elif escolha == '5':
        num_aleatorio = random.randint(1, 100)
        print(f"O número aleatório gerado é: {num_aleatorio}. E aí, gostou?")
    else:
        print("Escolha inválida. Tente novamente, vai...")
