""" 
Implemente uma função chamada postal(), cujo objetivo é preencher o endereço de uma carta que será enviada pelos correios. Para tanto, a sua função recebe 6 parâmetros de entrada:

O primeiro nome do destinatário (uma string)
O sobrenome do destinatário a last name (uma string)
O logradouro do destinatário com número (uma string)
A cidade do destinatário (uma string)
O estado do destinatário (uma string)
O CEP do destinatário (uma string)   
A sua função deve imprimir o endereço como no envelope em três linhas, seguindo o exemplo a seguir:
"""

def postal(primeiro_nome, sobrenome, logradouro, cidade, estado, CEP):
    print(f"{primeiro_nome} {sobrenome}")
    print(logradouro)
    print(f"{cidade}, {estado} {CEP}")

# Exemplo de uso
postal('Ljubomir', 'Perkovic', 'Avenida Paulista, 854', 'São Paulo', 'SP', '01310-100')