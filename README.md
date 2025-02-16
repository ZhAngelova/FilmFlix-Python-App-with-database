# FilmFlix Database Management System

## Overview
This is a simple **Python-based database management system** for handling a collection of films in an SQLite database (`filmflix.db`). The system allows users to **add, delete, update, and retrieve movie records** using an interactive **menu-driven interface**.

## Features
- **Add a film**: Insert a new movie record into the database.
- **Delete a film**: Remove a movie record based on its ID.
- **Update film details**: Modify existing records, either completely or by individual fields.
- **View films**:
  - View all films in the database.
  - Search films by **year of release**.
  - Search films by **rating**.
  - Search films by **genre**.

## Files and Modules
| File | Description |
|------|------------|
| `connect.py` | Establishes a connection to the SQLite database (`filmflix.db`). |
| `addFilm.py` | Allows users to insert new film records. |
| `deleteFilm.py` | Deletes a film record based on the film ID. |
| `updateFilm.py` | Updates an existing film record, either entirely or partially. |
| `readFilms.py` | Fetches and displays all film records from the database. |
| `reportFilm.py` | Allows users to search for films by **year released, rating, or genre**. |
| `allinone.py` | (Commented out) Previously used for filtering films by genre, year, or rating. |
| `dmenu.py` | Controls the **main menu** and the **report menu**, calling respective modules. |
| `dbMenu.txt` | Stores the text for the main menu displayed to users. |
| `filmflix.db` | The SQLite database file containing the `tblFilms` table. |

## How to Use
1. **Ensure Python is installed** on your system.
2. **Install SQLite3** if not already installed.
3. **Run the main menu script**:
   ```bash
   python dmenu.py
