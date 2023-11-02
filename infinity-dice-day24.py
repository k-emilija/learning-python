import random

print("Infinity Dice 🎲")
print("Welcome to the infinity dice game!\n")

while True:
    sides_input = input("How many sides should your dice have? ")
    try:
        sides = int(sides_input)
        if sides <= 0:
            print("Please enter a positive number for the sides of the dice.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

play_again = "yes"

def roll_dice(sides):
    print(f"You rolled a {random.randint(1, sides)}!")

# With the loop below I call the function and pass the number of sides as an argument.
# The loop will continue until the user enters "no".
while play_again == "yes":
    roll_dice(sides)
    play_again = input("Do you want to play again? (yes/no) ").lower()
    print()
    if play_again == "no":
        print("Thanks for playing!")
        break