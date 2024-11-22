# Módulos como namespaces
# • Um módulo é um arquivo contendo código Python
# • Este namespace temo mesmo nome do módulo
# • Neste namespace, estão armazenados todos os nomes no escopo global do módulo: os nomes de funções, valores e classes definidos no módulo
# • Estes nomessão os atributos do módulo

import math
print(dir(math)) # A função dir() retorna os nomes definidos em um namespace

print(math.sqrt) # <built-in function sqrt>
print(math.pi) # 3.141592

# Quando o interpretador Python executa um comando import ele:
# 1.Procura o arquivo correspondente ao módulo a ser importado
# 2.Roda o código do módulo para criar os objetos definidos nele
# 3.Cria o namespace onde esses objetos serão armazenados O comando import somente recebe um nome, o nome dó modulo
#   • Sem informações do diretório ou extensão O Caminho de Busca para localizar o módulo
#   • O Caminho de busca é a lista de diretórios onde o interpretador procurar por módulos
#   • A variável path definida no módulo da bibliotheca padrão sys aponta para essa lista

import sys

print(sys.path) # Diretório Corrente - Pastas da Biblioteca padrão

# Caminho de busca do módulo:
#   • Ao adicionar/Users/me ao caminho de busca, o módulo example pode ser importado

# Suponha que desejamos importar o módulo example salvo na pasta /Users/me que não está na lista sys.path

# dir() - Nomes no namespace do shell; note que example não está presente

# import example
""" 
Traceback (most recent call last):
  File "/home/persistent/penguin/FGV/collegue/Unidade 06 - Namespaces e controle de fluxo excepcional/_modulosNamespaces.py", line 31, in <module>
    import example
ModuleNotFoundError: No module named 'example' 
"""

""" 
sys.path.append('/Users/me')

import example
print(example.f)
print(example.x)

print(dir()) 
"""

# Aplicações reais são organizadas em módulos:
# Um módulo especial: o “programaprincipal” 
# Este módulo é chamado de módulo de alto nível

# • Os módulosrestantessão chamadosde módulos de “biblioteca” Quando módulossão importados, Python cria variáveis de “manutenção” no namespace do módulo, incluindo a variável __name__:
# • Se o módulo é executado como de alto nível, __name__ = '__main__'
print('My name is {}'.format(__name__))