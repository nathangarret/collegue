# Exercício 3
# Escreva uma função chamada buscarLinhas(), que recebe como parâmetros: o nome do arquivo de entrada (nomeArq) e uma palavra a ser buscada (palavra).
# 
# Sua função deve escrever um arquivo chamado resultado.txt que contém as linhas do arquivo original que contêm a palavra, como no exemplo a seguir:
# >>> buscarLinhas('exemplo.txt', 'exemplo')
 
# exemplo.txt
# Um exemplo de arquivo de
# Para o exercício de exemplo
# Vamos ver a resposta certa

# resultado.txt
# Um exemplo de arquivo de
# Para o exercício de exemplo

import os

def buscarLinhas(nomeArq, palavra):
    caminho_pasta = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_pasta, nomeArq)

    linhas_com_palavras = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arq:
        for linha in arq:
            if palavra in linha:
                linhas_com_palavras.append(linha)
    
    caminho_resultado = os.path.join(caminho_pasta, 'resultado.txt')
    with open(caminho_resultado, 'w', encoding='utf-8') as arq_resultado:
        for linha in linhas_com_palavras:
            arq_resultado.write(linha)

    print(f'{nomeArq}')
    for linha in linhas_com_palavras:
        print(linha.strip()) # Remove os espaços em brancos ao redor das linhas

buscarLinhas('exemplo.txt', 'exemplo')