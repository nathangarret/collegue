# Pedra Papel e Tesoura

# Vamos implementar um jogo de pedra papel e tesoura onde o usuário joga contra o computador:
# • Em cada jogada, o jogar escolhe sua opção
# • O sistema avalia o resultado da jogada escolhida com a jogada do computador e mostra o resultado
# • O jogo é repetido até o jogador digitar sair
# • Ao final, o placar final deve ser exibido
import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    score = {"player": 0, "computer": 0, "ties": 0}

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'quit' at any time to end the game.")

    while True:
        player_choice = input("\nMake your choice (rock, paper, scissors): ").strip().lower()
        if player_choice == "quit":
            break
        if player_choice not in options:
            print("Invalid choice! Please choose again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
            score["ties"] += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You won this round!")
            score["player"] += 1
        else:
            print("Computer won this round!")
            score["computer"] += 1

    print("\nGame over! Final score:")
    print(f"You: {score['player']} | Computer: {score['computer']} | Ties: {score['ties']}")

rock_paper_scissors()