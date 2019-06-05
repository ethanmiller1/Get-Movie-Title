# Ethan Miller
# 3/13/2019

from pyperclip import copy
from win32api import GetVolumeInformation, GetLogicalDrives
from win32file import GetDriveType
from imdb import IMDb

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

def getDrives():
  '''
  Searches for local disk drives matching letters A-Z
  that are in use and returns a list of the results.
  '''
  # Create an empty list to hold the drives.
  drives = []
  bitmask = GetLogicalDrives()
  # Test for each possible drive letter.
  for letter in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    # If drive exists, append to list of drives.
    if bitmask & 1:
      drives.append(letter)
    bitmask >>= 1

  return drives

def getDriveTypes():
  '''
  Searches a list of disk drives and returns a
  dictionary of the same list as keys with
  drive type information as values.
  '''
  # Create an empty dictionary to hold the drive / drive types.
  types = {}
  # Create a list of drive types for typeIndex to match.
  driveTypes = ['DRIVE_UNKNOWN', 'DRIVE_NO_ROOT_DIR', 'DRIVE_REMOVABLE', 'DRIVE_FIXED', 'DRIVE_REMOTE', 'DRIVE_CDROM', 'DRIVE_RAMDISK']

  for drive in getDrives():
    try:
      # GetDriveType() will return a number that represents a drive type.
      typeIndex = GetDriveType(u"%s:\\"%drive)
      # Add new key / value pairs to the 'types' dictionary, where the drive letter is the key and the type is the value.
      types[f'{drive}:'] = driveTypes[typeIndex]
    except Exception as e:
      print('Error: ', e)
  return types

def getCdRoms():
  '''
  Searches a dictionary of drives and
  drive types and returns a list of
  drives that are CD ROMs.
  '''
  drives = getDriveTypes()
  cdroms = []
  for drive, drive_type in drives.items():
    if drive_type == 'DRIVE_CDROM':
      cdroms.append(drive)
  return cdroms

def selectCdRom():
  '''
  Tests how many CD ROMs are in the machine,
  and if more than 1, prompts the user to
  select which CD ROM to use.
  '''
  cdroms = getCdRoms()

  if len(cdroms) > 1:
    # Print the available drives.
    for letter in cdroms:
      print(f'{cdroms.index(letter)+1}. {letter}')
    # Input validation.
    while True:
      try:
        # Promt user to select drive.
        index = input('Please select which drive to search (by number): ')
        return cdroms[int(index)-1]
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
    return cdroms[0]

# Get the volume label of your CD ROM.
drive = selectCdRom()
movie_name = getImdbTitle(getVolumeLabel(drive))

# Remove special characters from string.
movie_name = movie_name.translate({ord(i): None for i in '<>:"/\|?*'})

# Copy movie name to clipboard.
copy(movie_name)