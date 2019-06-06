# Get Movie Title 
**Version 1.0.0** 

[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/windows/)

<div align="center">
    <a href="#usage"><img src="https://github.com/king-melchizedek/Get-Movie-Title/raw/master/images/get_movie_title.png" width="200px"></a>
    <a href="#usage"><img src="https://github.com/king-melchizedek/Get-Movie-Title/raw/master/images/search_movie_title.png" width="200px"></a>
    <br>
</div>

> A simple python console app that finds the title and year of a DVD in your DVD drive.

This application was created to help in keeping with the [Plex file naming convention](https://support.plex.tv/articles/naming-and-organizing-your-movie-media-files/ "Naming and organizing your Movie files") when digitalizing DVD's with Handbrake. Rather than manually searching for the year of each movie, just run this program and it will (1) find the volume label for your DVD, (2) search IMDB for a movie that matches the volume label, and (3) copy the movie title and year to your clipboard in the following format: Title (Year). Then you can paste it right into Handbrake.

## Build

Ensure you have [Python](https://www.python.org/downloads/windows/ "Python Releases for Windows") installed, then:

``` bash
cd venv/Scripts
activate
cd ../..
python Get_IMDB_Movie.py
```

### Dependencies

There are 3 modules used by this program:

``` bash
pip install pypiwin32
pip install pyperclip
pip install IMDbPY
```

### Create an executable

Ensure you have [pyinstaller](https://pypi.org/project/PyInstaller/ "PyPI") installed with this project's dependencies, then:

``` bash
pyinstaller -F -i "..\get_movie_title\images\get_movie_title.ico" Get_IMDB_Movie.py
```

### Create a shortcut as a script

Right-click any directory and select New > Shortcut, then for the location of the shortcut, select the python executable of your virtual environment followed by the location of your python file:

``` bash
..\venv\Scripts\python.exe "..\Get_IMDB_Movie.py"
```

## Usage

<style>
.get_movie_title {
width: 20px;
position: relative;
top: 4px;
}
</style>

### <img src="https://github.com/king-melchizedek/Get-Movie-Title/raw/master/images/get_movie_title.ico" class="get_movie_title" > Get Movie Title

Simply launch the app to copy the move Title (Year) to clipboard.

![](https://github.com/king-melchizedek/Get-Movie-Title/raw/master/demos/Get_Movie_Title.gif)

If the volume label does not contain the name of the movie, the user will be prompted to input it manually.

### <img src="https://github.com/king-melchizedek/Get-Movie-Title/raw/master/images/search_movie_title.ico" class="get_movie_title" > Search Movie Title

Launch the app to manually input the movie you want to search for. Add the flag `-3` to have 3 movies returned, and then pick one. (Replace 3 with however many results you want returned to choose from.)

![](https://github.com/king-melchizedek/Get-Movie-Title/raw/master/demos/Search_Movie_Title.gif)

## Contributors

---

- Ethan Miller <ethan.romans5.8@gmail.com>

---

## License & copyright

© 2019 Ethan Miller