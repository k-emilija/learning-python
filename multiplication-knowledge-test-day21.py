print("✨ Test your multiplication knowledge! ✨")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math questions to solve.")
print()

number = int(input("Enter the number you want: "))

# To keep track of the score
score = 0

for i in range (1, 11):
  # For loop will loop through input question 10 times
  answer = int(input(f"What is {i} x {number}? "))
  print()
  correct_answer = i * number

  if answer == correct_answer:
    print("Correct! 🎊")
    score += 1
  else:
    print(f"Incorrect! The correct answer is {correct_answer}. 🤨")

# Display the final score
if score == 10:
  print("Wow! A perfect score! 🥳")
else:
  print(f"You got {score} out of 10 questions correct.")