# Exercício 3

# Implemente uma função chamada `divisores` que lê o arquivo `numeros.txt` e retorne um dicionário contendo pares `chave/valor` em que as chaves são os números disponíveis no arquivo lido e os valores são as listas dos divisores desses números.

# Caso o conteúdo do arquivo tenha como dados os números 10, 20, 25 e 12, a saída esperada é o dicionário {10: [1, 2, 5], 20: [1, 2, 4, 5, 10], 25: [1, 5], 12: [1, 2, 3, 4, 6]}

""" 
>>> divisores()
{10: [1, 2, 5], 20: [1, 2, 4, 5, 10], 25: [1, 5], 12: [1, 2, 3, 4, 6]} 
"""

import os as s

def divisors():
    in_folder = s.path.dirname(s.path.abspath(__file__))
    in_file = s.path.join(in_folder, 'numeros.txt')

    dic_divisors = {}

    with open(in_file, 'r', encoding='utf-8') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    for number in numbers:
        divisors = [i for i in range(1, number) if number % i == 0]
        dic_divisors[number] = divisors

    return dic_divisors

resultado = divisors()
print(resultado)