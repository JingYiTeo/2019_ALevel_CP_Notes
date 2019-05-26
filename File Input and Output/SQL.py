#create tabele
CREATE TABLE contacts (rid INTEGER PRIMARY KEY, name TEXT, dob TEXT, email TEXT, mobile TEXT);


#select all (*) entries from (table)
SELECT * FROM contacts;


#select specific (columns) from (table)
SELECT name, email FROM contacts;


#insert into (table)  with (field names) and then values
INSERT INTO contacts (name, dob, email, mobile)
VALUES ('Lim Ah Seng', '1995-01-01','limahseng@hotmail.com', '12345678');


#update (table) and new values
#given criteria (the ones need updating)
UPDATE contacts SET mobile = '88888888'
WHERE rid = 1;


#delete (same as update)
DELETE FROM contacts
WHERE rid = 1;


#using sqlite3
import sqlite3

# create database connection ("name of database")
connection = sqlite3.connect("contactdb.sqlite")

# create cursor
cursor = connection.cursor()

# create table
cursor.execute("CREATE TABLE contacts (rid INTEGER, name TEXT, dob TEXT, email TEXT, mobile TEXT);")

# insert
cursor.execute("INSERT INTO contacts (rid, name, dob,email, mobile) VALUES (1, 'Lim Ah Seng', '1995-01-01', 'limahseng@hotmail.com', '12345678');")

# select
cursor.execute("SELECT * FROM contacts;")

# update
cursor.execute("UPDATE contacts SET mobile = '88888888' WHERE rid = 1;")

# delete
cursor.execute("DELETE FROM contacts WHERE rid = 2;")

# make changes permanent
connection.commit()

#fetching the commits
results = cursor.fetchall()

#print out all the data in the database queried
for record in results:
    print(record)

# destroy database connection (and cursor)
connection.close()
