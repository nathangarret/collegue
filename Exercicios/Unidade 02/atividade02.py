""" 
Escreva um programa que permita ao usuário inserir uma lista de nomes e depois imprima o primeiro e o último nome da lista em ordem lexicográfica (dicionário). Um exemplo de execução é mostrado a seguir:
"""

listaNome = input("Insira uma lista de nomes: ").split()

print(listaNome)

if listaNome:
    listaNome.sort()
    
    print("O primeiro nome é: ", listaNome[0])
    print("O último nome é: ", listaNome[-1])
else:
    print("A lista está vazia ;(")