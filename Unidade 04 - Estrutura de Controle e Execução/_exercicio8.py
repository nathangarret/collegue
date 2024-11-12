""" 
Escreva uma função innerProduct() que toma como entrada duas listas (do mesmo comprimento) de números e, então, calcula e retorna o produto interno das duas listas. O produto interno de duas listas x = [x1, x2, ..., xn] e y = [y1, y2, ..., yn] é o valo 

x1 * y1 + x2 * y2 + ... + xn * yn
Como exemplo de execução:

>>> innerProduct([2,3,4], [1,0,2])
10
"""

def innerProduct(x, y):

    resultado = 0

    for i in range(len(x)):
        resultado += x[i] * y[i]
    return resultado

print(innerProduct([2,3,4], [1,0,2])) 

# 2 * 1 = 2+
# 3 * 0 = 0+
# 4 * 2 = 8+
#       = 10