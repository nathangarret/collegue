# criem uma nova lista e atribuam a uma variável chamada romanos, contendo as strings 'Julius', 'Augustus', 'Brutus' e 'Cassius'.
romanos = ['Julius', 'Augustus', 'Brutus', 'Cassius']

# criem uma lista e atribuam a uma variável chamada ingleses, contendo as strings 'Dickens', 'Austen', 'Henry' e 'Elizabeth'.
ingleses = ['Dickens', 'Austen', 'Henry', 'Elizabeth']

# criem uma lista e atribuam a uma variável chamada governantes, que contém os dois primeiros elementos da lista romanos e os dois últimos elementos da lista ingleses. Use expressões de manipulação de lista; não copie os dados apenas manualmente.
governantes = romanos[:2] + ingleses[2:]

print(governantes)