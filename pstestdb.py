import sqlite3

conn = sqlite3.connect('sep30.sqlite')
cur = conn.cursor()

query = 'select sqlite_version()'
cur.execute(query)
print(cur.fetchone())

cur.close()
conn.close()