# Import para fazer a mediana
import statistics

L = [94, 86, 85, 81, 86, 96, 91, 85, 86, 83, 89, 81, 86, 98, 84]

# Qual é o menor valor em L?
print(min(L))

# Qual é o maior valor em L?
print(max(L))

# Qual é o valor médio de L?
mediaL = sum(L) / len(L)
print(mediaL)

# Qual é a mediana dos valores em L?
"""  
mediana = soma - min(numeros) - max(numeros)
medianaL = sum(L) - min(L) - max(L)
print(medianaL)
"""

medianaL = statistics.median(L)
print(medianaL)

# Quantos dos valores são 85?
print(L.count(85))