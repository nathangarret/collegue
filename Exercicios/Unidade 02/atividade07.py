""" 
Escreva uma função chamada average(), que recebe como entrada uma lista de valores numéricos. A função deve retornar a média dos valores na lista. Se a lista for vazia, a função deve retornar o valor 0.

Um exemplo de execução é mostrado a seguir:

>>> lst = [1, 3, 4]
>>> average(lst)
2.6666666666666665
>>> average([])
0 
"""

def average(lst):
    if not lst: # A função usa if not values para verificar se a lista está vazia. Se estiver, retorna 0.
        return 0
    return sum(lst) / len(lst)
    
lst = [1, 3, 4]
print(f"{average(lst)}")

print(average([]))