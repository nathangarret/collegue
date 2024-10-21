""" 
Especificação
Escreva expressões python que computem:

O produto de 1111111 com ele mesmo.

Quantos livros de 81 mm de largura cabem em uma prateleira de 1.000 mm de largura?

Quantos centímetros sobrariam se colocássemos o número máximo possível de livros na prateleira do item anterior (ou seja, qual é o resto da divisão de 1.000 por 81)?

Em três atividades realizadas, você obteve notas 90/100, 95/100 e 87/100. Qual é a sua nota média nesses três exames?

Você obteve notas 90/100, 46/50, 55/60 e 66/70: Qual é a sua melhor nota nesses quatro exames?

Você obteve notas 90/100, 46/50, 55/60 e 66/70: Qual é a nota mais baixa?

A soma dos números de 1 a 10.

O produto dos números de 1 a 10.

Um Kb (kilobyte) é realmente 1.024 bytes, em que 1.024 é 2 elevado à potência 10: quantos bytes há em um gigabyte (2 elevado à potência 30)?

"""

print(1111111**2)

print(f"{1000 / 81:.2f}")

mm_sobra = 1000 % 81
cm_sobra = mm_sobra / 10 # Divisao de mm para cm
print(f"{cm_sobra:.2f}")