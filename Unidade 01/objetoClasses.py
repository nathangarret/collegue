# Classes e Objetos

# Todo valor em Py é armazenado na memória como um objeto
# Todo objeto tem um "valor" e um "tipo"
 
a = 3
print(type(a))

b = 3.0
print(type(b))

c = "three"
print(type(c))

d = [1, 2, 3]
print(type(d))

# O objeto tem um tipo, a variável não!
# Terminologia: objeto X é do tipo int = objeto X pertence a classe int
# O tipo do objeto determina que valores ele pode assumir e comi ele pode ser manipulado

print(2** 1024)

# abs(3.14) -> abs é utilizado para determinar um número absoluto

print("\nConstrutores de Objeto")
# Construtores de Objeto
x = 3 # implícita
print(x)

# explícita -> função construtora do tipo
y = int()
print(y)

z = float()
print(z)

i = str()
print(i)

lstObj = list()
print(lstObj)

print("\nConversão de Tipos: ")
# Conversão de Tipos
# Implicito
intToFloatImp = 2 + 3.0
print(intToFloatImp)

booleanToBinaryImp = False + 0
print(booleanToBinaryImp)

# Explicito
intToFloatExp = int(2.1)
print(intToFloatExp)

strToIntExp = int('456')
print(strToIntExp)

strTofloatExp = float('4.6')
print(strTofloatExp)

floatToIntExp = float(2**24)
print(f"{floatToIntExp:.2f}")

# Métodos
print("\nMétodos")

# Notação Geral: O.M(x,y) -> Objeto.Metodo(Parâmetros)
print("O.M(x,y) -> Objeto.Metodo(Parâmetros)")