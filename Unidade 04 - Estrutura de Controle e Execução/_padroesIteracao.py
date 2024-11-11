# Iteranado todos os itens de uma sequência *explícita*

for word in ['stop', 'desktop', 'post', 'top']:
    if 'ost' in word:
        print(word)
print('Done')

# Iterando caracteres de um arquivo texto

import os

caminho_pasta = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_pasta, 'test.txt')

with open(caminho_arquivo, 'r', encoding='utf-8') as arq:
    content_caracteres = arq.read() # caracteres
    for char in content_caracteres:
        print(char, end='') 

    content_lines = arq.readlines() # linhas
    for line in content_lines:
        print(line, end='')

# Implicita índices - range() sequências
print("\nImplicita índices - range() sequências")
n = 10

for i in range(n):
    print(i, end=' ')

print("\n")

for j in range(7, 100, 17):
    print(j, end=' ')

print("\n")

k = 0
word = 'abcdefghijklmnopqrstuvwxyz'

for k in range(len(word)):
    print(k, end=' ') # ?

print("\n")

pets = ['cat', 'dog', 'fish', 'bird']

# Acessando direto a lista
for animal in pets:
    print(animal, end=' ')

print("\n")

# Laço untador
# Acessando os items da lista
for l in range(len(pets)):
    print(pets[l], end=' ')

print("\n")

# função checkSorted():
# Checar se o [] está ordenado ou não
def checkSorted(lst):
    for num in range(len(lst)-1):
        if lst[num] > lst[num+1]:
            return False
    return True

print(checkSorted([1, 1, 3]))

print("\n")

# Acumulador
# calcular valor de []
lst = [1, 3, 7]
soma=0

for num in lst:
    soma+=num

print(soma)

# Calcular o produto de []
lst = [2, 4, 2]
mult = 1

for num in lst:
    mult *= num

print(mult)

print("\n")

# Calcule o fatorial de um número
def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(fatorial(1))
print(fatorial(3))
print(fatorial(4))
print(fatorial(6))

# Divisores de um número
def divisors(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

print(divisors(1))
print(divisors(6))
print(divisors(11))
print(divisors(37))