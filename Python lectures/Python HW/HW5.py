# program chooses a secret random number between 1 and 100. The user has a limited number of attempts to guess it.#ter each guess, the program tells the user if their guess was "too high," "too low," or "correct."
import random
def number_guessing():
   print(random.randrange(1, 100))
number_to_guess =(random.randrange(1, 100) )
attempts = 3
print ("A number has been generated. You have 3 attempts to guess it")

guess = int(input("Take a guess: "))
attempts += 1
if guess>number_to_guess:
    print("Too high!")

elif guess<number_to_guess:
    print ("Too low")

else: 
    print("Correct")


