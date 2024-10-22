# A soma de x, y e z.
numeros = [5, 8, 10]
soma = sum(numeros)
print(soma)

# A média dos valores de x, y e z.
media = soma / len(numeros)
print(f"{media:.2f}")

# Ache o maior valor dentre x, y e z.
maior_numero = max(numeros)
print(maior_numero)

# Ache a mediana entre x, y e z. Lembre-se de que a mediana é o "valor do meio". Você pode calcular isso usando as expressões dos outros itens. Para tanto, monte uma expressão que é a expressão do item a subtraído das expressões dos itens b e c.

mediana = soma - min(numeros) - max(numeros)
print(mediana)