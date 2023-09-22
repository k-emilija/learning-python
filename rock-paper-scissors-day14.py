print("E P I C  B A T T L E 🪨 📄✂️ ")
print()
print("This is a game of rock, paper and scissors!")
print()
print("In this game you have to choose one of these by writing\nR for Rock\nP for Paper\nS for Scissors")
print()

# to ensure that whenever is typed in input, each player cannot see what the other player typed in
from getpass import getpass as input

player1 = input("Player 1, please select your move (R, P or S)! > ").upper()
player2 = input("Player 2, Please select your move (R, P or S)! > ").upper()

print()

if player1 == player2:
  print("It's a tie!")
elif player1 == "P":
  if player2 == "R":
    print("Player 1 wins!")
  elif player2 == "S":
    print("Player 2 wins!")
  else:
    print("Invalid move! Try again!")
elif player1 == "R":
  if player2 == "S":
    print("Player 1 wins!")
  elif player2 == "P":
    print("Player 2 wins!")
  else:
    print("Invalid move! Try again!")
elif player1 == "S":
  if player2 == "P":
    print("Player 1 wins!")
  elif player2 == "R":
    print("Player 2 wins!")
  else:
    print("Invalid move! Try again!")
else:
  print("Invalid move! Try again!")