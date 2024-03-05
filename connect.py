import sqlite3 as sql # Assign alias sql to the imported sqlite3 module

try:
    with sql.connect("filmflix.db") as dbCon: # Connects to a database named "filmflix.db" if it exists, otherwise creates one and then connects to it
        dbCursor = dbCon.cursor() # Create a cursor object using the connection 

except sql.OperationalError as e:
    print(f"Connection Failed due to {e}")
    