# 1. Introdução ao Sobrecarga de Operadores
    # Python permite que operadores como +, -, * sejam redefinidos para classes específicas.
    # Isso é feito implementando métodos especiais como __add__, __sub__, etc.

# 2. Operadores como exemplo

# Operador +:
    # ë traduzido para o método __add__

class Point:
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # Outros operadores e seus métodos:
        # - → __sub__
        # * → __mul__
        # / → __truediv__
        # == → __eq__

# 3, Métodos repr() e str()
    # __repr__:
        # Fornece uma representação canônica da instância
        # Ideal para depuração e reconstrução do objeto
    # __str__:
        # Fornece uma representação legível para humanos
        # Usado pelo método print()

# 4. Contratos de consistência
    # A função repr() deve retornar uma string que permita recriar o objeto original usando eval(repr(obj)).

# 5. Implementações em Classes
    # Classe Point:
        # Exemplos de sobrecarga dos operadores + e ==.
    # Classe Card:
        # Implementação de métodos como __repr__ e __eq__ para manipulação de cartas de baralho.

# 6. Exercícios Práticos
    # Implementar os métodos para classes Deck e Card para sobrecarregar:
        # __repr__: Exibir uma representação legível de cartas.
        # __eq__: Comparar se duas cartas são iguais.