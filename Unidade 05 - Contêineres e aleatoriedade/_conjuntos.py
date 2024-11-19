# Conjuntos 

# • A classe set implementa um objeto com as propriedades de um conjunto matemático
# • Coleção não ordenada de objetos
# • Todos os membros devem ser objetos imutáveis

agenda = {
    '123-45-67',
    '234-56-78',
    '345-67-89'
}

print(agenda)
print(type(agenda))

idades = [23, 19, 18, 21, 18, 20, 21, 23, 22, 23, 19, 20]
print(set(idades)) # Ordena os numeros, sem repetir

print(list(set(idades)))

# x in s Verdadeiro se x estiver no conjunto s; se não, False

# x not in s Falsesex estiver no conjunto s; se não, True

# len(s) Retorna o tamanho do conjunto s

# s == t True se os conjuntos s e t tiverem os mesmos elementos; se não, False

# s != t True se os conjuntos s e t não tiverem os mesmos elementos; caso contrário, False

# s <= t True se cada elemento do conjunto s estiver no conjunto t; se não, False
 
# s < t True se s <= t e s != t
 
# s | t Retorna a união dos conjuntos s e t

# s & t Retorna a interseção dos conjuntos s e t
 
# s - t Retorna a diferença entre os conjuntos s e t

# s ˆ t Retorna a diferença simétrica dos conjuntos set

agenda_dois = {
    '849-45-67',
    '123-56-78',
    '234-67-89'
}

print('123-56-78' in agenda_dois)
print(len(agenda_dois))

agenda_tres = {
    '626-45-89',
    '123-56-67',
    '874-67-78'
}

print(agenda_dois == agenda_tres)
print(agenda_dois != agenda_tres)
print(agenda_dois < agenda_tres)
print(agenda_dois | agenda_tres)
print(agenda_dois & agenda_tres)
print(agenda_dois - agenda_tres)
print(agenda_dois ^ agenda_tres)

# Metódo de set
# • add(): Adiciona novos elementos ao conjunto
# • remove(): Remove elementos do conjunto
# • clear(): Remove todos os elementos do conjunto

agenda_quatro = {
    '345-67-89',
    '456-78-90'
}

agenda_quatro.add('123-45-67')
print(agenda_quatro)

agenda_quatro.remove('123-45-67')
print(agenda_quatro)

agenda_quatro.clear()
print(agenda_quatro)