# Orientada a Objetos

# Imagine que queiramos implementar um programa que lida com horários (horas, minutos e segundos). Usando os tipos básicos de Python, como poderíamos guardar essa informação?

# Dependente da motivação
# Opções:
# 1
hora = 20
minuto = 15
segundo = 10

# 2
horario = [20, 15, 10]

# 3
horario_ = {
    'hora': 20,
    'minuto': 15,
    'segundo': 10
}

# 4 - Ter uma classe que representa um horário (tempo)

# t = Tempo(20, 15, 10)
# Tempo(hora, minuto, segundo)

# t.adiantar_tempo(3600)
# print(t) - 21:15:10

# Conceito Básico:
# Classe - Definem novos tipos e suas propriedades
#   • Molde para os objetos
#   • Comumente associados a situações do problema em consideração
#   • Exemplo: Tempo

# Objeto - Realização do conceito definido na classe 
#   • Elemento que segue as propriedades da classe
#   • Estado + Comportamento
#   • Exemplo: 20:15:10

# Atributo - Características dos objetos
#   • hora
#   • minuto
#   • segundo

# Método - Ações realizada por cada objeto da classe
#   • Mecanismo de comunicação do objeto com o "mundo externo"
#   • Exemplo: adiantar_tempo(), numeroSegundo() (classe tempo)

# Notação geral: o.m(x, y)
#   • o - objeto
#   • m - metódo
#   • (x, y) - parâmetros

# PROGRAMAÇÃO ORIENTADA A OBJETOS
# O reuso de código é um benefício chave da organização do código em novas classes; este é possível através da abstração e do encapsulamento
#   • Abstração: Usuários manipulam objetos via invocações dos métodos sem ter que saber dos detalhes de implementação dos métodos
#       • Abstração facilita o desenvolvimento de software, pois um programador trabalha com objetos abstratamente.
#   • Encapsulamento: Para que a abstração seja efetiva, precisamos que o código e dados associados aos objetos sejam encapsulados, ou seja, invisíveis para o programa que use o objeto
#       • Podemos atingir o encapsulamento ideal graças ao mecanismos de namespaces de classes e objetos POO é uma abordagem de programação que atinge a modularização do código através do uso de objetos e da estruturação do código em classes

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado (encapsulado)
    
    def depositar(self, valor):
        self.__saldo += valor
        
    def get_saldo(self):
        return self.__saldo  # Método público para acessar o saldo

# Uso
conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.get_saldo())  # Saída: 1500

# Modularização do código significa organizar o programa em partes independentes e coesas, que colaboram entre si, facilitando o desenvolvimento, a manutenção e a reutilização. Isso é alcançado na POO através de classes e objetos encapsulados, que se comportam como módulos de funcionalidade.