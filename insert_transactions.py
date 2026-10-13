import sqlite3

conn = sqlite3.connect("retail_business.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Insert orders
cursor.executemany("""
INSERT OR IGNORE INTO orders
(order_id, customer_id, order_date, status)
VALUES (?, ?, ?, ?)
""", [
    (101, 1, '2025-01-20', 'Delivered'),
    (102, 2, '2025-02-10', 'Delivered'),
    (103, 3, '2025-02-15', 'Delivered'),
    (104, 1, '2025-03-12', 'Delivered'),
    (105, 4, '2025-03-25', 'Delivered'),
    (106, 5, '2025-04-05', 'Delivered'),
    (107, 6, '2025-04-18', 'Delivered'),
    (108, 2, '2025-05-10', 'Delivered'),
    (109, 7, '2025-06-15', 'Delivered'),
    (110, 8, '2025-07-20', 'Delivered'),
    (111, 3, '2025-08-05', 'Delivered'),
    (112, 9, '2025-09-10', 'Delivered'),
    (113, 10, '2025-10-15', 'Delivered'),
    (114, 4, '2025-11-05', 'Delivered'),
    (115, 11, '2025-12-10', 'Delivered'),
    (116, 12, '2026-01-15', 'Delivered'),
    (117, 5, '2026-02-10', 'Delivered'),
    (118, 6, '2026-03-20', 'Delivered'),
    (119, 7, '2026-04-15', 'Delivered'),
    (120, 8, '2026-05-10', 'Delivered')
])

# Insert order items
cursor.executemany("""
INSERT OR IGNORE INTO order_items
(item_id, order_id, product_id, quantity, unit_price)
VALUES (?, ?, ?, ?, ?)
""", [
    (1, 101, 1, 1, 55000),
    (2, 101, 3, 2, 2000),
    (3, 102, 2, 1, 25000),
    (4, 102, 9, 1, 1500),
    (5, 103, 4, 2, 8000),
    (6, 104, 8, 1, 15000),
    (7, 104, 3, 3, 2000),
    (8, 105, 5, 1, 12000),
    (9, 106, 1, 1, 55000),
    (10, 107, 6, 10, 100),
    (11, 108, 2, 2, 25000),
    (12, 109, 10, 1, 7000),
    (13, 110, 8, 2, 15000),
    (14, 111, 3, 5, 2000),
    (15, 112, 9, 4, 1500),
    (16, 113, 4, 1, 8000),
    (17, 114, 1, 1, 55000),
    (18, 115, 7, 5, 150),
    (19, 116, 2, 1, 25000),
    (20, 117, 5, 2, 12000),
    (21, 118, 8, 1, 15000),
    (22, 119, 10, 2, 7000),
    (23, 120, 1, 1, 55000)
])

# Insert payments
cursor.executemany("""
INSERT OR IGNORE INTO payments
(payment_id, order_id, amount, payment_date, payment_method)
VALUES (?, ?, ?, ?, ?)
""", [
    (1, 101, 59000, '2025-01-20', 'UPI'),
    (2, 102, 26500, '2025-02-10', 'Card'),
    (3, 103, 16000, '2025-02-15', 'UPI'),
    (4, 104, 21000, '2025-03-12', 'Card'),
    (5, 105, 12000, '2025-03-25', 'UPI'),
    (6, 106, 55000, '2025-04-05', 'Net Banking'),
    (7, 107, 1000, '2025-04-18', 'UPI'),
    (8, 108, 50000, '2025-05-10', 'Card'),
    (9, 109, 7000, '2025-06-15', 'UPI'),
    (10, 110, 30000, '2025-07-20', 'Card'),
    (11, 111, 10000, '2025-08-05', 'UPI'),
    (12, 112, 6000, '2025-09-10', 'Card'),
    (13, 113, 8000, '2025-10-15', 'UPI'),
    (14, 114, 55000, '2025-11-05', 'Card'),
    (15, 115, 750, '2025-12-10', 'UPI'),
    (16, 116, 25000, '2026-01-15', 'Card'),
    (17, 117, 24000, '2026-02-10', 'UPI'),
    (18, 118, 15000, '2026-03-20', 'Card'),
    (19, 119, 14000, '2026-04-15', 'UPI'),
    (20, 120, 55000, '2026-05-10', 'Card')
])

conn.commit()

print("Orders, order items, and payments inserted successfully!")

# Verify all five tables
for table in ["customers", "products", "orders", "order_items", "payments"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table}: {cursor.fetchone()[0]} records")

conn.close()