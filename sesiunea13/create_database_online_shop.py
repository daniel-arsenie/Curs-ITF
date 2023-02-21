import sqlite3

# The 'Categories' table stores information about the different
# product categories available in the store, with each category
# identified by a unique id and a name.
#
# The 'Products' table contains information about the different
# products for sale in the store, with each product identified
# by a unique id. Each product has a name, a description, a price,
# and a category_id that references the id of the category it belongs to.
#
# The 'Users' table stores information about the store's users,
# with each user identified by a unique id. Each user has a username
# and a password.
#
# The 'Carts' table stores information about the shopping carts
# of the store's users. Each cart is identified by a unique id, and
# is associated with a user_id that references the id of the user
# who created it. The created_at field stores the date and time the cart was created.
#
# The 'Cart_items' table stores information about the items
# in each cart. Each cart item is identified by a unique id, and
# is associated with a cart_id that references the id of the cart
# it belongs to, and a product_id that references the id of the product
# being added to the cart. The quantity field stores the number of units
# of the product in the cart.

con = sqlite3.connect('online_shop.db')
cursor = con.cursor()
cursor.executescript("""
CREATE TABLE if not exists Categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE if not exists Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

CREATE TABLE if not exists Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE if not exists Carts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE  if not exists Cart_items (
    id INTEGER PRIMARY KEY,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (cart_id) REFERENCES Carts(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);
""")
