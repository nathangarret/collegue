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

print("\nMétodos de listas: ")

lst = [1, 2, 3]

lst.append(7)
lst.append(3)
print(lst)

print(lst.count(3))

lst.remove(2)
print(lst)

lst.reverse()
print(lst)