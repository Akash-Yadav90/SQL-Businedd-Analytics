import sqlite3

conn = sqlite3.connect("retail_business.db")
cursor = conn.cursor()

for table in ["customers", "products"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} records")

conn.close()