from connect import *
from tabulate import tabulate

def search_record():
    try:
        # Search by column name - filmID or title or yearReleased or rating or duration or genre
        field = input("\nSearch by filmID or title or yearReleased or rating or duration or genre: \n")

        if field == "filmID":
            # Search by filmID
            filmID = int(input("\nEnter filmID: \n"))
            dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,)) # tuple in brackets so that its not seen as a string with index's for each character
            row = dbCursor.fetchone()  # Fetch one record that matches the given

            if row == None:
                print(f"\nNo record of filmID matches {filmID} in the table\n")
            else:
            #     print(f"\n{row}\n")
            # convert the row data into a list and add headers
                headers = ["filmID", "title", "yearReleased", "rating", "duration", "genre"]
                print(tabulate([list(row)], headers=headers))
        elif field in ["title", "yearReleased", "rating", "duration", "genre"]:
            # Search by title or yearReleased or rating or duration or genre
            strInput = (input(f"Enter the value for {field}: \n"))
        
            # SELECT * FROM tblFilms WHERE "title" or "yearReleased" or "rating" etc... LIKE %strInput%
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{strInput}%' ")
            
            rows = dbCursor.fetchall() # Fetch all records that match the given criteria
        
            if not rows:
                print(f"\nNo record(s) with {field} matching {strInput} found.\n")
            else:
                # Print out each returned row that matches
                # for records in rows:
                #     print(f"{records}\n")
                # convert the rows data into a list of lists and add headers
                headers = ["filmID", "title", "yearReleased", "rating", "duration", "genre"]
                print(tabulate(rows, headers=headers))
        else:
            # Where the field searched is not filmID or title or yearReleased or rating or duration or genre
            print(f"\nSearch field {field} is invalid.\n")

    
    except sql.OperationalError as oe:
        print(f"Failed due to {oe}")
    
    except sql.ProgrammingError as pe:
        print(f"Failed due to Programming Error: {pe}")
    
    except sql.Error as e:
        print(f"Failed due to Error: {e}")
        
if  __name__ == "__main__": #  Only runs if this script is executed, not imported
    search_record()

    