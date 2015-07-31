#!/usr/local/bin/python3
#coding: UTF-8
import psycopg2
import psycopg2.extras

conn = psycopg2.connect("dbname=chats user=hal password=immortal")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute("""SELECT * FROM table1 WHERE id = 1""")
rows = cur.fetchall()
for row in rows:
	print( "   ", row['fname'], "   ", row['id'])

conn.commit()

cur.execute("""INSERT INTO table1 (fname) VALUES (%s)""", ('Васелов',))
conn.commit()

cur.close()
conn.close()