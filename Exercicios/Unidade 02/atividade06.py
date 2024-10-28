""" 
Você irá escrever uma função (chamada hurricane) cuja função é controlar a entrada na nova atração (chamada Hurricane) de um parque de diversões. Para ser permitido que entre na atração, o visitante deve ter altura mínima de 135 centímetros. Escreva uma função que recebe como argumento a altura do visitante em centímetros e:

Caso o valor passado seja maior ou igual a 135 centímetros:
Imprime a mensagem Visitante permitido no Hurricane!
Retorna o valor booleano True

Caso contrário:
Imprime a mensagem Infelizmente, o visitante não pode entrar no Hurricane
Retorna o valor booleano False
"""


def hurricane(altura):
    if altura >= 135:
        return "Visitante permitido no Hurricane!", True
    else:
        return "Infelizmente, o visitante não pode entrar no Hurricane", False
    
print(hurricane(180))
print(hurricane(130))