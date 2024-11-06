""" ESCRITA EM ARQUIVOS TEXTO
1
2
3
4
Essa é a primeira linha. Essa é a primeira linha. Ainda a primeira linha…\n
2
3
4

1 Essa é a primeira linha. Ainda a primeira linha…\n
2 Agora na segunda linha.\n
1 Essa é a primeira linha. Ainda a primeira linha…\n
2 Agora na segunda linha.\n
3 Valores não strings como 5 precisam ser convertidos.\n

1 Essa é a primeira linha. Ainda a primeira linha…\n
2 Agora na segunda linha.\n
3 Valores não strings como 5 precisam ser convertidos.\n
4 Valores não strings como 5 precisam ser convertidos.\n
>>> outfile = open('test.txt', 'w')
>>> 
test.txt
>>> outfile.write('E')
>>> outfile.write('ssa é a primeira linha.')
>>>
>>> outfile = open('test.txt', 'w')
>>> outfile.write('E')
>>> outfile.write('ssa é a primeira linha.')
>>> outfile.write(' Ainda a primeira linha...\n')
>>>
>>> outfile = open('test.txt', 'w')
>>> outfile.write('E')
>>> outfile.write('ssa é a primeira linha.')
>>> outfile.write(' Ainda a primeira linha...\n')
>>> outfile.write('Agora na segunda linha.\n')
>>>
>>> outfile = open('test.txt', 'w')
>>> outfile.write('E')
>>> outfile.write('ssa é a primeira linha.')
>>> outfile.write(' Ainda a primeira linha...\n')
>>> outfile.write('Agora na segunda linha.\n')
>>> outfile.write('Valores não strings como '+str(5)+' precisam ser convertidos.\n')
>>>
>>> outfile = open('test.txt', 'w')
>>> outfile.write('E')
>>> outfile.write('ssa é a primeira linha.')
>>> outfile.write(' Ainda a primeira linha...\n')
>>> outfile.write('Agora na segunda linha.\n')
>>> outfile.write('Valores não strings como '+str(5)+' precisam ser convertidos.\n')
>>> outfile.write('Valores não strings como {} precisam ser convertidos.\n'.format(5))
>>> outfile.close() 

"""