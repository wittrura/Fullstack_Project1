# Defines movie class for instantiation of movie objects

# inputs
# movie title, string
# short summary, string
# movie poster image, string of url
# video trailer, string of url

import webbrowser

class Movie():
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
