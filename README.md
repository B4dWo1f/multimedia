# Multimedia

Set of codes that list the movies in a given folder and retrieves information from imdb (using imdbpy). The information is stored as json files which contain a python dictionary

## list_films.py
List all the files in a given folder excluding certain extensions

## indexar.py
Reads all the movies from a file "peliculas.txt" and search in imdb information about each one of them saving this info in a json file.
The class my_peli (name to be changed) is such that can be initialized empty, and updated passing a dictionary

## Dependencies
sudo apt-get install python-imdbpy
