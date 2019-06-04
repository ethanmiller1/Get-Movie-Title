# Ethan Miller
# 3/13/2019

from pyperclip import copy
from win32api import GetVolumeInformation
from imdb import IMDb
from wmi import WMI

# Create an instance of the IMDb class.
ia = IMDb()

def getVolumeLabel(drive):
    '''
    Reads in a disk drive ("D:\\") and returns its volume label.
    '''
    # return name of movie from DVD Drive
    volume_information = GetVolumeInformation(drive)
    volume_label = volume_information[0]
    return volume_label

def getImdbTitle(search):
    '''
    Reads in a string to search IMDB for
    and returns the first result found.
    '''
    try:
      movie = ia.search_movie(search)[0]
    except:
      # If IMDB can't find the movie from volume information, manually input the Title.
      done = False
      while done == False:
        try:
          title_input = input('Oops! IMDB can\'t find that title. Please manually enter the movie title: ')
          movie = ia.search_movie(title_input)[0]
          done = True
        except:
          continue

    # Update result to get the basic information.
    ia.update(movie)

    # Get the title and year.
    title = movie.get(movie.keys()[0])
    year = movie.get(movie.keys()[2])

    # String the input together and return it.
    movie_name = f'{title} ({year})'
    return movie_name

# Note: This function adds about 6 seconds to runtime. It is recomended that you remove it and simply set {letter} to your cdrom (e.g. replace letter = findCdRoms() with letter = 'D:')
def findCdRoms():
  '''
  Tests all of your disk drives to see whether
  they are a cdrom or not and returns the item
  selected from a list of drive letters that are cdroms.
  '''
  # Get the drive letter of your DVD drive.
  cdroms = WMI()
  letters = []
  for cdrom in cdroms.Win32_CDROMDrive():
      letters.append(cdrom.Drive)

  if len(letters) > 1:
    # Print the available drives.
    for letter in letters:
      print(f'{letters.index(letter)+1}. {letter}')
    # Input validation.
    while True:
      try:
        # Promt user to select drive.
        index = input('Please select which drive to search (by number): ')
        return letters[int(index)-1]
      except IndexError:
        print('Index error: That number doesn\'t appear to match any of the disk drives listed.')
        continue
      except ValueError:
        print('Value error: Value must be a numeric digit. Try again and God bless.')
        continue
      except Exception as e:
        print('Opps! Something went wrong. ', e)
        continue
  else:
    return letters[0]

# Get the volume label of your cdrom.
letter = findCdRoms()
movie_name = getImdbTitle(getVolumeLabel(letter))

# Remove special characters from string.
movie_name = movie_name.translate({ord(i): None for i in '<>:"/\|?*'})

# Copy movie name to clipboard.
copy(movie_name)