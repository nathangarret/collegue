def menuDeAcesso():
    numero_tentativas = 0
    while True:
        print("\n 1 - Entrar \n 2 - Exibir tentativas \n 3 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            senha = input("Digite a senha: ")
            if senha == "pythonEhLegal":
                print("Bem-vindo ao sistema! :)")
                return
            else:
                numero_tentativas += 1
                if numero_tentativas == 3:
                    print("Você já tentou 3 vezes. Acesso negado!")
                    return
        elif opcao == 2:
            print(f"Número de tentativas: {numero_tentativas}")
        elif opcao == 3:
            return

menuDeAcesso()