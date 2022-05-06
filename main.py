"""
--------------------
TINY IMPERFECT PIANO
--------------------
This project is intended to be a
music player to practice using Sound
objects in pygame.
"""

"""
ROUGH PLAN:
Two channels will be used for music so
that as one song fades out, the next
will fade in.

One channel will be used for alert tones
to recognize inputs.

Console will display song information
and control options.

STRETCH GOAL:
pygame GUI?
"""

# Import and initialize pygame,
# pygame.mixer, and custom library
import pygame
import lib

pygame.init()
pygame.mixer.init()

display = pygame.display.set_mode((300,300))

# Create two Channel objects for music playback
# and one for alert tones
main_channel0 = pygame.mixer.Channel(0)
main_channel1 = pygame.mixer.Channel(1)
alert_channel = pygame.mixer.Channel(2)

# Generate dictionary of album objects and
# list of album names
albums, album_names = lib.scan_for_music()

while True:
  album_choice = lib.choose_album(album_names)
  
  track_names = lib.load_album(album_choice, albums)

  play_choice = input(
    "\nChoose one: \
    \n1. Play " + album_choice + "\
    \n2. View track list \
    \n3. Choose another album \
    \nQ. Quit \n")
  
  if play_choice == "1":
    lib.play_album(album_choice, albums)
    
  elif play_choice == "2":
    print()
    for i in range(len(track_names)):
      print(str(i + 1) + ". ", track_names[i])
    track_choice = input("\nWhich track? \n")
    lib.play_track(track_choice, album_choice, albums)
    
  elif play_choice == "3":
    print("\nChoose another album.")
    
  elif play_choice == "q" or play_choice == "4":
    print("\nbye")
    break