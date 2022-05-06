import os
from shutil import move
import pygame


#################################
#       ORGANIZE BY ALBUM       #
# Build a list of Album objects #
#################################

class Album:
  def __init__(self, path, name):
    self.path = path
    self.name = name
    self.track_list = []

# Scan the music folder and return a list of folders inside.
def scan_for_music():
  
  albums = {}
  album_names = []
  
  # Scan the "Music" folder for all contents.
  with os.scandir("Music") as dir:
    
    # Make a list of all folders, and move any single songs
    # to the "misc" folder.
    for item in dir:
      
      # If it's a folder, add it to the album_names list and
      # albums dict as Album object.
      if not item.is_file():
        album_names.append(item.name)
        albums[item.name] = Album(("Music/" + item.name), item.name)
        
      # If it's a file, shutil.move() it to "misc".  Create "misc"
      # first if it does not already exist.
      elif item.is_file():
        try:
          move(("Music/" + item.name), "Music/misc/" + item.name)
        except:
          os.mkdir("Music/misc")
          move(("Music/" + item.name), "Music/misc/" + item.name)
          album_names.append("misc")
          albums["misc"] = Album("Music/misc", "misc")

  return albums, album_names


#################################
#    SONG OBJECTS FOR ALBUMS    #
#  Populate user chosen album   #
#   object with Song objects    #
#################################

class Song:
  def __init__(self, path, name):
    self.path = path
    self.name = name
    self.object = pygame.mixer.Sound(self.path)
  
# Get input to choose from available albums and return an album name.
def choose_album(album_names):
  print("\nChoose an album from below:")
  for i in range(len(album_names)):
    print((str(i+1) + ". "), album_names[i])
    
  album_choice = int(input()) - 1
  
  return album_names[album_choice]

# Return a list of Song objects for a given album.
def load_album(album, albums):
  track_names = []
  directory = albums[album].path
  
  # Scan the album for .mp3 files.
  with os.scandir(directory) as dir:
    
    # If the file is an .mp3, add the name to the track_names
    # list and append a Song object to Album.track_list.
    for file in dir:
      if file.name.endswith(".mp3"):
        track_names.append(file.name)
    track_names.sort()
    for track in track_names:
      albums[album].track_list.append(Song((directory + "/" + track), track))

  return track_names


#################################
#    PLAY BY ALBUM AND TRACK    #
#################################

def play_track(track, album, albums):
  selected_track = albums[album].track_list[int(track) - 1]
  print("\nNow playing", selected_track.name + "...")
  selected_track.object.play()
  while pygame.mixer.get_busy():
    pygame.time.wait(60)

def play_album(album, albums):
  for track in albums[album].track_list:
    print("\nNow playing", track.name + "...")
    track.object.play()
    while pygame.mixer.get_busy():
      pygame.time.wait(60)