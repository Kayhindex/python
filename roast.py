import sqlite3 as sq
import json
conn = sq.connect('database.db')
cur = conn.cursor()

cur.executescript("""DROP TABLE IF EXISTS user;
            DROP TABLE IF EXISTS course;
            DROP TABLE IF  EXISTS member;
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            name TEXT  UNIQUE)
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS course(
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE)
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS member(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            course_id INTEGER,
            role INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id)
            FOREIGN KEY(course_id) REFERENCES course(id))
            """)

conn.commit()

file = input('Enter the file name: \n')
if len(file)<1: file = 'roster_data_sample.json'

handler = open(file).read()
json = json.loads(handler) 

for var in json:
    name = var[0]
    title = var[1]

    # print(name, title)

    cur.execute("INSERT OR IGNORE INTO user(name) VALUES(?)", (name,))
    cur.execute("SELECT id FROM user WHERE name = (?)", (name,))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO course(title) VALUES(?)", (title,))
    cur.execute("SELECT id FROM course WHERE title = (?)", (title,))
    course_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO member(user_id, course_id)  VALUES(?,?)", (user_id, course_id))

    conn.commit()

cur.execute('SELECT user.name, course.title FROM user INNER JOIN course ON user.id = member.course_id')
rows = cur.fetchall()
for row in rows:
    print(row)