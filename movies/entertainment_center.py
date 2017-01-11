#
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

reservoir_dogs = media.Movie("Reservoir Dogs",
                            "A heist gone wrong",
                            "https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg",
                            "https://www.youtube.com/watch?v=vayksn4Y93A")

snatch = media.Movie("Snatch",
                    "Two sides of the London unground collide",
                    "https://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
                    "https://www.youtube.com/watch?v=Q8jbt0wBkMI")

mallrats = media.Movie("Mallrats",
                        "Just another day at the mall",
                        "https://upload.wikimedia.org/wikipedia/en/9/96/Mallrats.jpg",
                        "https://www.youtube.com/watch?v=_eVo7aBze1w")

in_bruges = media.Movie("In Bruges",
                        "Two hit men hide out in a small town in Belgium",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/In_Bruges_Poster.jpg",
                        "https://www.youtube.com/watch?v=KoE9edjEDCI")

movies = [toy_story, avatar, reservoir_dogs, snatch, mallrats, in_bruges]

fresh_tomatoes.open_movies_page(movies)
