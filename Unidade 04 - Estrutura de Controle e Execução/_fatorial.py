# Como calcular um fatorial de um número

def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(fatorial(1))
print(fatorial(3))
print(fatorial(5))
print(fatorial(7))