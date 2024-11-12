# Escreva um laço que solicitará repetidamente números inteiros ao usuário. Quando o usuário digitar 0, deverá ser impresso um relatório dizendo quantos números foram digitados e a sua soma. O número 0 final não deve ser contado.
# Um exemplo de execução é visto a seguir
# >>>
# Digite um número: 5
# Digite um número: -1
# Digite um número: 0
# Foram digitados 2 números. A soma total foi 4

def relatorio_numeros():
    quantidade = 0
    soma = 0

    while True:
        numero = int(input("Digite um número: (inteiro)\n"))

        if numero == 0:
            break

        quantidade += 1
        soma += numero

    print(f"Foram digitados {quantidade} números. A soma total foi {soma}.")
    
relatorio_numeros()