# creates movie objects for displaying on webpage
# import Movie class and functionality for displaying movies in html
import media
import fresh_tomatoes

import requests, json

# request movie data from api
# type: json
r = requests.get('http://localhost:3030/api/movies')
data = r.json()

# instantiation of movie objects using payload from API
toy_story = media.Movie(data['title1'], data['summary1'], data['poster1'], data['trailer1'])

avatar = media.Movie(data['title2'], data['summary2'], data['poster2'], data['trailer2'])

reservoir_dogs = media.Movie(data['title3'], data['summary3'], data['poster3'], data['trailer3'])

snatch = media.Movie(data['title4'], data['summary4'], data['poster4'], data['trailer4'])

mallrats = media.Movie(data['title5'], data['summary5'], data['poster5'], data['trailer5'])

in_bruges = media.Movie(data['title6'], data['summary6'], data['poster6'], data['trailer6'])

# create list of all movies
movies = [toy_story, avatar, reservoir_dogs, snatch, mallrats, in_bruges]

# display list of movies on webpage
fresh_tomatoes.open_movies_page(movies)
