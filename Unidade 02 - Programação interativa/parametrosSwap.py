# Passagem de parâmetros

# Uma variável não existe antes da sua atribuição
# <variable> = <expression>

""" 
1.<expression> é avaliada e seu valor é 
armazenado em um objeto do tipo apropriado

2.O objeto é atribuído ao nome <variable>
"""

# Atribuímos o valor 3 à variável 'a'
a = 3

# Atribuímos o resultado da soma 2 + 1.3 à variável 'b'.
# Como a operação envolve um inteiro e um float, o resultado é do tipo float.
b = 2 + 1.3

# Exibimos o tipo da variável 'b', que será <class 'float'>.
print(type(b))  # Saída: <class 'float'>

# A variável 'c' recebe a string 'three'. Strings são imutáveis.
c = 'three'

# A lista 'd' é criada concatenando duas listas [1, 2] e [3].
# O resultado é a lista [1, 2, 3].
d = [1, 2] + [3]

# Exibe o valor de 'a', que inicialmente é 3.
print(a)  # Saída: 3

# Reatribuímos o valor 6 à variável 'a'.
a = 6

# Exibe o valor atualizado de 'a', que agora é 6.
print(a)  # Saída: 6

# Exibe a lista 'd', que foi criada como [1, 2, 3].
print(d)  # Saída: [1, 2, 3]

# Modificamos o segundo elemento da lista 'd' (índice 1) de 2 para 7.
d[1] = 7

# Exibe a lista 'd' após a modificação: [1, 7, 3].
print(d)  # Saída: [1, 7, 3]

# Exibe o valor atual de 'a', que é 6.
print(a)  # Saída: 6

# Exibe o valor atual de 'b', que é 3.3.
print(b)  # Saída: 3.3

# Atribuímos à variável 'b' o valor de 'a' (que é 6).
# Agora, 'b' armazena 6, mas como é uma cópia de um valor imutável,
# mudanças em 'a' não afetarão 'b'.
b = a

# Exibe o valor de 'b', que agora é 6.
print(b)  # Saída: 6

# Mudamos o valor de 'a' para 9. Como inteiros são imutáveis,
# isso não afeta a variável 'b', que continua com o valor 6.
a = 9

# Exibe o valor de 'b', que permanece 6.
print(b)  # Saída: 6

# Atribuímos à variável 'c' a referência da lista 'd'.
# Agora, 'c' e 'd' referenciam o mesmo objeto na memória.
c = d

# Exibe o conteúdo de 'c', que é [1, 7, 3].
print(c)  # Saída: [1, 7, 3]

# Modificamos o terceiro elemento da lista 'd' (índice 2) de 3 para 9.
d[2] = 9

# Como 'c' e 'd' referenciam a mesma lista, a mudança em 'd'
# também é refletida em 'c'.
print(c)  # Saída: [1, 7, 9]

# Troca (Swap) de valores
a = 3
b = 6
print(a, b)

tmp = b
b = a
a = tmp
print(a, b)

i = 1
j = 3
print(i, j)

tmp = j
j = i
i = tmp
print(i, j)

# Passagem de parâmetros mutáveis
# Definimos uma função chamada 'h' que recebe um parâmetro 'l'.
# Esse parâmetro 'l' será uma referência para qualquer lista passada
# como argumento ao chamar a função.
def h(l):
    # Alteramos o valor do primeiro elemento da lista (índice 0) para 5.
    # Como listas são MUTÁVEIS, essa alteração vai afetar a lista original
    # passada como argumento, pois 'l' e a lista original referenciam
    # o mesmo objeto na memória.
    l[0] = 5

# Criamos uma lista chamada 'lst' com três elementos: [1, 2, 3].
lst = [1, 2, 3]

# Chamamos a função 'h' passando 'lst' como argumento.
# Isso significa que 'l' dentro da função vai referenciar a mesma lista
# que 'lst' (ou seja, ambas apontam para o mesmo objeto na memória).
h(lst)

# A função 'h' não tem um retorno explícito, então ela retorna 'None'.
# Se tentássemos imprimir o resultado de 'h(lst)', o que veríamos seria:
print(h(lst))  # Isso vai imprimir 'None'.

# No entanto, a lista original 'lst' foi modificada pela função.
# Agora, o primeiro elemento de 'lst' foi alterado de 1 para 5.
# Portanto, ao imprimir a lista, o resultado será:
print(lst)  # Isso vai imprimir '[5, 2, 3]'.

""" 
DEFININDO NOVAS FUNÇÕES

▪ Escreva uma função chamada swapFS() que
▪ Tem como entrada uma lista 
▪ Troca o primeiro e o segundo elementos da lista, se a lista tiver ao menos dois elementos 
▪ A função não retorna nada 
"""

def swapFS(y):
    if len(y) >= 2:
        y[0], y[1] = y[1], y[0] # efetua o swap 
        return y
    return False
        
myY = ['one', 'two', 'three']
print(myY)
print(swapFS(myY))

def swapTwo(z):
    z[0], z[1] = z[1], z[0]
    return z
xz = ['1', '3', '5', '7']
print(xz)
print(swapTwo(xz))

i = 2
j = 4
print(i, j)

tmp = j
j = i
i = tmp
print(i, j)