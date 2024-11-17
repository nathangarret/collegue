# Codificação de Strings

# Um objeto string (str) contém uma sequência ordenada de 
# caracteres que pode ser qualquer um dos seguintes:
# • Letras maiúsculas e minúsculas (alfabeto latino): 
# a b c … z e A B C … Z
# • Dígitos decimais: 0 1 2 3 4 5 6 7 8 9
# • Pontuações: , . : ; ‘ “ ! ? etc.
# • Operadores matemáticos e símbolos comuns:
# = < > + - / * $ # % @ & etc.
# • Mais detalhes virão
# Cada caractere é mapeado para um código binário para ser 
# representado na memória
# Por muitos anos, o padrão usado para esse mapeamento foi o 
# American Standard Code for Information Interchange (ASCII)

# ASCII

print(ord('a')) # ord - recebe o caractere e retorna seu código ASCII
print(chr(97)) # chr - recebe o código ASCII e retorna o caracter

# Unicode transformation formaat - UTF
# • No Unicode, todo caractere é representado por um inteiro chamado ponto de código. 
# • O ponto de código não é necessariamente a representação de bytes do caractere; é somente um identicador do caractere
# • O ponto de código para a letra a é o inteiro cuja representação é o inteiro com valor hexadecimal 0x0061
# • Para caracteres ASCII, o Unicode convenientemente usa o ponto de códigoigual ao código ASCII

print('\u0061')
print('\u0064\u0061d')
print('\u0409\u0443\u0431\u043e\u043c\u0438\u0440')
print('\u4e16\u754c\u60a8\u597d!')

# Uma string Unicode é uma sequência de pontos de código (0 to 0x10FFFF) 
# Diferente dos códigos ASCII, os pontos de código não são guardados diretamente na memória
# A regra que transforma caracteres Unicode em bytes é chamada de uma codificação (encoding)
# Existem muitas codificações: UTF-8, UTF-16, and UTF-32(UTF significa Unicode Transformation Format)
# • UTF-8 é o padrão usado para codificar textos em e-mails e páginas web
# • UTF-8 também é a codificação padrão para programas em Python 3
# • Em UTF-8, todo caracteres ASCII tem uma codificação de 8 bits
