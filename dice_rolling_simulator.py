import random


def roll_dice(num_dice, num_faces):
    rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
    return rolls


def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_faces = int(input("Enter the number of faces on each die: "))

        rolls = roll_dice(num_dice, num_faces)
        print("Rolling...")
        print("You rolled:", rolls)

        again = input("Roll again? (yes/no): ")
        if again.lower() != 'yes':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
