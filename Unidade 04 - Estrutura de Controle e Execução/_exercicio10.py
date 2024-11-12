"""  
Especificação
A constante matemática Pi é um número irracional com valor aproximado de 3,1415928... O valor preciso do quadrado dessa constante pode ser obtido com a seguinte soma infinita:

Piˆ2 = 8 + 8*(1/3)^2 + 8*(1/5)^2 + 8*(1/7)^2 + 8*(1/9)^2 + ...

(Pi é, naturalmente, a raiz quadrada desse valor).

Embora não possamos calcular essa soma infinita, obtemos uma boa aproximação do valor de Pi^2 ao calcular a soma dos termos iniciais dessa série. Escreva uma função chamada approxPIsquared() que recebe um número como entrada que representa um erro de aproximação. A sua função deve calcular uma aproximação de Piˆ2, somando N primeiros termos da série acima. Para decidir até que valor da série somar, você deve fazê-lo até que a diferença entre a soma obtida somando-se o N-ésimo termo e a soma anterior (até o termo de ordem N-1) seja menor do que o número passado na entrada da função. A função deve retornar a soma obtida.

Como exemplos de execução:

>>> approxPIsquared(0.0001)
9.855519952254232
>>> approxPIsquared(0.00000001)
9.869462988376474
"""