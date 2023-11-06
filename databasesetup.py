import sqlite3
conn = sqlite3.connect('therapy.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE RESPONSE
         (WORD BYTE     NOT NULL,
         RESPONSE           TEXT    NOT NULL);''')
print ("Table created successfully");

conn.close()