import sqlite3
conn = sqlite3.connect('test.db')
import datetime
c = conn.cursor()

c.execute("DELETE FROM STUDENTS WHERE ID=8")
conn.commit()
conn.close()
