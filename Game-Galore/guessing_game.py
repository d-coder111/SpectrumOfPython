import random

def guessing_game():
    # Welcome and difficulty level introduction
    print("Welcome to the Enhanced Number Guessing Game!")

    # Adding difficulty levels (Easy, Medium, Hard)
    print("Choose a difficulty level: ")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")

    # Input to select difficulty level
    while True:
        try:
            difficulty = int(input("Enter 1, 2, or 3 for difficulty: "))
            if difficulty == 1:
                lower_bound = 1
                upper_bound = 50
                max_attempts = 15
                break
            elif difficulty == 2:
                lower_bound = 1
                upper_bound = 100
                max_attempts = 10
                break
            elif difficulty == 3:
                lower_bound = 1
                upper_bound = 200
                max_attempts = 7
                break
            else:
                print("Invalid choice. Please select a valid difficulty (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    score = 100  # Initial score for tracking how well the user performs

    print(f"\nI've selected a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
                print(f"Your final score is {score - (attempts * 5)} points!")  # Subtract points based on attempts
                break

            # Adding hints after incorrect guesses
            if guess != secret_number:
                if secret_number % 2 == 0:
                    print("Hint: The secret number is even.")
                else:
                    print("Hint: The secret number is odd.")

                difference = abs(secret_number - guess)
                if difference > 50:
                    print("Hint: You're way off! More than 50 away!")
                elif difference > 20:
                    print("Hint: Getting warmer! You're 20-50 away.")
                elif difference > 10:
                    print("Hint: You're within 10-20 of the number!")
                else:
                    print("Hint: Very close! You're within 10 of the number!")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    # If user has used all attempts
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")
        print(f"Your final score is {score - (attempts * 5)} points.")

    # Adding replay option to make the game more dynamic
    replay = input("Would you like to play again? (yes/no): ").strip().lower()
    if replay == 'yes':
        guessing_game()  # Recursively call the game function for a new round
    else:
        print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    guessing_game()
