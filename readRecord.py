from connect import *
from tabulate import tabulate

def read_films():
    try:
        allFilms = dbCursor.execute("SELECT * FROM tblFilms").fetchall()

        if allFilms:
            print(tabulate(allFilms, headers = ["filmID", "title", "yearReleased", "rating", "duration", "genre"], tablefmt = "grid"))
        else:
            print("No films found in films table")

    except sql.OperationalError as oe:
        print(f"Failed due to {oe}")
    
    except sql.ProgrammingError as pe:
        print(f"Failed due to Programming Error: {pe}")
    
    except sql.Error as e:
        print(f"Failed due to Error: {e}")
        
if  __name__ == "__main__": #  Only runs if this script is executed, not imported
    read_films()
    