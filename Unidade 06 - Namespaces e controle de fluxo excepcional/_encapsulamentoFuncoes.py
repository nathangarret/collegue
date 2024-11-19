# Encapsulamento em funções e a pilha de programa

# O próposito do uso de funções;
# Modularidade: Para lidar com a complexidade de desenvolver programas grandes, usualmente "quebrando" ele em pedaços menores, mais simples e autocontidos
# Reuso do Código: Um fragmento de código que é usada muitas vezes em um programa deve ser encapsulada. Isso torna o código mais curto, simples, claro e também mais fácil de ser depurado e mantido
# Encapsulamento: Uma função esconde detalhes de sua implementação, o que torna o trabalho do desenvolvedor mais fácil

# Encapsulamento via varáveis locais:
def double(y):
    x = 2

    print('x = {}, y = {}'.format(x, y))
    return x * y

print(double(2))
# Toda chamada de função tem um namespace no qual as variáveis locais são guardadas

print("\nNamespaces de Funções")
# Namespaces de Funções
# Cada função possui seu próprio namespace (espaço de nomes).
# As variáveis definidas em uma função não afetam as de fora, mesmo que tenham o mesmo nome.
x, y = 20, 50

def double(y):
    x = 2
    print('x = {}, y = {}'.format(x, y))
    return x * y

res = double(5)  # x = 2, y = 5
print(x, y)      # x = 20, y = 50


print("\nPilha de programa")
# Pilha de programa
# O OS dedica um espaço de memória para a pilha de programa, cuja função é lembrar os valores definidos

def h(n):
    print('Start h')
    print(1 / n)
    print(n)

def g(n):
    print('Start g')
    h(n - 1)
    print(n)

def f(n):
    print('Start f')
    g(n - 1)
    print(n)

f(4)