""" 
Escreve uma função enfatizar() que toma como entrada uma string s e retorna (não imprime) uma string com espaços inseridos entre letras adjacentes.

Como exemplo:
>>> enfatizar('Muito importante')
'M u i t o i m p o r t a n t e' 
"""
def enfatizar(s):
    return ' '.join(s)

resultado = enfatizar("Muito importante")
print(resultado)