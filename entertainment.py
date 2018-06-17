import media
import fresh_tomatoes
'''
This file creates a list of movie objects by calling the constructor to instantiate movie objects.
These objects is stored in a list data structure. This list of movies is passed to the
open_movies_page() function as input to build the HTML file which displays the website.
'''
toystory=media.Movie("Toystory","Toystory Storyline","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("Avatar","Avatar Storyline","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
wonderwoman=media.Movie("Wonder Woman","Wonder woman Storyline","https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg","https://www.youtube.com/watch?v=1Q8fG0TtVAY")
ironman=media.Movie("IronMan","Iron Man Storyline","https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG","https://www.youtube.com/watch?v=8hYlB38asDY")
greatestshowman=media.Movie("The Greatest Showman","The greatest showman storyline","https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png","https://www.youtube.com/watch?v=AXCTMGYUg9A")
thelastsong=media.Movie("The Last Song","The last Song storyline","https://upload.wikimedia.org/wikipedia/en/1/12/LastSongposterMarch31.png","https://www.youtube.com/watch?v=vZH0Nf4KLBo")

movies=[toystory,avatar,wonderwoman,ironman,greatestshowman,thelastsong]
fresh_tomatoes.open_movies_page(movies)


