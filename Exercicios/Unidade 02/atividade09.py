""" 
Escreva uma função chamada intersect(), que recebe duas listas como parâmetro. A função deve retornar uma lista contendo todos os items que estão em ambas as listas. A lista resultante deve estar ordenada.
"""

def intersect(list1, list2):
    # Inicializa uma lista vazia para os elementos em comum
    result = []
    
    # Usando um conjunto para evitar duplicatas
    set_list2 = set(list2) # are used to store multiple items in a single variable
    
    # Itera sobre a primeira lista
    for item in list1:
        # Verifica se o item está na segunda lista
        if item in set_list2:
            # Adiciona à lista de resultados se não estiver lá
            if item not in result:
                result.append(item) # append method appends an element to the end of the list.
    
    # Ordena a lista resultante
    result.sort()
    
    return result

print(intersect([-3, 4, 76], [19, 27, 4, -3]))
print(intersect([4, 76, -1, -2], [19, -2, -1, 27, 4, -3]))
print(intersect([1, 4, 76], [19, 27, 5, -3]))