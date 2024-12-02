# 1. Problema Inicial: Encapsulamento Inadequado
    # Exemplo do Problema:
        # A classe Queue permite que erros internos, como o uso de uma lista vazia (IndexError), sejam expostos diretamente ao usuário.
        # Isso força o usuário a entender detalhes internos da implementação, o que não é ideal.

    # Solução Geral:
        # Criar uma exceção personalizada chamada EmptyQueueError.
        # Levantar essa exceção em vez de erros genéricos para maior clareza e encapsulamento.

# 2. Levantando Exceções
    # Como levantar uma exceção:
# raise ValueError("Mensagem de erro personalizada: ")

# Comportamento de raise:
    # Altera o fluxo do programa, mudando para um estado de exceção.  
    # # Pode aceitar uma mensagem para descrever o erro.

# 3. Exceçoes definidas pelo usuário
    # Estrutura básica:
        # Exceções personalizadas são subclasses de Exception.
# class MyError(Exception):
    # pass
        # Uso:
# raise MyError("Erro específico definido pelo usuário")

# 4. Classe Queue Revisitada
    # Objetivo: Melhorar o encapsulamento e clareza levantando uma exceção personalizada quando a fila está vazia.
    # Implementação:

class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.q = []
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError("dequeue from empty queue")
        return self.q.pop(0)
    
# Teste
queue = Queue()
try:
    queue.dequeue
except EmptyQueueError as e:
    print(e)

# 5. Benefícios do Uso de Exceções Personalizadas
    # Clareza:
        # Usuários de uma classe lidam com erros específicos ao domínio, e não com erros genéricos do Python.
    # Encapsulamento:
        # Esconde detalhes internos de implementação.
    # Reuso:
        # Exceções personalizadas podem ser usadas em diferentes partes de um sistema que compartilham lógica de domínio.