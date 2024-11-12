# Um laço infinito provê um serviço contínuo

def hello_ ():
    while True: # Sempre vai ser verdadeiro
        name = input('What`s your name? ')
        print(f'Hi, {name}!\n')

print(hello_())