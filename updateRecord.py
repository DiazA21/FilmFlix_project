from connect import *

def update_record():
    # filmID is the primary, unique key. more effiecient to use
    try:
        filmID = int(input("Enter the filmID of the record to be updated: "))
        dbCursor.execute(f"SELECT * FROM tblFilms where filmID = {filmID}")

        # fetchone method gets a unique (one) record
        row = dbCursor.fetchone()

        # none means no such id in database, checks if there's any data returned by query
        if row == None:
            print(f"No record with filmID {filmID} exists, cannot delete.")
        else:
            fieldName = input("Enter the field to update: (title or yearReleased or rating or duration or genre): ").title()
            fieldValue = input(f"Enter the updated value for {fieldName}: ")

            dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = ? WHERE filmID = ? ", (fieldValue, filmID))  # tuple containing new value and ID
            dbCon.commit()
            print(f"\nRecord with filmID {filmID} UPDATED\n")


    except sql.OperationalError as oe:
        print(f"Failed due to {oe}")
    
    except sql.ProgrammingError as pe:
        print(f"Failed due to Programming Error: {pe}")
    
    except sql.Error as e:
        print(f"Failed due to Error: {e}")
        
if  __name__ == "__main__": #  Only runs if this script is executed, not imported
    update_record()
