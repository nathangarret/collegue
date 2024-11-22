# Modulos como namespaces

# 1. O que são Módulos e Namespaces?
# Um módulo em Python é simplesmente um arquivo contendo código Python. Quando você importa um módulo, ele cria um namespace: um espaço isolado onde os nomes (variáveis, funções, classes) definidos dentro do módulo são armazenados. Isso evita conflitos de nomes: você pode ter uma função calcular() no módulo matematica e outra função calcular() no módulo finanças, sem que uma interfira na outra.

# import math: Importa o módulo math. Os nomes dentro de math (como sqrt, pi, sin, etc.) ficam acessíveis através de math.nome.
import math

raiz_quadrada = math.sqrt(16)
print(raiz_quadrada)

valor_pi = math.pi
print(valor_pi)

# dir(math): Lista todos os nomes (atributos) disponíveis dentro do namespace math.
print(dir(math))

# Importando o módulo -
import sys

print(sys.path)
# Quando você usa import modulo, Python procura pelo arquivo modulo.py em uma lista de diretórios chamada "caminho de busca". A variável sys.path contém esse caminho.

# Se o módulo não for encontrado no caminho de busca, você recebe um ImportError. Você pode adicionar diretórios ao sys.path:
# Suponha que 'meu_modulo.py' esteja em '/home/usuario/meus_modulos'
sys.path.append('/home/usr/meus_modulos')

# import meu_modulo

# Módulo de Alto Nível (__main__)

# __name__ - indica qual módulo está sendo executado - Todo programa Python tem um módulo principal. A variável especial __name__ indica qual módulo está sendo executado. Se o módulo for executado diretamente (não importado), __name__ será "__main__". Isso é útil para colocar código que só deve ser executado quando o arquivo é o programa principal, não quando importado como módulo.

# file _modulosNamespaces.py
def minha_funcao() -> str:
    print("Executando minha função!")

if __name__ == "__main__":
    minha_funcao()

# Diferentes maneiras de importar um módulo
# import modulo: Importa todo o módulo. Acessa os atributos com modulo.atributo.
# from modulo import atributo1, atributo2: Importa atributos específicos. Usa-os diretamente pelo nome.
# from modulo import *: Importa todos os atributos do módulo para o namespace atual. Cuidado: pode causar conflitos de nomes e dificultar a leitura do código. Geralmente, é melhor evitar essa forma.

# In other file that import '_modulosNamespaces.py'
# Forma 1
import _modulosNamespaces
_modulosNamespaces.minha_funcao()

# Forma 2
from _modulosNamespaces import minha_funcao
minha_funcao()

# Forma 3 - Menos recomendada
from _modulosNamespaces import *
minha_funcao()

# Resumindo: módulos e namespaces são ferramentas essenciais para organizar código Python, evitar conflitos de nomes e reutilizar código de forma eficiente. Entender como funcionam é fundamental para escrever programas Python mais robustos e organizados.