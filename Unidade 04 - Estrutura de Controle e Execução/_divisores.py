# Divisores de um número

def divisors(n):
    divisores = []

    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    return divisores

print(divisors(1))
print(divisors(22))
print(divisors(44))
print(divisors(71))