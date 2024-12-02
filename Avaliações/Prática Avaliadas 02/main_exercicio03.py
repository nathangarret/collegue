# Exercício 3

# Implemente uma função chamada `divisores` que lê o arquivo `numeros.txt` e retorne um dicionário contendo pares `chave/valor` em que as chaves são os números disponíveis no arquivo lido e os valores são as listas dos divisores desses números.

# Caso o conteúdo do arquivo tenha como dados os números 10, 20, 25 e 12, a saída esperada é o dicionário {10: [1, 2, 5], 20: [1, 2, 4, 5, 10], 25: [1, 5], 12: [1, 2, 3, 4, 6]}

""" 
>>> divisores()
{10: [1, 2, 5], 20: [1, 2, 4, 5, 10], 25: [1, 5], 12: [1, 2, 3, 4, 6]} 
"""

import os

def divisores():
    caminho_pasta = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_pasta, 'numeros.txt')

    quantidade_divisores = {} # Chave e valor

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        numeros = [int(line.strip()) for line in arquivo.readlines()] # strip - remove quaisquer espaços em
        
    for numero in numeros:
        divisor = [i for i in range(1, numero) if numero % i == 0]
        quantidade_divisores[numero] = divisor

    return quantidade_divisores

resultado = divisores()
print(resultado)