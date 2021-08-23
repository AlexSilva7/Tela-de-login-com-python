import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute("""
SELECT * FROM Users;
""")

for linha in cursor.fetchall():

    print (linha)

conn.close()


