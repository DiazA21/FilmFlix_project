from connect import *

def del_film():
    try:
        #filmID is primary key, unique key. More efficient to use
        filmID = int(input("Enter the filmID of the record to be deleted: "))
        dbCursor.execute(f"SELECT * FROM tblFilms where filmID = {filmID}")

        # fetchone method gets a unique (one) record
        row = dbCursor.fetchone()

        # none means no such id in database, checks if there's any data returned by query
        if row == None:
            print(f"No record with filmID {filmID} exists, cannot delete.")
        else:
            dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (filmID,))
            dbCon.commit()
            print(f"\nThe record {filmID} has been successfully deleted\n")

    #  Handles errors that may occur when interacting with the database

    except sql.OperationalError as oe:
        print(f"Failed due to {oe}")
    
    except sql.ProgrammingError as pe:
        print(f"Failed due to Programming Error: {pe}")
    
    except sql.Error as e:
        print(f"Failed due to Error: {e}")
        
if  __name__ == "__main__": #  Only runs if this script is executed, not imported
    del_film()
