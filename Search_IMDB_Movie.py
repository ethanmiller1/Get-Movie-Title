# Ethan Miller
# 3/13/2019

try:
  from pyperclip import copy
  from imdb import IMDb
except ModuleNotFoundError as e:
  print('Oops! Something went wrong.', e)
  input('Press enter to exit . . .')
  exit()
    
# Create an instance of the IMDb class.
ia = IMDb()

def getImdbMovie(search):
  '''
  Reads in a string to search IMDB for
  and returns the first result found.
  '''
  try:
    return ia.search_movie(search)[0]
  except:
    # If IMDB can't find the movie from volume information, manually input the Title.
    while True:
      try:
        title_input = input('Oops! IMDB can\'t find that title. Please manually enter the movie title: ')
        return ia.search_movie(title_input)[0]
      except:
        continue

def getImdbTitle(movie):
  '''
  Takes in a movie object and concatonates
  the title and year attributes.
  '''
  # Update result to get the basic information.
  ia.update(movie)

  # Get the title and year.
  title = movie.get(movie.keys()[0])
  year = movie.get(movie.keys()[2])

  # String the input together and return it.
  movie_name = f'{title} ({year})'
  return movie_name


title_input = input('Please enter the title and year of the movie you want: ')
movie = getImdbMovie(title_input)
movie_name = getImdbTitle(movie)

# Remove special characters from string.
movie_name = movie_name.translate({ord(i): None for i in '<>:"/\|?*'})

# Copy movie name to clipboard.
copy(movie_name)