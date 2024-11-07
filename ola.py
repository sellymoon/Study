Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def saudacao(Damdam): 
...     print("Olá, " + Damdam + "! Como você está?") 
...     resposta = input("Bem e você? ") 
...     
...     if resposta.lower() == "estou bem":
...         print("Ótimo! Fico feliz em ouvir isso. 😊")
...     elif resposta.lower() == "estou mal":
...         print("Sinto muito que você esteja se sentindo assim. Espero que melhore logo! ❤️")
...     else:
...         print("Legal! É sempre bom ter um bom dia. 🌼")
... 
...         
>>> nomes = ["Gabriel", "Selena", "Damdam"]
... 
>>> repetir = "s"
... 
>>> while repetir.lower() == "s":
...     for nome in nomes:
...         saudacao(nome)
... 
...     repetir = input("Deseja repetir? (s/n): ")
... 
... 
Olá, Gabriel! Como você está?
Bem e você? 
Legal! É sempre bom ter um bom dia. 🌼
Olá, Selena! Como você está?
Bem e você? ESTOU MAL
Sinto muito que você esteja se sentindo assim. Espero que melhore logo! ❤️
Olá, Damdam! Como você está?
Bem e você? legal
Legal! É sempre bom ter um bom dia. 🌼
