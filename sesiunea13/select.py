import sqlite3
from pprint import pprint

con = sqlite3.connect("online_shop.db")
cursor = con.cursor()

print('*' * 50)

cursor.execute("SELECT * FROM Products")
pprint(cursor.fetchall())

print('*' * 50)

cursor.execute("SELECT * FROM Cart_items")
pprint(cursor.fetchall())
