print('\033[32m✨ Inspirational Anime Quotes Generator ✨\033[0m\n')
# \n is a newline character - when you include \n in a string, it creates a line break or a new line in the output.

name = input('What is your name?\n')
print(f"Hello, {name}! 👋")

# I'm using f-string for a better readability

current_day = input('\nWhat is the current day of the week?\n').lower()  
# I'm converting the user's input to lowercase for a case-insensitive comparison with the .lower() method

if current_day == "monday":
  monday_quote = input("\nDo you want a quote from One Punch Man or Haikyuu?\n").lower()
  if monday_quote == "one punch man":
   print("\nHuman strength lies in the ability to change yourself. – Saitama")
  elif monday_quote == "haikyuu":
   print("\nThe future belongs to those who believe in the beauty of their dreams. - Shoyo Hinata")
  else:
   print("\nOh! You get a random one!\nA dropout will beat a genius through hard work.” –  Rock Lee (Naruto).")
    
elif current_day == "tuesday":
  tuesday_quote = input("\nDo you want a quote from One Piece or Naruto?\n").lower()
  if tuesday_quote == "one piece":
   print("\nDon’t start a fight if you can’t end it. - Sanji")
  elif tuesday_quote == "naruto":
   print("\nIf you don’t like your destiny, don’t accept it. Instead, have the courage to change it the way you want it to be. - Naruto Uzumaki")
  else:
   print("\nOh! You get a random one!\nSimplicity is the easiest path to true beauty. - Seishuu Handa (Barakamon)")

elif current_day == "wednesday":
  wednesday_quote = input("\nDo you want a quote from Naruto or Fairy Tail?\n").lower()
  if wednesday_quote == "naruto":
   print("\nKnowing what it feels to be in pain, is exactly why we try to be kind to others. - Jiraiya")
  elif wednesday_quote == "fairy tail":
   print("\nHurt me with the truth. But never comfort me with a lie. - Erza Scarlet")
  else:
   print("\nOh! You get a random one!\nIf you really want to be strong… Stop caring about what your surrounding thinks of you! - Saitama (One Punch Man)")

elif current_day == "thursday":
  thursday_quote = input("\nDo you want a quote from Fairy Tail or Pokemon?\n").lower()
  if thursday_quote == "fairy tail":
   print("\nMistakes are not shackles that halt one from stepping forward. Rather, they are that which sustain and grow one’s heart. - Mavis Vermillion")
  elif thursday_quote == "pokemon":
   print("\nIt's more important to master the cards you’re holding than to complain about the ones your opponent was dealt.- Grimsley")
  else:
   print("\nOh! You get a random one!\nNot giving up on yourself is what’s truly important. That way you don’t end up pathetic. - Reiko Mikami (Another)")

elif current_day == "friday":
  friday_quote = input("\nDo you want a quote from Bleach or Fate Zero?\n").lower()
  if friday_quote == "bleach":
   print("\nWe are all like fireworks: we climb, we shine and always go our separate ways and become further apart. But even when that time comes, let’s not disappear like a firework and continue to shine forever. - Hitsugaya Toshiro")
  elif friday_quote == "fate zero":
   print("\nDo exactly as you like. That is the true meaning of pleasure. Pleasure leads to joy and joy leads to happiness. - Gilgamesh")
  else:
   print("\nOh! You get a random one!\nYou can't sit around envying other people’s worlds. You have to go out and change your own. - Shinichi Chiaki (Nodame Cantabile")

elif current_day == "saturday":
  saturday_quote = input("\nDo you want a quote from Kokoro Connect or Naruto?\n").lower()
  if saturday_quote == "kokoro connect":
   print("\nWhat you can’t accomplish alone, becomes doable when you’re with someone else. - Taichi Yaegashi")
  elif saturday_quote == "naruto":
   print("\nIt's not always possible to do what we want to do, but it’s important to believe in something before you actually do it. - Might Guy")
  else:
   print("\nOh! You get a random one!\nDo not think about other things, there is only one thing you can do. So master that one thing. Do not forget. What you must imagine is always that you, yourself, are the strongest. You do not need outside enemies. For you, the one you have to fight is none other than your own image. - Archer (Fate Stay Night)")

elif current_day == "sunday":
  sunday_quote = input("\nDo you want a quote from Fairy Tail or One Punch Man?\n").lower()
  if sunday_quote == "fairy tail":
   print("\nFear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder. - Gildarts Clive")
  elif sunday_quote == "one punch man":
   print("\nWho decides limits? And based on what? You said you worked hard? Well, maybe you need to work a little harder. Is that really the limit of your strength? Could you of tomorrow beat you today? Instead of giving in, move forward. - Saitama")
  else:
   print("\nOh! You get a random one!\nIf your life can change once, your life can change again. - Sanae Furukawa (Clannad)")

else:
  print("\nOpps! Something went wrong, please try again! 🤨")