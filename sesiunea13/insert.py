import sqlite3

con = sqlite3.connect("online_shop.db")
cursor = con.cursor()

cursor.execute("INSERT INTO CATEGORIES (name) VALUES ('Accesorii PC')")
cursor.execute("INSERT INTO CATEGORIES (name) VALUES ('Anvelope masina')")

###########################################################################
products_values = [
    ('Cooler', 'raceste procesor', 99, 1),
    ('Debica', 'anvelope R15', 259, 2),
]

SQL_query = "INSERT INTO PRODUCTS (name, description, price, category_id) VALUES (?,?,?,?)"
cursor.executemany(SQL_query, products_values)
###########################################################################
users_values = [
    ('Josh', 'abc123'),
    ('Andrei', '4444333221')
]

SQL_query = "INSERT INTO USERS (username, password) VALUES (?,?)"
cursor.executemany(SQL_query, users_values)
###########################################################################
carts_values = [
    ('1', '21.2.2023'),
    ('1', '21.2.2023'),
    ('2', '21.2.2023'),
    ('2', '21.2.2023')
]

SQL_query = "INSERT INTO CARTS (user_id, created_at) VALUES (?,?)"
cursor.executemany(SQL_query, carts_values)

###########################################################################
cart_items_values = [
    ('1', '1', 3),
    ('2', '2', 2),
    ('3', '1', 100),
    ('4', '2', 5)
]

SQL_query = "INSERT INTO CART_ITEMS (cart_id, product_id, quantity) VALUES (?,?,?)"
cursor.executemany(SQL_query, cart_items_values)

con.commit()
