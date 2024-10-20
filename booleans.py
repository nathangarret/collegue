# Booleans - True or False

""" 
menor = 2 < 3
print(menor)

maior = 2 > 3
print(maior)

igual = 2 == 3
print(igual)

diferente = 2 != 3
print(diferente)

menorIgual = 2 <= 3
print(menorIgual)

maiorIgual = 2 >= 3
print(maiorIgual)

operadorAlgebrico = 2 + 4 == 2* (9 / 3)
print(operadorAlgebrico)
""" 

# Comumente que precisamos avaliar expressões que envolvem mais de um fato:
# - not, and, or

""" 
not:
A | not A
True | False
False | True
"""

print("not:")

booleanNot = not(3<4)
print(booleanNot)

booleanNotTrue = not(True)
print(booleanNotTrue)

booleanNotFalse = not(False)
print(booleanNotFalse)


"""
and:
A | B | A and B
True | True | True :)
True | False | False
False | True | False
False | False | False 
"""

print("\nand:")

booleanAnd = 2<3 and 3<4
print(booleanAnd)

booleanAndEqual = 4==5 and 3<4
print(booleanAndEqual)

booleanAndCompare = False and True
print(booleanAndCompare)

booleanAndCompare_2 = True and True
print(booleanAndCompare_2)


"""
or:
A | B | A or B
True | True | True :)
True | False | True :)
False | True | True :)
False | False | False 
"""

print("\nor:")

booleanOrEqual = 4==5 or 3<4
print(booleanOrEqual)

booleanOrCompare = False or True
print(booleanOrCompare)

booleanOrCompare_2 = False or False
print(booleanOrCompare_2)

booleanOrEqual_2 = 4+1 == 5 or 4-1 < 4
print(booleanOrEqual_2)

# Exercícios

print("\nExercícios: ")

first = 3 == 4-2
print(first)

second = 17//5 == 3
print(second)

third = (284 % 2) == 0 and (284 % 3) == 0 # Apenas o primeiro é verdadeiro, e segundo é False portando usando AND o output é: False
print(third)

fourth = (284 % 2) == 0 or (284 % 3) == 0 # Apenas o primeiro é verdadeiro, e segundo é False portando usando OR o output é: True
print(fourth)