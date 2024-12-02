# Exercício 2

# O método index() da classe list retorna o índice da primeira ocorrência do valor na lista. Entretanto, caso o valor não esteja na lista, uma exceção é levantada. 

# Implemente uma função chamada safeIndex() que recebe como entradas uma lista e um valor e retorna o índice da primeira ocorrência do valor na lista. Caso o valor não esteja na lista, a função deve imprimir uma mensagem informando que o valor não está na lista e retornar None

def safeIndex(lista, valor):
    try:
        return(f"O valor '{valor}' está na posição: {lista.index(valor)} da lista.")
    except ValueError:
        print(f"O valor '{valor}' não está na posição")
        return None

lst = [23,42,54,39]
print(lst)
print(safeIndex(lst, 11))

# Tipos de excessão:
# • ValueError