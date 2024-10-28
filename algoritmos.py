""" 
lista_mes = ['Janeiro', 'Fevereiro', 'Março',]

for elemento in lista_mes:
    print(elemento[:3])
 
"""

""" 
# Pede um nome e imprime na vertical
nome = input("Digite um nome: ")

for elemento in nome:
    print(elemento)

def menorQue10(lst):
    return [num for num in lst if num < 10]

x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(menorQue10(x)) 
"""

""" 
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in lst:
    if item < 10:
        print(item) 
        
"""

# Número primo
numero = eval(input('Diga um número: '))
contagem = 0

for num in range(1, numero+1):
    if numero % num == 0:
        contagem += 1
if contagem == 2:
    print('Primo')
else:
    print('Composto')