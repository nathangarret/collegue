def cities():
    lista_cidades = []

    while True:
        city = input('Enter city: ')

        if city != "":
            return lista_cidades
        
        lista_cidades.append(city)

print(cities())