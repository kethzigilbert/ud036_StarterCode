import media
import fresh_tomatoes
'''
This file creates a list of movie objects by calling the
constructor to instantiate movie objects.
These objects is stored in a list data structure.
This list of movies is passed to the open_movies_page()
function as input to build the HTML file which displays the website.
'''
toystory = media.Movie(
    "Toystory",
    "Toystory Storyline",
    "https://bit.ly/2wkpqR5",  # NOQA
    "https://bit.ly/VZggnq"   # NOQA
    )
avatar = media.Movie(
    "Avatar",
    "Avatar Storyline",
    "https://bit.ly/1JofiD1",  # NOQA
    "https://bit.ly/1vJjkEs"   # NOQA
)
wonderwoman = media.Movie(
    "Wonder Woman",
    "Wonder woman Storyline",
    "https://bit.ly/2sZ0i01",  # NOQA
    "https://bit.ly/2fiI5m1"   # NOQA
)
ironman = media.Movie(
    "IronMan",
    "Iron Man Storyline",
    "https://bit.ly/2rLG8b8",  # NOQA
    "https://bit.ly/2oPeTFS"  # NOQA
)
greatestshowman = media.Movie(
    "The Greatest Showman",
    "The greatest showman storyline",
    "https://bit.ly/2mHyqJa",  # NOQA
    "https://bit.ly/2smpt99"  # NOQA
)
thelastsong = media.Movie(
    "The Last Song",
    "The last Song storyline",
    "https://bit.ly/2JWnJ3c",  # NOQA
    "https://bit.ly/2cc1WUW"  # NOQA
)

movies = [toystory, avatar, wonderwoman, ironman, greatestshowman, thelastsong]
fresh_tomatoes.open_movies_page(movies)
