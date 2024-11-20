# Execeções e fluxo de controle excepcional

# Tipos de erros:
# • Erros de sintaxe
# • Erros de estado errôneo

""" 

>>> excuse = 'I'm sick'
SyntaxError: invalid syntax

>>> print(hour+':'+minute+':'+second)
Traceback (most recent call last):
File "<pyshell#113>", line 1, in <module>
print(hour+':'+minute+':'+second)
TypeError: unsupported operand type(s) for +: 'int' and 'str’

>>> infile = open('sample.txt')
Traceback (most recent call last):
File "<pyshell#50>", line 1, in <module>
infile = open('sample.txt')
IOError: [Errno 2] No such file or directory: 'sample.txt’ 

"""

# • Eles ocorrem durante o processo de tradução destes comandos para linguagens de máquina e antes de serem executados

""" 

>>> (3+4] 
SyntaxError: invalid syntax

>>> if x == 5 
SyntaxError: invalid syntax 

>>> print 'hello' 
SyntaxError: invalid syntax 

>>> lst = [4;5;6] 
SyntaxError: invalid syntax 

>>> for i in range(10): 
print(i) 
SyntaxError: expected an indented block 

"""

# A Execução do Programa entra em um Estado Errôneo
# Quando um erro ocorre, um objeto do tipo "erro" é criado
# • Esse objeto tem um tipo relacionadocom o tipo de erro
# • O objeto contém informação sobre o erro O comportamento padrão é imprimir esta informação e interromper a execução do comando

# Tipos de excessão:
# • KeyboardInterrupt Levantado quando o usuário pressiona Ctrl-C, a tecla de interrupção
# • OverflowError Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande
# • ZeroDivisionError Levantado quando se tenta dividir por 0
# • IOError Levantado quando uma operação de entra/saída falha por um motivo relacionado com E/S
# • IndexError Levantado quando um índice sequencial está fora do intervalo de índices válidos
# • NameError Levantado quando se tenta avaliar um identificador não atribuído (nome)
# • TypeError Levantado quando uma operação da função é aplicada a um objeto do tipo errado
# • ValueError Levantado quando a operação ou função tem um argumento com tipo correto, mas com valor incorreto

def h(n):
    print('Start h')
    print(1/n)
    print(n)

def g(n):
    print('Start g')
    h(n-1)
    print(n)
 
def f(n):
    print('Start f')
    g(n-1)
    print(n)

f(2)

# Comportamento padrão: interromper a execução e imprimir a informação de erro contida no objeto exceção