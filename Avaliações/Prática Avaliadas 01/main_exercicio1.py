# Exercício 1

# Considere que a variável info contenha a seguinte lista: ['Curso', 'Python']
info = ['Curso', 'Python']

# Escreva comandos Python que:
# (a) Acrescenta a string ‘introdução' na lista armazenada em info
info.append('introdução')

# (b) Acrescenta a string 'de'
info.append('de')

# (c) Acrescenta a string 'a'
info.append('a')

# (d) Mude a ordem dos elementos na lista tal que a lista final seja ['Curso', 'de', 'introdução', 'a', 'Python']
print(info)

info = info[0], info[3], info[2], info[4], info[1]
print(info)