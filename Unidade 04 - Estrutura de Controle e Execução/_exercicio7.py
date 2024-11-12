""" 
Lembre que os numerais romanos usam os símbolos M, D, C, X, V e I cujos valores decimais são:

Um exemplo de execução é mostrado a seguir:

M = 1000        D = 500        C = 100
X =   10        V =   5        I =   1
Por exemplo, o numeral romano MDCXVII corresponde a:

1000+500+100+10+5+1+1+1=1617
Há regras mais complicadas. Por exemplo, IV normalmente é 4, mas usaremos uma versão simples de numerais romanos onde apenas acumulamos os valores de cada um dos símbolos. Por exemplo, MIIIMMDCM, avaliaremos como 41000 + 31 + 1500 + 1100 = 4603. Escreva uma função roman() que toma como entrada uma string s, avalia e retorna o valor de s como um numeral romano de acordo com essas regras simplificadas.

Exemplos de execução:

>>> roman('MDCXVII')
1617
>>> roman('MIIIMMDCM')
4603

"""

def roman(s):
    # Dicionário que mapeia os símbolos romanos aos seus valores decimais
    valores = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'X': 10,
        'V': 5,
        'I': 1
    }
    
    # Variável para armazenar o valor total
    total = 0
    
    # Para cada caractere na string, soma o valor correspondente
    for char in s:
        if char in valores:
            total += valores[char]
    
    return total

print(roman('MDCXVII'))  # Saída: 1617
print(roman('MIIIMMDCM'))  # Saída: 4603