lst = [9, 7, 7, 10, 3, 8, 6, 6, 2]

# Contar ocorrências do número 7
print(lst.count(7)) 

# Alterar o último valor da lista para 4
print(len(lst))
print(lst[-1])

lst[-1] = 4
print(lst) 

# Mostrar a nota mais alta
print(max(lst))

# Ordenar as notas da lista
lst.sort() # Altera a lista par auma ordem crescente
print(lst)

# Avalia a média das notas da lista
mediaGeral = sum(lst) / len(lst)
print(f"{mediaGeral:.2f}")