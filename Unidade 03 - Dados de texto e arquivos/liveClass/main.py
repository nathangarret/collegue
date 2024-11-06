# Insira elemento em uma lista
elementos = ['Walter', 'é', 'um', 'ótimo']
elemento_add_um = "professores"
elemento_add_dois = "dos"
elemento_add_tres = "melhores"

elementos.remove(elementos[3])

elementos.append(elemento_add_um)
print(elementos)

elementos.insert(3, elemento_add_dois)
print(elementos)

elementos.insert(4, elemento_add_tres)
print(elementos)

def palavras_ate_5_letras(palavras):
    return [palavra for palavra in palavras if len(palavra) <= 7]

palavras_aleatorias = ["Relâmpago", "Harmonia", "Borboleta", "Desafio", "Oceano", "Luminária", "Melodia", "Horizonte", "Vagalume", "Serenidade"]

palavras_curta = palavras_ate_5_letras(palavras_aleatorias)
print(palavras_curta)

# Abrindo arquivos - Read
import os

infile = os.path.dirname(os.path.abspath(__file__))
way_file = os.path.join(infile, 'sequencias.txt')
# print(way_file)

fill = open(way_file)
readFile = fill.read()

print(readFile)
print(type(readFile))
print(len(readFile))

readFile = readFile.split("\n")
print(readFile)
print(type(readFile))

print(len(readFile))

for linha in readFile:
    l = linha.split("\t")
    soma = 0
    for n in l:
        soma += eval(n)
    if soma > 200:
        print(linha)