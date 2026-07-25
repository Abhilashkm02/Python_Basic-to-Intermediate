'''Create a class with a constructor
    *Write a class movie with attributes Title and rating
    *Create multiple objects of the class and display their attributes using a method'''


class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def display_info(self):
        print(f"Movie Title: {self.title}, Rating: {self.rating}")

# Create multiple objects of the class
movie1 = Movie("Ironman", 8.8)
movie2 = Movie("Avengers", 9.3)
movie3 = Movie("spiderman", 9.0)

# Call the display_info() method for each object
movie1.display_info()
movie2.display_info()
movie3.display_info()

