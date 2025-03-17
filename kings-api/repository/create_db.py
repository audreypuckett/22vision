import sqlite3

def connect_db():
    """Connects to SQLite database and returns connection."""
    return sqlite3.connect("kings.db")

def create_tables():
    """Drops existing tables and creates new ones in the database."""
    conn = connect_db()
    cursor = conn.cursor()

    # Drop tables if they exist (to start fresh)
    cursor.executescript("""
        DROP TABLE IF EXISTS alternative_names;
        DROP TABLE IF EXISTS highlights;
        DROP TABLE IF EXISTS kings;
        DROP TABLE IF EXISTS persons;
    """)

    # Create Persons table (stores both Kings and non-Kings, e.g., mothers)
    cursor.execute("""
        CREATE TABLE persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT
        )
    """)

    # Create Kings table (person_id is also the primary key)
    cursor.execute("""
        CREATE TABLE kings (
            id INTEGER PRIMARY KEY REFERENCES persons(id) ON DELETE CASCADE,
            reign_start TEXT NOT NULL,
            reign_end TEXT,
            age_kinged INTEGER NOT NULL,
            years_reigned INTEGER NOT NULL,
            months_reigned INTEGER DEFAULT 0,
            kingship TEXT NOT NULL CHECK(kingship IN ('United', 'Judah', 'Israel')),
            gods_eyes TEXT NOT NULL CHECK(gods_eyes IN ('Did Right', 'Did NOT Do Right', 'Did Evil')),
            father_id INTEGER REFERENCES persons(id),
            mother_id INTEGER REFERENCES persons(id),
            predecessor_id INTEGER REFERENCES kings(id)
        )
    """)

    # Create Highlights table (linked to Person)
    cursor.execute("""
        CREATE TABLE highlights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note TEXT NOT NULL,
            book TEXT NOT NULL,
            chapter INTEGER NOT NULL,
            verse TEXT NOT NULL,
            person_id INTEGER NOT NULL REFERENCES persons(id) ON DELETE CASCADE
        )
    """)

    # Create Alternative Names table (linked to Person)
    cursor.execute("""
        CREATE TABLE alternative_names (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            person_id INTEGER NOT NULL REFERENCES persons(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()

# Run this to ensure tables exist
create_tables()