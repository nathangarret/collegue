""" 
Escreva um programa que permita ao usuário inserir três números que correspondem ás notas recebidas pelo aluno Bob nas três avaliações de uma disciplina de programação. O seu programa deve imprimir a nota final obtida pelo aluno, assumindo que a nota final é a média aritmética das três notas. Além disso, o programa deve informar se o aluno foi aprovado ou não na disciplina. Assuma que o aluno é aprovado se sua nota final foi maior ou igual a 7. Se o aluno for aprovado, o seu programa deve exibir a mensagem Aluno Aprovado; caso contrário, a mensagem Aluno Reprovado deve ser exibida.
"""

nota_um =    float(input("Digite o valor da 1° nota: "))
nota_dois =  float(input("Digite o valor da 2° nota: "))
nota_tres = float(input("Digite o valor da 3° nota: "))

mediaGeral = (nota_um + nota_dois + nota_tres) / 3 

if mediaGeral >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")