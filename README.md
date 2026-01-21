# Soccer Academy Manager (CLI)

## Project Overview
A command-line interface (CLI) tool designed to manage sports academy rosters and performance statistics. This project demonstrates the integration of Python logic with a relational database (SQLite) to perform full CRUD operations, data aggregation, and automated reporting.

## Key Features
* **Roster Management:** Add new players with specific positions to a persistent database.
* **Relational Data Modeling:** Tracks player goals in a separate table linked via Foreign Keys (1-to-many relationship).
* **Data Analysis:** Automatically generates "Pivot Table" style reports (e.g., counting players by position) using SQL aggregation.
* **Advanced Querying:** specific filtering capabilities (e.g., finding all "Midfielders" using wildcard `LIKE` operators).
* **Excel Integration:** Exports the full roster to a `.csv` file for external analysis in Microsoft Excel or Google Sheets.

## Technologies Used
* **Language:** Python 3.x
* **Database:** SQLite3
* **Libraries:** `sqlite3`, `csv`

## How to Run
1.  Clone this repository.
2.  Run the roster manager:
    ```bash
    python soccer_tracker.py
    ```
3.  Run the stats tracker:
    ```bash
    python goal_tracker.py
    ```
4.  Check the desktop for the generated `roster_export.csv` file.

## Code Highlight (SQL Join)
The project utilizes SQL Joins to dynamically link player identities with match performance:

```python
SELECT Players.Name, Goals.Opponent 
FROM Goals
JOIN Players ON Goals.Player_ID = Players.rowid