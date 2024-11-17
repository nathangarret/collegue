# Advinhe o número: 

# O computador determina um número secreto, e o jogador deve adivinhar o número. Para cada adivinhação, o computador diz se o número é muito alto ou muito baixo, como a seguir:

import random as rd

def guess_the_number():
    secret_number = rd.randint(1, 10)
    attempts = 0

    print("Drawing a number between 1 and 10... \nLet's begin! Try to guess the number!")

    while True:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}: "))
            if guess < secret_number:
                print("The drawn number is greater than: ", guess)
            elif guess > secret_number:
                print("The drawn number is less than: ", guess)
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")

guess_the_number()