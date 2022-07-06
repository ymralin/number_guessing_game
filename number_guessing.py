import random

print("Welcome to the number guessing game.\nTry to guess a number between 1 and 100.")
print("(Type 'exit' to quit the game.)\n")

def game():
    def print_guesses(guess_num):
        print(f"You have {guess_num} attempts remaining to guess the number")
    difficulty = ""
    while difficulty == "":
        difficulty_input = input("Choose a difficulty. Type easy or hard:\n")
        if difficulty_input.lower() == "easy":
            difficulty= "easy"
            remaining_guesses = 10
        elif difficulty_input.lower() == "hard":
            difficulty = "hard"
            remaining_guesses = 5
        elif difficulty_input.lower() == "exit":
            quit()

    number = random.randint(1,101)
    print_guesses(remaining_guesses)

    player_guess = 0
    guesses = 0
    while player_guess != number:
        if remaining_guesses<1:
            print(f"You loose. No more guesses. The number was {number}")
            break
        player_guess = ""
        while not player_guess.isnumeric():
            player_guess = input("Make a guess:\n")
            if player_guess.lower() == "exit":
                quit()
        player_guess = int(player_guess)
        guesses+=1
        if player_guess == number:
            print(f"Correct. The number is {number}. You guessed in {guesses} tries.")
        else:
            remaining_guesses -= 1
            if player_guess < number:
                print(f"Too low. {remaining_guesses} attempts remaining.")
            elif player_guess > number:
                print(f"Too high. {remaining_guesses} attempts remaining.")

next_play = True

while next_play:
    game()
    play_again = input("Do you want to play again? Y or N:\n")
    if play_again.lower() == "y":
        next_play = True
    elif play_again.lower() == "n":
        next_play = False
    elif play_again.lower() == "exit":
        quit()