x = "Olá, mundo! :)\n"
print(x)

# print("Olá, mundo! :)"

"""

Usage | Explanation
x in a | Verdadeiro se x é substring de a
x not in a | Verdadeiro se x não é substring de a
s + t | Concatenação de s t
s * n, n * s | Concatenação de n cópias de s = n representa uma quantidade de números
s[i] | Caractere no índice de s
len(s) | (função) Comprimento de string s

"""

s = 'rock'
usageIn = 'o' in s
print(usageIn)

t = 'climbing'
usageIn_2 = 'o' in t
print(usageIn_2)

usageNotIn = 'bi' not in t
print(usageNotIn)

rockClimbing = s + t
print(rockClimbing)

rockClimbing_2 = s + " " + t
print(rockClimbing_2)

rockRockRock = 5 * s
print(rockRockRock)

underscore_ = 30 * '_|/'
print(underscore_)

print(len(t))

# Indexação de Strings
print("\nIndexação de Strings")

s = "Apple"
print(s[0])

print(len(s))

print(s[-5]) # número negativo = começa pelo último caracter == s[-5] seria A
print(s[0]) # número positivo = começa pelo primeiro caracter == s[0] seria A

# Alphabet - usando len - localizando dentro de indexações

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))

print(alphabet[-26]) # como começa do -1 -> -26 corresponde a posição 25 do positivo
print(alphabet[0])

print(alphabet[-24])
print(alphabet[2])

print(alphabet[-1])
print(alphabet[25])

print(alphabet[-2])
print(alphabet[24])

print(alphabet[-10])
print(alphabet[16])