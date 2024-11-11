# Aninhando um laço dentro do outro
def nested(n):
    for j in range(n): # 11111 - 22222 - 33333 - 44444 - 01234
        for i in range(n): # 01234 - 01234 - 01234 - 01234 - 01234
            print(i, end='')
        print()

nested(5)

print("\n for dentro do for: ")

# Quando j = 0 deve imprimir 0
# Assim por diante j = 1 deve imprimir 0 1
# j = 2 deve imprimir 0 1 2
def nested_two(m):
    for j in range(m):
        for i in range(j + 1):
            print(i, end='')
        print()

nested_two(5)