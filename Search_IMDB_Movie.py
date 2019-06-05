# Ethan Miller
# 3/13/2019

try:
  from pyperclip import copy
  from imdb import IMDb
  from re import search
except ModuleNotFoundError as e:
  print('Oops! Something went wrong.', e)
  input('Press enter to exit . . .')
  exit()
    
# Create an instance of the IMDb class.
ia = IMDb()

def getMovieTitles(search, num_results):
  '''
  Reads in a string to search IMDB for
  and returns num_results number of results found.
  '''
  # Create a zero-based list to parellel the number of results we want to be displayed.
  return_num = range(num_results)
  # Create an empty list to hold a list of movies.
  movie_titles = []
  # Search IMDB for movies that match our search.
  movies = ia.search_movie(search)
  # For each movie we 
  for number in return_num:
    movie = movies[number]
    # Update result to get the basic information.
    ia.update(movie)
    # Get the title and year.
    title = movie.get(movie.keys()[0])
    year = movie.get(movie.keys()[2])
    # Concatonate the strings together and append it.
    movie_name = f'{title} ({year})'
    # Append the movie name to movie_titles.
    movie_titles.append(movie_name)
  return movie_titles

def selectTitle():
  pass

def checkMovieTitles(search, num_results):
  '''
  Error handling for returnMovieTitles() function.
  '''
  try:
    return returnMovieTitles(search, num_results)
  except:
    # If IMDB can't find the movie from volume information, manually input the Title.
    while True:
      try:
        title_input = input('Oops! IMDB can\'t find that title. Please manually enter the movie title: ')
        return returnMovieTitles(title_input, num_results)
      except:
        continue

def copyTitle(search, num_results):
  '''
  Copies the movie title and year returned by
  the getImdbTitle() function to clipboard.
  '''
  # Search for movie.
  movies = getMovieTitles(search, num_results)
  movie_name = movies[0]

  # Remove special characters from string.
  movie_name = movie_name.translate({ord(i): None for i in '<>:"/\|?*'})

  # Copy movie name to clipboard.
  copy(movie_name)

# Get search input from user.
title_input = input('Please enter the title and year of the movie you want: ')

# Test for flags.
search_object = search(r'(.*)-(\d)', title_input)
if search_object:
  num_results = int(search_object.group(2))
  search = search_object.group(1)
  print(f'Searching IMDB for first {num_results} results . . .')
  print(getMovieTitles(search, num_results))
else:
  copyTitle(title_input, 1)