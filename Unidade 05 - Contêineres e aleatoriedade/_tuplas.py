# Classe tuple

""" 
agenda = {
    ['Anna','Karenina']:'(123)456-78-90', 
    ['Yu', 'Tsun']:'(901)234-56-78', 
    ['Hans','Castorp']:'(321)908-76-54'
} 

print(error)
"""

# Semelhante a lista, mas é imutável
dias = ('Seg', 'Ter', 'Qua')
print(dias)

print(type(dias))

dias = 'Seg', 'Ter', 'Qua', 'Qui'
print(dias)

print(dias[2])

# Suponhamos que queiramos definir uma "caixa de contatos" com um dicionário
agenda = {
    ('Anna','Karenina'):'(123)456-78-90', 
    ('Yu', 'Tsun'):'(901)234-56-78', 
    ('Hans','Castorp'):'(321)908-76-54'
} 

print(agenda)

def lookup():
    agenda = {
        ('Anna', 'Karenina'): '(123)456-78-90',
        ('Yu', 'Tsun'): '(901)234-56-78',
        ('Hans', 'Castorp'): '(321)908-76-54'
    }

    print("Bem-vindo ao serviço de pesquisa da agenda telefônica!")
    print("Digite 'sair' como nome para encerrar o programa.")
    
    while True:
        # Solicitar o nome e sobrenome do usuário
        nome = input("Digite o nome: ").strip()
        if nome.lower() == 'sair':
            print("Encerrando o serviço de pesquisa. Até logo!")
            break
        sobrenome = input("Digite o sobrenome: ").strip()
        if sobrenome.lower() == 'sair':
            print("Encerrando o serviço de pesquisa. Até logo!")
            break

        # Buscar na agenda
        contato = (nome, sobrenome)
        if contato in agenda:
            print(f"O número de telefone de {nome} {sobrenome} é {agenda[contato]}.")
        else:
            print(f"Desculpe, o contato {nome} {sobrenome} não foi encontrado na agenda.")

lookup()