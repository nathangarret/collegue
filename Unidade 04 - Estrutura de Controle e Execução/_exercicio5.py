""" 
Escreva uma função cripto() que toma como entrada uma string s e retorna uma string criptografada, onde a criptografia procede da seguinte forma:

divida o texto em blocos de duas letras cada
troque cada par de letras
Como exemplos:

>>> crypto('Secret Message')
'eSrcteM seaseg'
>>> crypto('Secret Messages')
'eSrcteM seasegs'
Orientações adicionais
Realize as saídas como acima. Note que espaços, pontuação, etc. são tratados como letras e devem ser trocados de ordem no processo, como nos exemplos acima. 
"""

def cripto(s):

    criptograda = ""

    # Divididno a string em blocos de 2 caracteres e trocando os pares
    for i in range(0, len(s), 2): # s[0:2]
        # Houver o par completo troque as letras
        if i + 1 < len(s): 
            criptograda += s[i + 1] + s[i]
        else:
            criptograda += s[i]
    return criptograda

print(cripto('Secret Message'))   # 'eSrcteM seaseg'
print(cripto('Secret Messages'))  # 'eSrcteM seasegs'