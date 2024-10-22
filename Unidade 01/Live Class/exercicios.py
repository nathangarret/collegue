# 1)
# A soma dos números negativos de -7 a -1
lst = [-7, -6, -5, -4, -3, -2, -1]
print(sum(lst))

# usando range
nmrs_negativos = sum(range(-7, 0))
print(nmrs_negativos)

# for + range
nmr_negativos = 0
for numero in range(-7, 0):
    nmr_negativos += numero
    
print(nmr_negativos)

# 2) A idade média de grupo: 17 9y - 24 10y - 21 11y - 27 12y
qntdIdade = (17 * 9 + 24 * 10 + 21 * 11 + 27 * 12)
qntPessoas = (17 + 24 + 21 + 27)
print(f"{qntdIdade / qntPessoas:.2f}")

# 3) 2 elevado a potência -20
print(f"{2**(-20):.2f}")

# 4) 61 cabe quantas vezes em 4356
print(f"{4356 // 61:.2f}") # divisao inteira, por isso utilzando //

# 5) 4356 cabe quantas vezes em 61
print(f"{4356 % 61:.2f}")

print("\n# Usando str")
# Usando str
# '-+'
s1 = '-'
s2 = '+'
print(s1 + s2)
print(s1 + s2 + s1)
print(s2 + s1*3)
print(s2 + s1*2 + s2 + s1*2)

print("\n# Expressoes booleanas")
s = 'goodbye'
print(s[0])
print(len(s))
print(s[-7])

# Verificar o primeiro caracter da String é g
print(s[0] == 'g')
print(s[0:8]) # Retorna go | Intervalo 0 1

# Intervalo de índices "0:x"
print(s[0:2] == 'ga')

# Penúltimo caracter
print(s[-2])

# Se o primeiro e último caracter sao iguais
print(s[-7] == s[-1])

# Listas
print("\n# Listas")

respostas = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N']

# (a) Atribua à variável numYes o número de ocorrências de ‘Y’ na lista respostas
numYes = respostas.count('Y')
print(numYes)

# (b) Atribua à variável numNos o número de ocorrências de ‘N’ na lista respostas
numNos = respostas.count('N')

# (c) Atribua à variável percentYes o percentual de strings ‘Y’ na lista resposta 
percentYes = numYes / len(respostas)
print(f"{percentYes:.2f}")

# (d) Ordene a lista resposta
respostas.sort()
print(respostas)

respostas.sort(reverse=True) # Faz em ordem inversa
# (e) Atribua à variável ind o índice da primeira ocorrência de ‘Y’ na lista resposta ordenada

# (f) Atribua à variável ind o índice da próxima ocorrência de ‘Y’ na lista resposta ordenada