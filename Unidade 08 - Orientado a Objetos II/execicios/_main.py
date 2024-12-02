# Problema: Modificar as classes Deck e Card para suportar uma representação formal e comportamentos específicos.

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class Deck:
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in Deck.suits for rank in Deck.ranks]

    def shuffle(self):
        from random import shuffle
        shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

# Teste:
deck = Deck()
deck.shuffle()
print(deck.dealCard())  # Exemplo de saída: Card('4', '♠')

# Problema: Modificar a classe Card para que o operador == retorne True se duas cartas têm o mesmo rank e suit.

card1 = Card('4', '\u2662')
card2 = Card('4', '\u2662')
print(card1 == card2)  # True