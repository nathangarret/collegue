# Comando if: Decisão de caminho único e Duplo

print("Único: ")

temp = 91

if temp > 86:
    print("It is hot!")
    print("Be sure to drink liquids.")
print("Goodbye")

print("\nDuplo: ")

temp = 12

if temp > 86:
    print("It is hot!")
    print("Be sure to drink liquids.")
else:
    print("It is not hot!")
    print("Bring a jacket")
print("Goodbye.")

# Múltiplos caminhos
print("\nMúltiplos: ")

def temperature(t):
    if t > 86:
        print("It is hot!")
    elif t > 32:
        print("It is cold!")
    else:
        print("It is freezing!")
    print("Goodbye")

temperature(99)

print("\nExplicita x Implicita")

# Explicita x Implicita
def temperature(t):
    if t <= 86 and t > 32:
        print("It is cold!")
    elif t > 86:
        print("It is hot!")
    else:
        print("It is freezing!")
    print("Goodbye")

temperature(86)

# Cálculo IMC
print("\nCálculo IMC")
def meuIMC(peso, altura):
    imc = peso / (altura**2)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Normal")
    else:
        print("Sobrepeso")

meuIMC(1.85, 85)

# Season
def season(month):
    if 1 <= month <= 3:
        print("Inverno")
    elif 4 <= month <= 6:
        print("Primaveira")
    elif 7 <= month <= 9:
        print("Verão")
    elif 10 <= month <= 12:
        print("Outono")
    else:
        print("Digite um mês válido!")

season(3)
season(100)

# Equação de 2° Grau

print("\nEquação de 2° Grau")
import math as mt

def equacaoSegundoGrau(a, b, c):
    delta = b**2 - 4 * a * c

    if delta < 0:
        return "Não tem solução"
    elif delta == 0:
        return -b / (2 * a)
    else:
        r1 = (-b - mt.sqrt(delta)) / 2 * a
        r2 = (-b + mt.sqrt(delta)) / 2 * a
        return(r1, r2)
    
print(equacaoSegundoGrau(1, 2, 1))
print(equacaoSegundoGrau(1, 0, -1))
print(equacaoSegundoGrau(1, 0, 1))