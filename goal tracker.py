import sqlite3

# Connect to the EXISTING database
connection = sqlite3.connect("academy.db")
cursor = connection.cursor()

# 1. Create the Goals Table
# Notice we don't save the Player Name here, only their ID.

cursor.execute("""
CREATE TABLE IF NOT EXISTS Goals (
    Goal_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Player_ID INTEGER,
    Opponent TEXT
)
""")

print("--- Goal Tracker Loaded ---")

# 2. Show the Roster so you know who is who
print("\nCurrent Roster:")
# rowid is a hidden ID number that SQLite creates automatically
cursor.execute("SELECT rowid, Name FROM Players")

for row in cursor.fetchall():
    print(f"ID: {row[0]} | Name: {row[1]}")

print("-----------------------")


while True:
    # 1. Ask for the ID (The Bridge)
    target_id = input("Enter Player ID to add a goal (or 'quit'): ")
    
    if target_id == "quit":
        break
        
    # 2. Ask for the detail
    opponent = input("Who was the opponent? ")
    
    # 3. Save the bridge (Player_ID) and the detail (Opponent)
    cursor.execute("INSERT INTO Goals (Player_ID, Opponent) VALUES (?,?)", (target_id, opponent))
    
    connection.commit()
    print("Goal Logged!")

print("--- Done ---")


print("\n--- GOAL REPORT ---")

# The Magic Query
# We are selecting the NAME from the Players table
# AND the OPPONENT from the Goals table.
# The 'JOIN' connects them where the IDs match.

query = """
SELECT Players.Name, Goals.Opponent 
FROM Goals
JOIN Players ON Goals.Player_ID = Players.rowid
"""

cursor.execute(query)

for row in cursor.fetchall():
    # row[0] is the Name, row[1] is the Opponent
    print(f"{row[0]} scored against {row[1]}")

connection.close()