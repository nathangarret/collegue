# Entrada e saída
# input -> A função input() lê uma entrada dada pelo usuário no terminal - Entrada
# ->
# print -> A função print() mostra (imprime) o seu argumento no terminal de saída - Saída

# resposta1 = input("Qual o seu nome: ")

# Nesse caso a váriavel resposta1 está recebendo a saida do input - No caso será o nome da pessoa

# print("Seu nome é: ", resposta1)

# Função eval - Recebe uma string e avalia como uma expressão python
# E se precisarmos de um número na saída do input?
# R: Existem duas opções, podemos usar a conversão de tipos, ou a função eval()

"""
# Exercícios
nome = input("Qual o seu nome: ")
idade = int(input("Digite sua idade: "))
# Transformando o input str em int

print(type(idade))

idade5anos = idade + 5
print(nome, f", sua idade será {idade5anos} daqui a 5 anos!")
"""

# Exercício
base = float(input("Digite o valor da base: "))
altura = float(input("Digite a altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print("Área = ", area)
print(type(area))

print("Perímetro = ", perimetro)
print(type(perimetro))