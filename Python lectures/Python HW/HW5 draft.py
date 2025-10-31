import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 5  # Set a limit for the number of guesses

print(f"A number between 1 and 100. You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")            
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}. Better luck next time!")