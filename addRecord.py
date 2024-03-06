from connect import *

# Create a subroutine to add a film record to database

def add_film():
    try:
        # filmID is autoincrement so no data required
        # Get user input for film details and store in variables
        title = input("Enter film title: ")
        yearReleased = input("Enter release year: ")
        rating = input("Enter film rating: ")
        duration = input("Enter film duration: ")
        genre = input("Enter film genre: ")

        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)", (title, yearReleased, rating, duration, genre))

        dbCon.commit() # Makes the changes in the table permanent

        print(f"\n{title} has been added to database.\n")
    
     #  Handles errors that may occur when interacting with the database

    except sql.OperationalError as oe:
        print(f"Failed due to {oe}")
    
    except sql.ProgrammingError as pe:
        print(f"Failed due to Programming Error: {pe}")
    
    except sql.Error as e:
        print(f"Failed due to Error: {e}")
        
if  __name__ == "__main__": #  Only runs if this script is executed, not imported
    add_film()

