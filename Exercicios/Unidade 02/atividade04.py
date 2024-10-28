"""
Escreva um programa que permita ao usuário inserir dois números que correspondem às notas recebidas pelo aluno Bob nas duas avaliações de uma disciplina de programação.

Para o aluno ser aprovado na disciplina, ele precisa fazer pelo menos 7 pontos na primeira atividade e pelo menos 8 pontos na segunda atividade.

O seu programa deve imprimir a mensagem Candidato Aprovado. Parabéns! caso as condições acima sejam satisfeitas. Caso contrário, o programa deve imprimir a mensagem Candidato Reprovado. 
"""

nota_um =    float(input("Digite o valor da 1° atividade: "))
nota_dois =  float(input("Digite o valor da 2° atividade: "))

if nota_um >= 7 and nota_dois >= 8:
    print("Candidato Aprovado")
else:
    print("Candidato Reprovado")