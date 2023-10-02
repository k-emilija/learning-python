import random
# 'random' is a module in Python's standard library that provides functions for generating random numbers and performing random operations

print("G U E S S  T H E  N U M B E R")
print()
print("In this game you will have to guess a number between 1 and 1000 and I will tell you if you are too low, too high, or get it correct.")
print()


secret_number = random.randint(1, 1000)
# generates a random integer between 1 and 1000 (inclusive)
counter = 0

# WHILE LOOP STARTS HERE
while True:
  players_guess = input("Enter a number between 0 and 1000!\n")
  print()

# user input validation and error handling
  try:
    players_guess = int(players_guess)
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    continue

  counter += 1

  if players_guess < 0:
    print("You can't choose a negative number. Please choose a number greater than or equal to 1.🤨 Try again!")
  elif players_guess > 1000:
    print("That won't do it! Please choose a number less than or equal to 1000. 🤨 Try again!")
    continue
  elif players_guess > secret_number:
   print("Too high!")
   print()
  elif players_guess < secret_number:
   print("Too low!")
   print()
  else:
   print(f"WOW, you really guessed it! Good job! ✨👍")
   print(f"It took you {counter} time(s) to guess the secret number.")
   break