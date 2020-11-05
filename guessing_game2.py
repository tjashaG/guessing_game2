import random
from pathlib import Path

MIN_NUMBER = 1
MAX_NUMBER = 1000
SECRET = random.randint(MIN_NUMBER, MAX_NUMBER)
not_guessed = True
number_of_guesses = 0

if __name__ == "__main__":
    scores = Path(".", "data", "scores.txt")
    top_score = int(scores.read_text())
    print(f"The top score so far is {top_score}. Can you beat it?")

    print(f"Guess the secret number between {MIN_NUMBER} and {MAX_NUMBER}! Can you beat your top score?")
    #print(SECRET)

    while not_guessed:
        guess = int(input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: "))

        while guess < MIN_NUMBER or guess > MAX_NUMBER:
            print("Please input a number within the valid range!")
            guess = int(input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: "))

        if guess == SECRET:
            print(f"You guessed it! The number was {SECRET}. It took you {number_of_guesses} guesses!")
            if number_of_guesses < top_score:
                scores.write_text(str(number_of_guesses))
                print(f"You've beat the top score with {number_of_guesses} guesses!")
            else:
                print(f"Sorry, you didn't beat the top score with {number_of_guesses} guesses!")
            not_guessed = False
        elif guess < SECRET:
            print("Wrong number. Try higher!")
            number_of_guesses += 1
        else:
            print("Wrong number. Go lower!")
            number_of_guesses += 1
