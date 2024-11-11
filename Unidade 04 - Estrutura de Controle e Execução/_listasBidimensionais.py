# Lista padrão - linhas [3, 5, 7, 9]

# Lista bidimensional - linhas e colunas - "tabelas"
""" 
    0, 1, 2, 3
0   3, 5, 7, 9 = [[3, 5, 7, 9] =
1   0, 2, 1, 6 = [0, 2, 1, 6] = 
2   3, 8, 3, 1 = [3, 8, 3, 1]] = 

"""


lst = [[3, 5, 7, 9],
       [0, 2, 1, 6],
       [3, 8, 3, 1]]

print(lst[0])
print(lst[1])
print(lst[2])

print(lst[0][0])
print(lst[2][3])

# Imprime os valores em uma lista 2D como uma tabela
def print_2d(x):
    for i in x:
        for j in i:
            print(j, end=' ')
        print()

print(print_2d())

# Incrementa cada elemento na lista 2D
def incr_2d(y):    
    # nrows = números de linhas em y
    # ncols = números de colunas em y
    nrows = len(y)
    ncols = len(y[0])

    for k in range(nrows):
        for l in range(ncols):
            y[k][l] += 1