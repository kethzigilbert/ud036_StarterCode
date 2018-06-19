import webbrowser


class Movie():
    '''
    This class will contain properties of a movie that are
    needed to be encapsulated in a movie object such as
    movie titles, box art, poster images, and movie trailer URLs.
    '''
    def __init__(self, title, storyline, poster_image, trailer):
        # print self
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
