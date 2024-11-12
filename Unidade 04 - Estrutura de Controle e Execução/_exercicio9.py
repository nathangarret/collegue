""" 
Escreva uma função chamada pairs() que toma como entrada duas listas de mesmo comprimento x = [x0, x1, x2, ..., xn] e y = [y0, y1, y2, ..., yn] e retorne a lista dos pares (tuplas):

[(x1, y1), (x1, y1), (x2, y2), ... , (xn, yn )].
Como exemplo de execução:

>>> pairs([2,3,4], 
        [1,0,2])
[(2, 1), (3, 0), (4, 2)]
"""

def pairs(x, y):
    if len(x) != len(y):
        return []

    return list(zip(x, y))  # A função é útil para criar pares de elementos de várias iteráveis

print(pairs([2,3,4], [1,0,2])) # [(2, 1), (3, 0), (4, 2)]