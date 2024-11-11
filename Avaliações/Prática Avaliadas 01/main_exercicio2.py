# Exercício 2

# Escreva uma função chamada buscaContatos() que recebe como entradas uma lista, lst (que contém nomes), e uma string contendo uma letra, inicial, e imprime os elementos da lista (nomes) que começam com a letra inicial.

# Por exemplo:
# >>> buscaContatos(['Igraine', 'Arthur', 'Gorlois', 'Uther', 'Guenevere'], 'G')
# Gorlois
# Guenevere

def buscaContatos(lst, inicial):
    for nome in lst:
        if nome.startswith(inicial):
            print(nome)
        
buscaContatos(['Igraine', 'Arthur', 'Gorlois', 'Uther', 'Guenevere'], 'G')