""" 
Suponha que você já tenha uma lista definida, chamada dados, contendo três strings: o primeiro nome, o nome do meio e o sobrenome de uma pessoa, nessa ordem. Escreva uma expressão que produza uma string que consiste no sobrenome da pessoa seguido de uma vírgula e espaço, depois o primeiro nome e um espaço, depois a inicial do meio da pessoa seguida de um ponto. Assim, por exemplo, se a lista dados for igual a ['Pedro', 'Álvares', 'Cabral'], sua expressão produzirá a string 'Cabral, Pedro Á.'
"""

dados = ['Nathan', 'Vasconcelos', 'Garrett']
nomeFormatado = f"{dados[2]}, {dados[0]} {dados[1][0]}"
# {dados[1][0]}: Acessa o elemento no índice 1 (nome do meio), então pega o caractere no índice 0 desse elemento (a primeira letra) e a insere.
# Saída: V

print(nomeFormatado)