Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome = input("Qual é o seu nome? ")
... idade = input("Quantos anos você tem? ")
... nota = float(input("Qual é a sua nota? "))
... 
... print(f"Prazer em te conhecer, {nome}!")
... 
... if nota >= 6:
...     print("Você está aprovado!")
... elif nota >= 4:
...     print("Você está de recuperação!")
... else:
