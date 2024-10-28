""" 
Escreva um programa que permita ao usuário inserir uma lista de nomes. O seu programa deve imprimir os nomes na lista que não representam nomes compostos (ou seja, nomes que contenham espaços ou hífen).
"""

lista = eval(input('Digite a lista de nomes:'))
#Inclua sua solução abaixo

for nome in lista:
  if ' ' not in nome and '-' not in nome:
    print(nome)