import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population TEXT)""")

conn.close()

