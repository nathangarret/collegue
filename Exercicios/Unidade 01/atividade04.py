# O número de letras em 'Supercalifragilisticexpialidocious'.
strExample = "Supercalifragilisticexpialidocious"
print(len(strExample))

# 'Supercalifragilisticexpialidocious' contém 'ice' como uma substring?
print('ice' in strExample)
 
# Qual dos nomes a seguir vem primeiro na ordem alfabética: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'?
nomes = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
nomes.sort()

print(nomes)
 
# Qual dos nomes a seguir vem por último na ordem alfabética: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'?
nomes.sort(reverse=True)

print(nomes)