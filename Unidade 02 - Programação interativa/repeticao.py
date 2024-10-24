# Comando FOR

""" 
1. Peça ao usuário para digitar uma lista de produtos
2. Peça ao usuário para digitar a lista dos preços dos produtos dados
3. Peça ao usuário um valor máximo desejado
4. Liste o nome de todos os produtos cujo preço são menores do que 
o valor especificado pelo usuário

# 1. Pedir ao usuário para digitar uma lista de produtos
produtos = input("Digite os nomes dos produtos separados por vírgula: ").split(',')

# 2. Pedir ao usuário para digitar os preços correspondentes
precos = input("Digite os preços dos produtos na mesma ordem, separados por vírgula: ").split(',')

# Converter os preços para float
precos = [float(preco.strip()) for preco in precos]

# 3. Pedir ao usuário para informar o valor máximo desejado
valor_maximo = float(input("Digite o valor máximo desejado: "))

# 4. Exibir produtos com preço menor que o valor especificado
print("\nProdutos abaixo do valor máximo:")
for produto, preco in zip(produtos, precos):
    if preco < valor_maximo:
        print(f"{produto.strip()}: R$ {preco:.2f}")
"""
     
# ?   
# split   
# strip
# zip

# Laço for -> Executa um bloco de código para cada elemento de uma sequência
name = 'Apple'
for char in name:
    print(char)
        
# for <variable> in <sequence>:
#   <indented code block>
# <non-indented code block>

for word in ['stop', 'desktop', 'post', 'top']:
    if 'top' in word:
        print(word)
print('Done.')

print("\nFunção range")
# Função range(x, y, z)
for i in range(2, 16, 10):
    print(i)
    
# A função range() é usada para iterar sobre uma sequência de números em um intervalo especificado

# Para iterar sobre uma lista de n números 0, 1, 2, …, n-1
# for i in range(n):

# Para iterar sobre a lista de números i, i+1, i+2, …, n-1
# for i in range(i, n):

# Para iterar sobre a lista de n números i, i+c, i+2c, i+3c, …, n-1
# for i in range(i, n):

print("\nExercícios: ")
# ▪ Escreva laços for que imprimam as seguintes sequências
# ▪ 0, 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10
for i in range(0, 11):
    print(i)
    
# ▪ 1, 2, 3, 4, 5, 6, 7, 8, 9
for j in range(1, 10):
    print(j)

# ▪ 0, 2, 4, 6, 8
for k in range(0, 10, 2):
    print(k)

# ▪ 1, 3, 5, 7, 9
for l in range(1, 10, 2):
    print(l)

# ▪ 20, 30, 40, 50, 60
for m in range(20, 70, 10):
    print(m)