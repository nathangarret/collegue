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

# Escreva uma função chamada hello() que:
# • Recebe um nome (uma string) como entrada
# • Imprime uma mensagem de boas-vindas personalizada
def hello(string):
  return "Olá, " + string + ", boas-vindas ao mundo Python."

print(hello('Nathan'))

# Escreva uma função chamada rng() que:
# • Recebe uma lista como parâmetro de entrada
# • Retorna o intervalo dos números (isto é a maior diferença entre elementos da lista)
def rng(list):
  intervaloNumeros = max(list) - min(list)
  return intervaloNumeros
  
print(rng([4, 0, 1, -2]))

# Programas Python devem ser documentados
# • Para manutenção do código
# • Para uso do código

"""  
Comentários
def f(x):
res = x**2 + 10 #calcula o resultado
return res #retorna resultado

Docstring
def f(x):
'retorna x**2 + 10'
res = x**2 + 10 #calcula o resultado
return res #retorna resultado
"""