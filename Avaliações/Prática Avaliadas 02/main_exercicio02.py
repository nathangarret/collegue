# Exercício 2

# O método index() da classe list retorna o índice da primeira ocorrência do valor na lista. Entretanto, caso o valor não esteja na lista, uma exceção é levantada. 

# Implemente uma função chamada safeIndex() que recebe como entradas uma lista e um valor e retorna o índice da primeira ocorrência do valor na lista. Caso o valor não esteja na lista, a função deve imprimir uma mensagem informando que o valor não está na lista e retornar None

def safe_index(lst, value):
    try:
        return (f"O valor está na posição: {lst.index(value)} da lista.")
    except ValueError:
        print(f"O valor '{value}' não está na lista.")
        return None

lst = [23,42,54,39]

# numeros = [10, 20, 30, 40, 50]
print(safe_index(lst, 54))

# Tipos de excessão:
# • ValueError Levantado quando a operação ou função tem um argumento com tipo correto, mas com valor incorreto
