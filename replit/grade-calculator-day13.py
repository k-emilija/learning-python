# The program will ask the user to type in the name of a test, the maximum score they could have received, and how many points they received. For example, test could be called "Python Skills" and the maximum score is 50 points and the user receives 30 points out of 50 possible points.  

print("✨ Exam Grade Calculator ✨")
print("")

print("Let's calculate your " + input("What is the name of the exam?\n") + " exam grade!")
print("")

max_score = int(input("Enter Max. Possible Score:\n"))
print("")
your_score = int(input("Enter Your Score:\n"))

# Figure out the percentage the user received and round to 2 decimal places

percentage = round(float(your_score / max_score) * 100, 2)
print("")

# print(f"Your percentage: {percentage}")

if percentage <= 49:
  print(f"You got {percentage}% which is a U")
elif percentage >= 50 and percentage <= 59:
  print(f"You got {percentage}% which is a D")
elif percentage >= 60 and percentage <= 69:
  print(f"You got {percentage}% which is a C")
elif percentage >= 70 and percentage <= 79:
  print(f"You got {percentage}% which is a B")
elif percentage >= 80 and percentage <= 89:
  print(f"You got {percentage}% which is a A-")
elif percentage >= 90:
  print(f"You got {percentage}% which is a A+")
else:
  print("Try again!")
  