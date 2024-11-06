def  buscaContatos(lst, inicial):
    for nome in lst:
        if nome.startswith(inicial):
            print(nome)

buscaContatos(['Igraine', 'Arthur', 'Gorlois', 'Uther', 'Guenevere'], 'G')