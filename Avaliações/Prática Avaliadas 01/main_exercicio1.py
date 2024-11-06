# Exercicío 1

info = ['Curso', 'Python']

# a)
info.append('introdução')

# b)
info.append('de')

# c)
info.append('a')

print(info) # ['Curso', 'Python', 'introdução', 'de', 'a']

# d)
info = info[0], info[3], info[2], info[4], info[1]
print(info)