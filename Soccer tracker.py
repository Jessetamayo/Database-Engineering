import sqlite3

# 1. Open the Filing Cabinet (Database)
connection = sqlite3.connect("academy.db")
cursor = connection.cursor()

# 2. Create the "Form" (Table) if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Players (Name TEXT)")

print("--- Database Ready! ---")

while True:
    p_name = input("What is the player name? ")
    p_pos = input("What position? ")
    if p_name == "quit":
        print("Done")
        break
    cursor.execute("INSERT INTO Players (Name,Position) VALUES (?,?)", (p_name,p_pos))
    connection.commit()
    print(f"Saved {p_name},{p_pos}")

print("\n--- Roster Breakdown (Pivot Table) ---")

# 1. Select Position and COUNT the names, then Group By Position
query = """
SELECT Position, COUNT(Name) 
FROM Players 
GROUP BY Position
"""
cursor.execute(query)

# 2. Print the stats
for row in cursor.fetchall():
    # row[0] is the Position, row[1] is the Count
    print(f"Position: {row[0]} | Count: {row[1]}")

connection.close()