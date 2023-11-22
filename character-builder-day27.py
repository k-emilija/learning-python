import random, os, time

print("✨ Welcome to this amazing Character Builder! ✨\n")
  
def roll_dice(sides):
  result = random.randint(1, sides)
  return result

def generate_health_stat():
  roll_6_sided_dice = roll_dice(6)
  roll_12_sided_dice = roll_dice(12)
  health = int((roll_6_sided_dice * roll_12_sided_dice) / 2 + 10)
  return health

def generate_strength_stat():
  roll_6_sided_dice = roll_dice(6)
  roll_12_sided_dice = roll_dice(12)
  strength = int((roll_6_sided_dice * roll_12_sided_dice) / 2 + 12)
  return strength

while True:
  character_name = input("Name your character:\n")
  print()
  character_type = input("Character Type (Elf, Wizard, Human, Dwarf):\n")
  print()
  print(character_name)
  print(f"HEALTH: {generate_health_stat()}")
  print(f"STRENGTH: {generate_strength_stat()}")
  print()
  print("May your name go down in Legend…")
  print()
  more_characters = input("Do you want to create another character? (yes / no)\n").lower()
  if more_characters == "no":
    break
  time.sleep(1)
  os.system("clear")