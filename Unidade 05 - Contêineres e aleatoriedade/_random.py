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

# Funções shuffle(), choice(), sample()
names = ['Ann', 'Bob', 'Cal', 'Dee', 'Eve', 'Flo', 'Hal', 'Ike']
random.shuffle(names) # Method takes a sequence, like a list, and reorganize the order of the items
print(names)

print(random.choice(names)) # Choose a random element from a non-empty sequence.
print(random.choice(names))
print(random.choice(names)) 
print(random.choice(names))
print(random.sample(names, 3)) # Chooses k unique random elements from a population sequence
print(random.sample(names, 3))
print(random.sample(names, 3))

def aproxPi(n): # (n) pontos aleatórios que serão gerados
    inside_circle = 0 # Armazenar a contagem de pontos dentro do círculo
    for _ in range(n): # _ usado com uma variável descartável por que não é usada dentro do loop
        x, y = random.uniform(-1, 1), random.uniform(-1, 1) # Gera duas coordenadas aleatórias x e y entre -1 e 1. O random.uniform(-1, 1) retorna um ponto flutante aleatório entre -1 e 1
        if x**2 + y**2 <= 1: # Verifica se o ponto está dentro do círculo 
            inside_circle += 1 # incrementa o contador
    return 4 * inside_circle / n # A função retorna o valor aproximado de π.

# Testando a função com os exemplos fornecidos
results = {
    1000: aproxPi(1000),
    100000: aproxPi(100000),
    1000000: aproxPi(1000000)
}

print(results)