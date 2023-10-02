print("E P I C  B A T T L E 🪨 📄✂️ ")
print()
print("This is a game of rock, paper and scissors!")
print()
print("In this game you have to choose one of these by writing\nR for Rock\nP for Paper\nS for Scissors")
print()

# to ensure that whenever is typed in input, each player cannot see what the other player typed in
from getpass import getpass as input

# Created counter variables outside the loop
player1_score = 0
player2_score = 0

# Creating a while loop
while True:
 player1 = input("Player 1, please select your move (R, P or S)! > ").upper()
 player2 = input("Player 2, Please select your move (R, P or S)! > ").upper()

 if player1 == player2:
  print("It's a tie!")
   
 elif player1 == "P":
   if player2 == "R":
    print("Player 1 wins!")
    player1_score += 1
    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")
   elif player2 == "S":
    print("Player 2 wins!")
    player2_score += 1
    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")
   else:
    print("Invalid move! Try again!")
    continue
     
 elif player1 == "R":
   if player2 == "S":
    print("Player 1 wins!")
    player1_score += 1
    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")
   elif player2 == "P":
    print("Player 2 wins!")
    player2_score += 1
    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")
   else:
    print("Invalid move! Try again!")
    continue
     
 elif player1 == "S":
   if player2 == "P":
    print("Player 1 wins!")
    player1_score += 1
    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")
   elif player2 == "R":
    print("Player 2 wins!")
    player2_score += 1
    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")
   else:
    print("Invalid move! Try again!")
    continue
 else:
  print("Invalid move! Try again!")
  continue

 if player1_score == 3 or player2_score == 3:
    print("Thanks for playing!")
    exit()
 else:
    continue