# Herança

# 1. O que é Herança?
    # Herança permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse).

# Exemplos de reuso:
    # As classes Card e Deck podem ser reutilizadas em diversos jogos de cartas.
        # Criar uma nova classe que adiciona funcionalidades extras a uma existente.

# 2, Exemplo de Implementação
    # Problema criar uma classe MyList que:
        # Se comporte como uma lista padrão
        # Tenha um método adicional choiche() qye retorna um elemento aleatório

import random

class MyList:
    def __init__(self, initial=[]):
        self.lst = initial

    def __len__(self):
        return len(self.lst)
    
    def append(self, item):
        self.lst.append(item)

    def choice(self):
        return random.choice(self.lst)
    
    def __repr__(self):
        return f"MyList({self.lst})"
    
# Teste
mylist = MyList()
mylist.append(2)
mylist.append(1)
mylist.append(11)
print(mylist)
print(mylist.choice())