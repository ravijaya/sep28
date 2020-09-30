import sqlite3

conn = sqlite3.connect('sep30.sqlite')
cur = conn.cursor()

query = """
create table tasks (
    id integer primary key autoincrement, 
    title text,
    description text, 
    done boolean
);
"""
cur.execute(query)

cur.close()
conn.close()