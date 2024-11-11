def pairSum(valores, x):
    for i in range(len(valores)):
        for j in range(i, len(valores)):
            if valores[i] + valores[j] == x:
                print(i, j)

pairSum([7, 8, 5, 3, 4, 6], 6)