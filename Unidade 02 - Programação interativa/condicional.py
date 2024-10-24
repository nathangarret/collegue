# Comado if
"""
COMANDO IF: DECISÃO DE CAMINHO ÚNICO
if <condition>:
    <indented code block>
<non-indented statement>

if temp > 86:
    print('It is hot!')
    print('Drink liquids.')
print('Goodbye.')
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Vocẽ pode tirar a carteira de motorista!")
else:
    print("Infelizmente, você ainda não pode tirar a carteira de motorista!")