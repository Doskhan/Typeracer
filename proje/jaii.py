import sqlite3
conn = sqlite3.connect('test.db')
import datetime
c = conn.cursor()
m=[]
# c.execute("SELECT * FROM STUDENTS")
# for row in c:
#     for col in row:
#         print ("\'%s\'" % str(col), end=" ")
#     print()
j=str(c.execute("SELECT * FROM STUDENTS WHERE ID = %d" % 3))
print(c.fetchone())
m.append(j)
print(m)
conn.close()
