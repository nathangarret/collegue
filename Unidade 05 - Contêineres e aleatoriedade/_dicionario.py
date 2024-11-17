# Containers são dicionário - Armazenar mais de um tipo
# Exemplo = CPF
# Chaves - Valor

employee = {
    "864-20-9753": ['Anna', 'Karenina'],
    "987-65-4321": ['Yu', 'Tsun'],
    "100-01-9010": ['Hans', 'Castorp']
}

print(employee)
# Não são ordenados - Mutáveis

employee['100-01-9010'] = "Holden Cafield"
print(employee)

# - novos(key, value) podem ser
# O valor de uma associado a uma chave pode ser modificado
employee['864-20-9753'] = "Holden Cafield"
print(employee)

#
def complete(abbreviation):

    days = {
        'Mo': 'Monday',
        'Tu': 'Tuesday',
        'We': 'Wednesday',
        'Th': 'Thursday',
        'Fr': 'Friday',
        'Sa': 'Saturday',
        'Su': 'Sunday',
    }

    return days[abbreviation]

print(complete(abbreviation='Mo'))

#
def frequency(item_list):
    counters = {}

    for item in item_list:
        if item in counters:
            counters[item] += 1
        else:
            counters[item] = 1
    return counters

print(frequency([95, 96, 100, 85, 95, 90, 95, 100, 100]))

#
def word_count(text):

    word_list = text.split() # Divide o texto em palavras

    counters = {}

    for word in word_list:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    
    for word in counters:
        if counters[word] == 1:
            print('{:8} appears {} time.'.format(word, counters[word]))
        else:
            print('{:8} appears {} times.'.format(word, counters[word]))

print(word_count('all animals are eqaul but some animals are more equal than other'))