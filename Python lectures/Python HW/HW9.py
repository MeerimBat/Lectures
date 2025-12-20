import random

def roll_dice():
    # Simulate rolling two dice
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1, dice_2

def main():
    print("Welcome to the Double Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice (or type 'q' to quit): ").strip().lower()
        if input == 'q':
            print("Thanks for playing! Goodbye!")
            break
        dice_1, dice_2 = roll_dice()
        print(f"You rolled: {dice_1} and {dice_2}")
        print(f"Total: {dice_1 + dice_2}\n")

    dict_frequency = {i: 0 for i in range(2, 13)}
    print(dict_frequency)
    for i in range(roll_dice):
        rolling_result = roll_dice()
        dict_frequency[rolling_result]+=1
    return dict_frequency

print(main())
freq = {}
for item in ():
    freq[item] = freq.get(item, 0) + 1

print(freq)

if __name__ == "__main__":
    main()

# a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

freq = {}
for item in a:
    freq[item] = freq.get(item, 0) + 1

print(freq)
