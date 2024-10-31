# Um arquivo é uma sequência de bytes armazenada em memória secundária
# Dados - Programas
# Texto ou binários

# Caminhos absolutos - Desde de o diretório padrão
# Caminho relativos - Dentro de uma pasta do projeto

infile = open('example.txt', 'r')
infile.close()

# r Modo de leitura (padrão)
# w Modo de gravação; se o arquivo já existir, seu conteúdo é apagado
# a Modo de acréscimo; o conteúdo é ascrescentado ao final do arquivo
# r+ Modo de leitura e gravação (pouco usado)
# t Modo de texto padrão
# b Modo binário

# Tipo arquivo
""" 
arqEntrada.read(n) Lê n caracteres de arqEntrada (ou até que o final do arquivo);
Retorna string 

arqEntrada.read() Lê até o final do arquivo arqEntrada;
Retorna string 

arqEntrada.readline() Lê linha de arqEntrada (ou até o final do arquivo); 
Retorna string 

arqEntrada.readlines() Lê até o final do arquivo arqEntrada;
Retorna uma lista de strings (cada linha é um elemento da lista) 

arqSaida.write(s) Grava a string s no arquivo arqSaida

file.close(n) Fecha o arquivo file(retorna o número de caracteres escritos)
"""