# Leitura de números válidos

def lerNumeroValido(a, b):
    while True:
        valor = int(input('Digite um valor (inteiro): '))
        if a <= valor <= b:
            return valor

print(lerNumeroValido(1, 10))