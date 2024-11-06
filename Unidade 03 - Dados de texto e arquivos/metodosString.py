# Operadores em String
n = "cleiton"

print(len(n))
print(n[:3])
print(n[0])
print(n[-7])
print(n[-4:-1]) # 3 caracteres -> ito

print(n.capitalize()) # capitalize -> retorna a string com a primeira letra em maiúsculo

print(n.count("o")) # 1 # count -> conta o número de ocorrẽncias

print(n.find("n"))# find -> retorna o índice da primeira ocorrência de target em n
print(n[6])

print(n.upper()) # upper - deixa a string em letra maiúscula
print(n.lower()) # lower - deixa a string em letra minúscula

old = "ei" # O que eu quero q modifique
new = "cl" # O que vai modificar
print(n.replace(old, new))

x = 'http://www.linkedin.com/in/nathangarrett'
print(x.split('/')) # ['http:', '', 'www.linkedin.com', 'in', 'nathangarrett']

print(n.strip()) # Retorna n sem espaços no começo e no final

# Strings são imutáveis - Cópias são feitas das strings

""" event = "Tuesday, Feb 29, 2012 -- 3:35 PM"
table = str.maketrans(':,-', 3*' ')
event.translate(table) """

events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
print(events)
""" 9/13 2:30 PM
9/14 11:15 AM
9/14 1:00 PM
9/15 9:00 AM """

resposta_A = events.count("9/14")
print(f"a) {resposta_A}")

resposta_B = events.find("9/14")
print(f"b) {resposta_B}")

resposta_C = events.find("9/15") - 1
print(f"c) {resposta_C}")

# D)
print(f"d) ", events[resposta_B:resposta_C].split('\n'))
