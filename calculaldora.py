Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
while True:
    print("\nEscolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Saindo...")
        break
    elif escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

...         if escolha == '1':
...             resultado = num1 + num2
...             print(f"O resultado da adição é: {resultado}")
...         elif escolha == '2':
...             resultado = num1 - num2
...             print(f"O resultado da subtração é: {resultado}")
...         elif escolha == '3':
...             resultado = num1 * num2
...             print(f"O resultado da multiplicação é: {resultado}")
...         elif escolha == '4':
...             if num2 == 0:
...                 print("Erro: Divisão por zero não é permitida.")
...             else:
...                 resultado = num1 / num2
...                 print(f"O resultado da divisão é: {resultado}")
...     else:
...         print("Escolha inválida. Tente novamente.")
... 

Escolha uma operação:
1 - Adição
2 - Subtração

... 3 - Multiplicação
4 - Divisão
5 - Sair
Digite o número da operação desejada: 4
Digite o primeiro número: 55
Digite o segundo número: 6
O resultado da divisão é: 9.166666666666666

Escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
Digite o número da operação desejada: 5
Saindo...
>>> 
