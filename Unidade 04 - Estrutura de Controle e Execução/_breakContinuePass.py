# Break - intorrompe a execução - usado no corpo de um laço - quando executado, interrompe o laço atual - 
def cities_two():
    lista = []

    while True:
        city = input("Enter city: ")

        if city == "":
            break # para a execução

        lista.append(city)
    
    return lista

print(cities_two())

s = "python e legal"
for letter in s:
    if letter == 'e' or letter == 'o':
        break
    print(letter, end='') # pyth

print()

def before_zero(table):
    for row in table:
        for num in row:
            if num == 0:
                break
            print(num, end='')
        print()

print(before_zero([[2, 3, 0, 6], # 23
                   [0, 3, 4, 5], # None
                   [4, 5, 6, 0] # 456
]))

# Continue - Volta o laço ao começo - No sentido de continuar a iteração
t = "python e legal"

for letter in t:
    if letter == "e" or letter == "o":
        continue # pythn  lgal
    print(letter, end='')

print()

def ignore_zero(table):
    for row in table:
        for num in row:
            if num == 0:
                continue
            print(num, end='')
        print()

print(ignore_zero([
    [2, 3, 0, 6], # 236
    [0, 3, 4, 5], # 345
    [4, 5, 6, 0]  # 456
]))

# Pass - Apenas não faz nada - usado para substituir um corpo
n = 12

if n % 2 == 0:
    pass # Se for par retornará None
else:
    print(n) # Exibe apenas o número n ímpar