# Capturando e manipulando exceções

# try/except
# try caso a excessão for levantada durante a exceção, então o bloco except é executado

# É possível restringir o comando except para capturar um tipo específico de exceção
# Tipos de excessão:
# • KeyboardInterrupt Levantado quando o usuário pressiona Ctrl-C, a tecla de interrupção
# • OverflowError Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande
# • ZeroDivisionError Levantado quando se tenta dividir por 0
# • IOError Levantado quando uma operação de entra/saída falha por um motivo relacionado com E/S
# • IndexError Levantado quando um índice sequencial está fora do intervalo de índices válidos
# • NameError Levantado quando se tenta avaliar um identificador não atribuído (nome)
# • TypeError Levantado quando uma operação da função é aplicada a um objeto do tipo errado
# • ValueError Levantado quando a operação ou função tem um argumento com tipo correto, mas com valor incorreto

import os

def busca_idade(nome_arquivo:str) -> str:

    try:
        arquivo_entrada = open(nome_arquivo)
        str_idade = arquivo_entrada.readline()
        int_idade = int(str_idade)
        print('Idade é: ', int_idade)
    except IOError:
        # Executando somente se for levantada exceção IOError
        print("Erro de entrada/saída.")
    except ValueError:
        # Executando somente se for levantada exceção ValueError
        print("Valor não poder ser convertido para inteiro.")
    except:
        # Executando somente se for levantada exceção
        # Diferente de IOError ou ValueError
        print('Outro erro.')


caminho_pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(caminho_pasta, 'hello-world.txt')

print(arquivo)
busca_idade(arquivo)