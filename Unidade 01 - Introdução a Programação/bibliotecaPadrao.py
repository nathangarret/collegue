import math

# Raiz quadrada
print(math.sqrt(144))

# Cosseno
print(math.cos(0))

# Logaritmo
print(math.log(8))
print(math.log(8, 2))

# Pi
print(math.pi)

# Exercícios
print("\nExercícios: ")

# Comprimento da hipotenusa de um triângulo retângulo com catetos 3 e 4
c = math.sqrt(3**2 + 4**2)
print(c) # 5.0

print(c > 5) # False

# Á área de um círculo de raio 10
print(f"{math.pi * 10 * 10:.3f}")

"""
O valor de uma expresão booleana que checa se o ponto de coordenadas (5, 5) está dentro do círculo
de centro (0, 0) e raio 7

1. Distância entre as coordenada (5, 5) para (0, 0) é menor ou igual que a 7
    
"""
print(f"{math.sqrt(5*5 + 5*5) <= 7}")