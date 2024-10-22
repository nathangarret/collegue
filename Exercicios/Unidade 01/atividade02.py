""" 
Especificação
Escreva expressões python que computem:

1
O produto de 1111111 com ele mesmo.

2
Quantos livros de 81 mm de largura cabem em uma prateleira de 1.000 mm de largura?

3
Quantos centímetros sobrariam se colocássemos o número máximo possível de livros na prateleira do item anterior (ou seja, qual é o resto da divisão de 1.000 por 81)?

4
Em três atividades realizadas, você obteve notas 90/100, 95/100 e 87/100. Qual é a sua nota média nesses três exames?

5
Você obteve notas 90/100, 46/50, 55/60 e 66/70: Qual é a sua melhor nota nesses quatro exames?

6
Você obteve notas 90/100, 46/50, 55/60 e 66/70: Qual é a nota mais baixa?

7
A soma dos números de 1 a 10.

8
O produto dos números de 1 a 10.

9
Um Kb (kilobyte) é realmente 1.024 bytes, em que 1.024 é 2 elevado à potência 10: quantos bytes há em um gigabyte (2 elevado à potência 30)?

"""

# 1
print(1111111**2)

# 2
print(f"{1000 / 81:.2f}")

# 3
mm_sobra = 1000 % 81
cm_sobra = mm_sobra / 10 # Divisao de mm para cm
print(f"{cm_sobra:.2f}")

# 4 Em três atividades realizadas, você obteve notas 90/100, 95/100 e 87/100. 
# Qual é a sua nota média nesses três exames?
somaNotas = (90 + 95 + 87) / 3
print(f"{somaNotas:.2f}")

# 5 Você obteve notas 90/100, 46/50, 55/60 e 66/70: 
# Qual é a sua melhor nota nesses quatro exames?
notas_exame = [90 / 100, 46 / 50, 55 / 60, 66 / 70]
melhor_nota = max(notas_exame)
porcentagem = melhor_nota * 100

print(f"{porcentagem:.2f}%")

# Você obteve notas 90/100, 46/50, 55/60 e 66/70: Qual é a nota mais baixa?
notas_exame2 = [90 / 100, 46 / 50, 55 / 60, 66 / 70]
menor_nota = min(notas_exame2)
porcentagem2 = menor_nota * 100

print(f"{porcentagem2:.2f}%") # ? 90%

# A soma dos números de 1 a 10.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lst)) # 55

print(sum(range(1, 11))) # 55

numeroInicial = 0
for i in range(1, 11):
    numeroInicial += i
    
print(numeroInicial) # 55

# O produto dos números de 1 a 10.
numeroInicial2 = 1
for n in range(1, 11):
    numeroInicial2 *= n
    
print(numeroInicial2)

# Um Kb (kilobyte) é realmente 1.024 bytes, pois 1.024 é 2 elevado à potência 10.
# Da mesma forma, um gigabyte (GB) é 2 elevado à potência 30, o que dá o número exato de bytes.

# Calculando o número de bytes em um gigabyte (2**30):
gigabyte = 2 ** 30  # 1 GB = 1.073.741.824 bytes

# Exibindo o resultado
print(gigabyte)  # Saída: 1073741824