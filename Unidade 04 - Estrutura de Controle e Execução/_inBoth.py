def inBoth(lista_um, lista_dois):
    for i in range(len(lista_um)):
        for j in range(len(lista_dois)):
            if lista_um[i] == lista_dois[j]:
                print([i, j])
                return True
    return False

print(inBoth([3, 2, 5, 4, 7], [9, 0, 1, 3]))
print(inBoth([2, 5, 4, 7], [9, 0, 1, 3]))