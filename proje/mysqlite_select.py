import sqlite3
conn = sqlite3.connect('us.db')
import datetime
c = conn.cursor()
a ="Chingiz"
q= "barca123"
# c.execute("SELECT PAGE FROM USERS WHERE NAME = \'"+a+"\' AND SURNAME =\'"+q+"\' ")
c.execute("SELECT * FROM USERS")
l=c.fetchall()
print(l)
conn.close()
