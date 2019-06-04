# Ethan Miller
# 3/13/2019

# create an instance of the IMDb class
from pyperclip import copy
from win32api import GetVolumeInformation
from imdb import IMDb
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

movie_name = getImdbTitle(getVolumeLabel("D:\\"))

# Remove special characters from string.
movie_name = movie_name.translate({ord(i): None for i in '<>:"/\|?*'})

# Copy movie name to clipboard.
copy(movie_name)