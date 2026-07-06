from database.database import DatabaseManager

db = DatabaseManager()

print("=" * 50)
print("DATABASE TABLES")
print("=" * 50)

tables = db.get_tables()

for table in tables:
    print(table["name"])

print("\n")

for table in tables:

    table_name = table["name"]

    print("=" * 50)
    print(f"SCHEMA : {table_name}")
    print("=" * 50)

    schema = db.get_schema(table_name)

    for column in schema:
        print(dict(column))

    print()

db.close()