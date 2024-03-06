-- SQLite
-- Changing filmID to autoincrement 
BEGIN;
-- Create a new table with autoincrement on filmID
CREATE TABLE tblFilms_new (
    filmID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    yearReleased INTEGER,
    rating TEXT,
    duration INTEGER,
    genre TEXT
);
-- Copy all data from old table to the new table
INSERT INTO tblFilms_new (
        filmID,
        title,
        yearReleased,
        rating,
        duration,
        genre
    )
SELECT filmID,
    title,
    yearReleased,
    rating,
    duration,
    genre
FROM tblFilms;
-- Delete the old table and rename new table to original table's name
DROP TABLE tblFilms;
ALTER TABLE tblFilms_new
    RENAME TO tblFilms;
COMMIT;