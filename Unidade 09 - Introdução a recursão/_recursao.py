# Conceitos Introduzidos:
# Definição de Recursão: Recursão é um conceito onde uma função chama a si mesma para resolver subproblemas de um problema maior. É composta por dois elementos principais:

# Caso Base: Define uma condição para que a recursão termine.
# Passo Recursivo: A função chama a si mesma com argumentos menores ou simplificados.

def countdown(n):
    if n <= 0:
        print("Fim!!!")
    else:
        print(n)
        countdown(n - 1)

# Explicação: A função countdown imprime números de n até 0. O caso base ocorre quando n <= 0. Se n > 0, o passo recursivo reduz n a cada chamada.
# Problema de Pilha de Programa: Se não houver um caso base, a recursão continuará indefinidamente, causando um erro de "pilha estourada".

def vertical(n):
    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        print(n % 10)

vertical(3214)