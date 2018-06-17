import webbrowser
#This class will contain properties of a movie are that need to be encapsulated in a movie object such as movie titles, box art, poster images, and movie trailer URLs.
class Movie():
    def __init__(self,title,storyline,poster_image,trailer):
        #print self
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
