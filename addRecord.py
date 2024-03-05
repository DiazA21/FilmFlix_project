from connect import *

# Create a subroutine to add a film record to database

def add_film():
    # Get user input for film details and store in variables
    title = input("Enter film title: ")
    yearReleased = input("Enter release year: ")
    rating = input("Enter film rating: ")
    duration = input("Enter film duration: ")
    genre = input("Enter film genre")

    dbCursor.execute()

