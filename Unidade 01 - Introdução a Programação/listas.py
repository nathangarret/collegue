# Listas

listaUm = ['opa', 'tudo', 'bem?']
listaDois = [0, 1, 'two', 'three', [4, 'five']]

listaNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(listaNumbers))
print(sum(listaNumbers))

# Métodos de lista

listaNumbers.append(11)
print(listaNumbers)
print(sum(listaNumbers))

"""
listaNumbers.append() # Adiciona um item no final da lista
listaNumbers.count() # Retorna o número de ocorrências de item de uma lista
listaNumbers.index() # Retorna o índice (de primeira ocorrência) de item em uma lista
listaNumbers.pop() # Remove e retorna o último elemento de uma lista
listaNumbers.remove() # Remove a primeira ocorrência de uma lista
listaNumbers.reverse() # Inverte a ordem dos elementos de uma lista
listaNumbers.sort() # Ordena os elementos de umna lista em ordem crescente
"""

""" 

Os métodos append(), remove(), reverse() e sort() não retornam nenhum valor;
Eles e o método pop() modificam a lista!

"""

# Exibe uma mensagem na tela com uma linha em branco antes do texto
print("\nMétodos de listas: ")

# Define uma lista inicial com três elementos
lst = [1, 2, 3]

# Adiciona o número 7 ao final da lista
lst.append(7)
# Adiciona mais um 3 ao final da lista
lst.append(3)
# Exibe a lista atualizada: [1, 2, 3, 7, 3]
print(lst)

# Conta quantas vezes o número 3 aparece na lista
print(lst.count(3))  # Saída: 2

# Remove a primeira ocorrência do número 2 na lista
lst.remove(2)
# Exibe a lista após a remoção: [1, 3, 7, 3]
print(lst)

# Inverte a ordem dos elementos da lista
lst.reverse()
# Exibe a lista invertida: [3, 7, 3, 1]
print(lst)

# Retorna o índice da primeira ocorrência do número 3
print(lst.index(3))  # Saída: 0

# Ordena os elementos da lista em ordem crescente
lst.sort()
# Exibe a lista ordenada: [1, 3, 3, 7]
print(lst)

# Remove a primeira ocorrência do número 3
lst.remove(3)
# Exibe a lista após a remoção: [1, 3, 7]
print(lst)

# Remove e retorna o último elemento da lista
print(lst.pop())  # Saída: 7

# Exibe a lista final após a remoção do último elemento: [1, 3]
print(lst)