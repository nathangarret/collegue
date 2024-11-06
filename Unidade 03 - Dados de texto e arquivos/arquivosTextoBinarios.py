# Um arquivo é uma sequência de bytes armazenada em memória secundária de um computador - hd - ssd
# Dados - Programas
# Texto ou binários

# Caminhos absolutos - Desde de o diretório padrão
# Caminho relativos - Dentro de uma pasta do projeto
infile = open('example.txt', 'r')
content = infile.read()
infile.close()

print(content)

# r Modo de leitura (padrão)
# w Modo de gravação; se o arquivo já existir, seu conteúdo é apagado
# a Modo de acréscimo; o conteúdo é ascrescentado ao final do arquivo
# r+ Modo de leitura e gravação (pouco usado)
# t Modo de texto padrão
# b Modo binário

# Tipo arquivo
# arqEntrada.read(n) Lê n caracteres de arqEntrada (ou até que o final do arquivo); Retorna string 
def numCharts(filename):
    'retorna o número de caracteres em um arquivo'
    
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    
    return len(content)


""" arqEntrada.read() Lê até o final do arquivo arqEntrada;
Retorna string """

"""
arqEntrada.readline() Lê linha de arqEntrada (ou até o final do arquivo); 
Retorna string 

arqEntrada.readlines() Lê até o final do arquivo arqEntrada;
Retorna uma lista de strings (cada linha é um elemento da lista) 

arqSaida.write(s) Grava a string s no arquivo arqSaida

file.close(n) Fecha o arquivo file(retorna o número de caracteres escritos)

#
Implemente a função meuGrep() que:
1.Toma como entrada duas strings: um nome de arquivo 
e uma string alvo
2.Exibe cada linha do arquivo que contém a string alvo 

#
Padrões comuns de leitura de um arquivo:
1.Ler o conteúdo do arquivo em uma string
2.Ler o conteúdo do arquivo em uma lista de palavras
3.Ler o conteúdo do arquivo em uma lista de palavras

#
Padrões comuns de leitura de um arquivo:
1.Ler o conteúdo do arquivo em uma string
2.Ler o conteúdo do arquivo em uma lista de palavras
3.Ler o conteúdo do arquivo em uma lista de palavras

    • Arquivos que representam dados são normalmente estruturados
    • Torna a leitura dos dados padronizada, mais rápida e mais fácil
    • Um exemplo de arquivos estruturados são os arquivos CSV, JSON, XML
    • CSV = Comma Separated Files
    • Representar uma tabela 
    • Cada linha representa uma entidade
    • Cada coluna representa uma propriedade
    • As colunas são separadas por vírgulas

#
Leia o conteúdo do arquivo estoque.txt
1.Imprima o produto com o maior nível de vendas
2.Imprima o produto com o menor estoque
3.Imprima a média de vendas dos produtos
1 Produto,Estoque,Vendas\n
2 Leite,200,100\n
3 Farinha,50,200\n
4 Bolacha,15,60\n
5 Sabonete,50,75\n
"""

