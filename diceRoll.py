import random

def roll_dice():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    return [roll_dice() for _ in range(num_dice)]

def get_number_of_dice():
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? (1, 2, or 3): "))
            if num_dice in [1, 2, 3]:
                return num_dice
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def main():
    num_dice = get_number_of_dice()
    rolls = roll_multiple_dice(num_dice)
    print(f"You rolled: {rolls}")
    print(f"Sum of rolls: {sum(rolls)}")

if __name__ == "__main__":
    main()

