# Polimorfismo
    # O polimorfismo na programação orientada a objetos, mostrando como métodos podem ser sobrescritos ou estendidos em subclasses, promovendo reutilização de código e flexibilidade.

# 1. Sobrescrevendo Métodos de Superclasse
# Definição: Subclasses podem herdar métodos de superclasses e, se necessário, sobrescrevê-los para ajustar comportamentos específicos.

# Exemplo com Classes Animal e Passaro:
class Animal:
    def __init__(self, especie, lingua):
        self.especie = especie
        self.lingua = lingua

    def falar(self):
        print(f"Eu sou um(a) {self.especie} e eu {self.lingua}")

class Passaro(Animal):
    def falar(self):
        print(f"{self.lingua}! " * 3)
    
# Teste
snoppy = Animal("cachorro", "latido")
snoppy.falar()

tweety = Passaro("canário", "pio")
tweety.falar()

# 2. Hierarquia de Atributos e Métodos
    # Quando um método é chamado, o Python procura sua definição no namespace do objeto e, se não encontrar, sobe na hierarquia da classe até a superclasse.
    # Isso permite que métodos sejam sobrescritos em subclasses sem alterar o comportamento na superclasse.

# 3. Estendendo Métodos da Superclasse
    # Definição: Em vez de sobrescrever completamente um método, podemos estendê-lo, chamando a versão da superclasse dentro da versão da subclasse.

class Super:
    def metodo(self):
        print("em Super.metodo")

class Extentido(Super):
    def metodo(self):
        print("Começando Extendido.metodo") 
        super().metodo()
        print("terminando Extendido.metodo")

# Teste
obj = Extentido()
obj.metodo()


# 4. Exemplo de Funcionários com Polimorfismo
    # Problema: Criar um método para gerenciar horas extras que se comporte diferentemente para funcionários gerais e gerentes.

print("\nFuncionários com Polimorfismo")
class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.horas_extras = 0

    def contarHoraExtra(self):
        self.horas_extras += 1

class Gerente(Funcionario):
    def contarHoraExtra(self):
        self.horas_extras += 1.5

# Teste:
funcionario_1 = Funcionario("João")
funcionario_1.contarHoraExtra()
print(funcionario_1.horas_extras)  # Saída: 1

gerente_1 = Gerente("Maria")
gerente_1.contarHoraExtra()
print(gerente_1.horas_extras)  # Saída: 1.5

# 5. Benefícios do Polimorfismo
    # Flexibilidade: Subclasses podem implementar comportamentos específicos sem alterar a superclasse.
    # Reuso de Código: Métodos e atributos da superclasse são herdados automaticamente.
    # Extensibilidade: Novas funcionalidades podem ser adicionadas sem alterar o código existente.

# Sobrescrever Métodos
    # Classes podem sobrescrever métodos de suas superclasses para comportamentos específicos
    # Exemplo: Classe (Animal) e subclasse (Bird):
class Animal:
    def __init__(self, especie, som) -> None:
        self.especie = especie
        self.som = som
    def speak(self) -> str:
        print(f"Eu sou um {self.especie} e faço {self.som}")

class Bird(Animal):
    def speak(self) -> str:
        print(f"{self.som}! {self.som}! {self.som}!")

tweety = Bird("canário", "pio")
tweety.speak()