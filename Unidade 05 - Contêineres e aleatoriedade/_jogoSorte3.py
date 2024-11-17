import random

def choose_door(stage):
    """Simulates a stage of the door-choosing game.

    Args:
        stage: The current stage of the game (1, 2, or 3).

    Returns:
        True if the player advances/wins, False if they lose.
    """
    print(f"Stage {stage}: Choose a door (1, 2, or 3):")
    choice = int(input())

    if choice < 1 or choice > 3:
      print("Invalid choice. Please enter 1, 2, or 3.")
      return choose_door(stage) # recursively call function until valid input is entered


    if stage == 3:
        winning_door = random.randint(1, 3)
        if choice == winning_door:
            print("You win!")
            return True
        else:
            print("You lose!")
            return False
    else:
        winning_doors = random.sample(range(1, 4), 2) # Pick 2 winning doors
        if choice in winning_doors:
            print("You advance to the next stage!")
            return True
        else:
            print("You lose!")
            return False

def play_game():
    """Plays the entire three-stage door-choosing game."""
    if choose_door(1):
        if choose_door(2):
            choose_door(3)

play_game()