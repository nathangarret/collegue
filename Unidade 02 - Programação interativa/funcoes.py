# Vimos algumas funções predefinidas •abs(), max(), len(), sum(), print()

def f(x):
    res = x*2 + 10
    return res

print(f(2))

# def: palavra chave para definição de função 
# f: nome da função 
# x: nome da variável que representa o argumento de entrada
# return: especifica o retorno da função

# Dica importante return vs print
# *return* dentro da função - A função retorna o valor res que pode ser usado em uma expressão
# *print* dentro da função - A função *print* res, mas não retorna nad

"""
def <function name> (<0 or more variables>):
  <indented function body>
"""

import math

def hip(a, b):
    res = math.sqrt(a**2 + b**2)
    return res

print(hip(3, 4))    