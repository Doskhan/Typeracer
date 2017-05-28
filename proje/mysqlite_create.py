import sqlite3
conn = sqlite3.connect('us.db')
c = conn.cursor()

c.execute('''CREATE TABLE last
        (ID INTEGER primary key not null ,
        Name VARCHAR(20) NOT NULL,
        EMAIL VARCHAR(20) NOT NULL UNIQUE,
        PASSWORD VARCHAR(20) NOT NULL)''')
conn.close()
