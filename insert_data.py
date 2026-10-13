import sqlite3

conn = sqlite3.connect("retail_business.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Insert customers
cursor.executemany("""
INSERT OR IGNORE INTO customers
(customer_id, customer_name, region, signup_date)
VALUES (?, ?, ?, ?)
""", [
    (1, "Aarav Sharma", "North", "2025-01-10"),
    (2, "Priya Patel", "West", "2025-01-15"),
    (3, "Rahul Verma", "South", "2025-02-01"),
    (4, "Sneha Reddy", "South", "2025-02-18"),
    (5, "Arjun Singh", "North", "2025-03-05"),
    (6, "Ananya Gupta", "East", "2025-03-20"),
    (7, "Vikram Joshi", "West", "2025-04-12"),
    (8, "Isha Mehta", "East", "2025-05-01"),
    (9, "Rohan Das", "North", "2025-05-15"),
    (10, "Kavya Nair", "South", "2025-06-10"),
    (11, "Aditya Rao", "West", "2025-07-05"),
    (12, "Meera Shah", "East", "2025-08-15")
])

# Insert products
cursor.executemany("""
INSERT OR IGNORE INTO products
(product_id, product_name, category, price)
VALUES (?, ?, ?, ?)
""", [
    (1, "Laptop", "Electronics", 55000),
    (2, "Smartphone", "Electronics", 25000),
    (3, "Headphones", "Electronics", 2000),
    (4, "Office Chair", "Furniture", 8000),
    (5, "Desk", "Furniture", 12000),
    (6, "Notebook", "Stationery", 100),
    (7, "Pen Pack", "Stationery", 150),
    (8, "Monitor", "Electronics", 15000),
    (9, "Keyboard", "Electronics", 1500),
    (10, "Bookshelf", "Furniture", 7000)
])

conn.commit()

print("Customers and products inserted successfully!")

conn.close()