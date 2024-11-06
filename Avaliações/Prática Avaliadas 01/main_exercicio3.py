import os

def buscarLinhas(nomeArq, palavra):
    caminho_pasta = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_pasta, nomeArq)
    
    linhas_com_palavra = []
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arq:
        for linha in arq:
            if palavra in linha:
                linhas_com_palavra.append(linha)
                
                
    caminho_resultado = os.path.join(caminho_pasta, 'resultado.txt')
    with open(caminho_resultado, 'w', encoding='utf-8') as arq_resultado:
        for linha in linhas_com_palavra:
            arq_resultado.write(linha)
            
            
    print(f"{nomeArq}")
    for linha in linhas_com_palavra:
        print(linha.strip())
    
buscarLinhas('exemplo.txt', 'exemplo')