import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or type 'exit' to quit): ")

        if guess.lower() == "exit":
            print("Game exited. The number was:", number_to_guess)
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
