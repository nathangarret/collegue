# Saída formatada

prod = 'morels'
cost = 139
wght = 1/2
total = cost * wght
print(prod, cost, wght, total)

print(prod, cost, wght, total, sep='; ')
print(prod, cost, wght, total, sep=':::')

pets = ['boa', 'cat', 'dog']
for i in pets:
    print(i, end=':::')
    
# Metódo format()
hour = 11
minute = 45
second = 33
print('\nHour: {}:{}:{}'.format(hour, minute, second))

for j in range(1, 8):
    print(j, j**2, 2**j)
    
for k in range(1, 8):
    print('w/ format: {} {:2} {:3}'.format(k, k**2, 2**k))
    
# Podemos especificar a tipo de saída

""" 
b binário
c caractere
d decimal
X hexadecimal
e notação científica
f ponto-fixo
"""

n = 10
print('{:b}'.format(n))
print('{:c}'.format(n))
print('{:d}'.format(n))
print('{:X}'.format(n))
print('{:e}'.format(n))
print('{:7.2f}'.format(n))