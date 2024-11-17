# O módulo random

# Algumas aplicações precisão de números gerados aleatoriamente:
# • Computação Científica
# • Simulações Financeiras
# • Criptografia
# • Jogos de Computadores
 
# Números verdadeiramente aleatórios são difíceis de serem gerados

# Comumente, números pseudo-aleatórios são usados
# • Parecem ser aleatórios
# • São gerados com um processo determinístico
# O módulo random da biblioteca padrão de Python provê geradores de números pseudo-aleatórios além de outras funções de amostragem

import random

print(random.randrange(1, 10))
print(random.uniform(0, 1))

# Funções shuffle(), choice(), sample

names = ['Ann', 'Bob', 'Cal', 'Dee', 'Eve', 'Flo', 'Hal', 'Ike']
import random

random.shuffle(names)
print(names)

print(random.choice(names))
print(random.choice(names))
print(random.choice(names)) # Choose a random element from a non-empty sequence.
print(random.choice(names))
print(random.sample(names, 3))
print(random.sample(names, 3))
print(random.sample(names, 3)) # Chooses k unique random elements from a population sequence

import random

def aproxPi(n):
    inside_circle = 0
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / n

# Testando a função com os exemplos fornecidos
results = {
    1000: aproxPi(1000),
    100000: aproxPi(100000),
    1000000: aproxPi(1000000)
}

print(results)