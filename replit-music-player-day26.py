# This code will only work in replit, but I am saving it here for a future reference.
"""

from replit import audio
import os, time

def play_music():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    stop_playback = int(input("Press number 2 if you want to stop the playback and go back to the menu "))
    if stop_playback == 2:
      source.paused = True
      return
    else:
      continue

while True:
  os.system("clear")
  print(f"✨ MyPOD Music Player ✨")
  time.sleep(1)
  print(f"Press 1 to Play Music")
  time.sleep(1)
  print(f"Press 2 to Exit")
  time.sleep(1)
  print(f"Press any other number to see the menu again")
  user_input = int(input())
  if user_input == 1:
    print(f"Playing music!")
    play_music()
  elif user_input == 2:
    exit()
  else:
    continue
    
"""