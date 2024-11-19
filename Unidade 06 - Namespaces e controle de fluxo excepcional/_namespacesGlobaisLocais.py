# Escopo: namespaces global vs local

# • O namespace é onde os nomes definidos durante a execução da função são armazenados - O escopo desses nomes é o namespace da função

# De fato, todo nome em Python tem um escopo:
# • Seja um nome de uma variável, função, classe, ...
# • Nomes definidos no shell ou em um módulo fora de qualquer função são ditas ter escopo global

# Global
x = 5

print(x)

# Local
def f(b):
    a = 9
    return a * b

a = 0

print('f(3) = {}'.format(f(3))) # Chamada da função
print('a({}) = {}'.format(a, a)) # Chamada da variável global

# Quando o interpretador avalia uma variável, como ele identifica as diferenças entre local e global?
# • O namespace da chamada da função delimitadora (def f(b))
# • O namespace global (módulos)
# • O namespace do módulo builtins (print())

print("=== RESTART ===")

def h(c):
    global a
    a = 6 # Se torna global em todo o escopo

    return a * c

a = 0
print('h(3) = {}'.format(h(3)))
print('a({}) = {}'.format(a, a))