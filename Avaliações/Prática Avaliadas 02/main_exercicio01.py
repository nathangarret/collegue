# Exercício 1

# Escreva uma função chamada diferente() que recebe uma tabela bidimensional como parâmetro e retorna o número de entradas distintas na tabela. Sua função deve funcionar da seguinte forma:
""" 
>>> t = [[1,0,1],[0,1,0]]
>>> diferente(t)
2 
"""

def diferente(table):
    return len(set(element for line in table for element in line)) # set - valores únicos

s = [[1, 0, 1], [0, 1, 0]]
print(s)
print(diferente(s))

t = [[32, 12, 52, 63], [32, 64, 67, 52], [64, 64, 17, 34],[34, 17, 76, 98]]
print(t)
print(diferente(t))