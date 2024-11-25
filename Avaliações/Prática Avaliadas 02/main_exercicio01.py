# Exercício 1

# Escreva uma função chamada diferente() que recebe uma tabela bidimensional como parâmetro e retorna o número de entradas distintas na tabela. Sua função deve funcionar da seguinte forma:

""" 
>>> t = [[1,0,1],[0,1,0]]
>>> diferente(t)
2 
"""

def diferente(tabela):
    elementos_distintos = []

    for linha in tabela: # 
        for elemento in linha: # 
            if elemento not in elementos_distintos:
                elementos_distintos.append(elemento) # 
    
    return len(elementos_distintos) # Retornar a quantidade de elementos_distintos

s = [[1, 0, 1], [0, 1, 0]]
t = [[32, 12, 52, 63], [32, 64, 67, 52], [64, 64, 17, 34],[34, 17, 76, 98]]
print(diferente(s))
print(diferente(t))