""" 
Primeira parte
Nos Estados Unidos, a temperatura é medida em graus Fahrenheit em vez de graus Celsius. É bem simples converter uma esacla na outra: se C representa a temperatura em Celsius e F, a tempratura em Fahrenheit correspondente é dada por: ** F = (9C/5)+32**.
"""

def convert(i):
    # i = Celsius
    # return j = Fahrenheit
    
    j = (9 * i / 5) + 32
    
    return j

print(convert(0))
print(convert(20))
 
print("\nTable:")

def table():
    print(f"{'F':<7} {'C':>7}") 
    for c in range(-30, 41, 10):
        f = convert(c) # O segredo de unir as duas funções está nessa linha! :)
        print(f"{f:<7.1f} {c:>7.1f}")
print(table())

""" 
Partes da f-string
'F':>7:

'F': É a string que queremos imprimir. Neste caso, representa a letra "F" para Fahrenheit.
:>: O símbolo > indica que o conteúdo deve ser alinhado à direita.
7: O número 7 especifica a largura total do campo. Portanto, F será impresso em um espaço de 7 caracteres, alinhado à direita. Se F ocupar menos de 7 
caracteres, espaços em branco serão adicionados à esquerda.
"""