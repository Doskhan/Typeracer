# import sqlite3
# conn = sqlite3.connect('test.db')
# import datetime
# c = conn.cursor()
#
# c.execute("INSERT INTO STUDENTS VALUES ('8','Chingiz','Isaev','15 November 1894')")
# c.execute("INSERT INTO STUDENTS (NAME,SURNAME,DATE) VALUES ('Igor','Ivanov','11 September 1967')")
# conn.commit()
#
# conn.close()

import sqlite3
conn = sqlite3.connect('us.db')
import datetime
c = conn.cursor()
c.execute("INSERT INTO last VALUES ('1','Doskhan','Dosya','barca123')")

# c.execute("INSERT INTO qwerty (NAME,SURNAME,EMAIL,PASSWORD,TYPE) VALUES ('Igor','Ivanov','Igor123','igor123',0)")
conn.commit()

conn.close()
