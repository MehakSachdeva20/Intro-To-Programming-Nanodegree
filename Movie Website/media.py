import webbrowser#it allows to include url which can be opened in various browser

class Movie:#creation the class is done here

    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']#ratings are provided to the movies

    def __init__(#init function is called here whose work is basically to craete a space and is commonly known as constructor
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        ):#self and inint function and movie title,storyline of the movie,image of the poster and youtube trailer are defined here

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #Storing or assigning of the values is done here


        def show_trailer(self):#in order to show the trailer this function is declared here so that the movie starts
            webbrowser.open(self.trailer_youtube_url)
