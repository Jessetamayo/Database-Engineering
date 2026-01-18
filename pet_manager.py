import sqlite3

# 1. CONNECT TO DATABASE
connection = sqlite3.connect("pethotel.db")
cursor = connection.cursor()

# 2. RESET THE TABLE (So we start fresh)
cursor.execute("DROP TABLE IF EXISTS Pets")

# 3. CREATE THE TABLE
cursor.execute("""
CREATE TABLE Pets (
    PetID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Type TEXT,
    Weight REAL
);
""")

print("--- Welcome to Pet Hotel ---")

# 4. ASK YOU FOR INPUT
# This input happens in the Terminal, but the CODE lives in the file.
new_name = input("Enter the pet's name: ")
new_type = input("Enter the pet's type (Dog/Cat): ")
new_weight = float(input("Enter the pet's weight: "))

# 5. INSERT THE DATA
insert_query = "INSERT INTO Pets (Name, Type, Weight) VALUES (?, ?, ?)"
cursor.execute(insert_query, (new_name, new_type, new_weight))

print(f"\n--- Success! {new_name} has been checked in. ---")

# 6. SAVE AND SHOW RESULTS
connection.commit()

cursor.execute("SELECT * FROM Pets")
all_pets = cursor.fetchall()

print("\n--- Current Guest List ---")
for pet in all_pets:
    print(pet)

connection.close()