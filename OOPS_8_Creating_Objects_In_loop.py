class Movie:
    def __init__(self, moviename, movieruntime, movieactor):
        self.moviename = moviename
        self.movieruntime = movieruntime
        self.movieactor = movieactor

    def printer(self):
        print(f"Movie name : {self.moviename}, Movie Runtime : {self.movieruntime}, Movie Actor : {self.movieactor}")

if __name__ == "__main__":
    newmoview = True
    list_of_movies = []
    while newmoview == True:
        moviename = input("Please enter movie name")
        movieruntime = input("Please enter movie runtime")
        movieactor = input("Please enter movie actor")
        obj = Movie(moviename,float(movieruntime),movieactor)
        list_of_movies.append(obj)
        anothermovie = input("Do you want to add another movie")
        if anothermovie.casefold() == "no":
            newmoview = False


    for movie in list_of_movies:
        movie.printer()