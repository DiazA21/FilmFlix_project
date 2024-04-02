import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('filmflix.db')

# Create a cursor object
cur = conn.cursor()

# Delete records
cur.execute("DELETE FROM tblFilms WHERE filmID = 42")

# Reset the filmID counter
cur.execute("UPDATE SQLITE_SEQUENCE SET SEQ=? WHERE NAME='tblFilms'", (39 + 1,))

# Commit the changes and close the connection
conn.commit()
conn.close()