import sqlite3
from pathlib import Path

project_dir = Path(__file__).resolve().parent
db_path = project_dir / "retail_business.db"
sql_path = project_dir / "queries.sql"

if not db_path.exists():
    raise FileNotFoundError(f"Database not found: {db_path}")

if not sql_path.exists():
    raise FileNotFoundError(f"SQL file not found: {sql_path}")

sql_text = sql_path.read_text(encoding="utf-8")

with sqlite3.connect(db_path) as conn:
    statements = [
        statement.strip()
        for statement in sql_text.split(";")
        if statement.strip()
    ]

    for index, statement in enumerate(statements, start=1):
        print(f"\n{'=' * 50}")
        print(f"QUERY {index}")
        print("=" * 50)

        try:
            cursor = conn.execute(statement)

            if cursor.description:
                columns = [column[0] for column in cursor.description]
                rows = cursor.fetchall()

                print(" | ".join(columns))
                print("-" * 50)

                for row in rows:
                    print(" | ".join(str(value) for value in row))

                print(f"\nRows returned: {len(rows)}")
            else:
                print("Statement executed successfully.")

        except sqlite3.Error as error:
            print(f"SQL execution error: {error}")
            print("Problematic SQL statement:")
            print(statement)