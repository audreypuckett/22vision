from model.King import King
import sqlite3

def insert_king(king: King):
    """Inserts a King into the database and returns its ID."""
    conn = sqlite3.connect("kings.db")
    cursor = conn.cursor()

    # Step 1: Insert into persons table
    cursor.execute("""
        INSERT INTO persons (name, role)
        VALUES (?, ?)
    """, (king.get_name(), "King"))

    king_id = cursor.lastrowid  # Get the inserted person ID

    # Step 2: Insert into kings table using the same person_id
    cursor.execute("""
        INSERT INTO kings (id, reign_start, reign_end, age_kinged, years_reigned, months_reigned, kingship, gods_eyes, father_id, mother_id, predecessor_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        king_id,
        king.reign_start,
        king.reign_end,
        king.age_kinged,
        king.years_reigned,
        king.months_reigned,
        king.kingship.value,
        king.get_gods_eyes().value,
        None,  # Father ID (can be updated later)
        None,  # Mother ID (if available)
        None   # Predecessor ID (if known)
    ))

    # Insert alternative names
    for alt_name in king.get_alt_names():
        cursor.execute("""
            INSERT INTO alternative_names (name, person_id)
            VALUES (?, ?)
        """, (alt_name, king_id))

    # Insert highlights
    for highlight in king.get_highlights():
        cursor.execute("""
            INSERT INTO highlights (note, book, chapter, verse, person_id)
            VALUES (?, ?, ?, ?, ?)
        """, (
            highlight.get_note(),
            highlight.get_book().value,
            highlight.get_chapter(),
            highlight.get_verse(),
            king_id
        ))

    conn.commit()
    conn.close()
    return king_id


def get_all_kings():
    """Fetch all kings from the database."""
    conn = sqlite3.connect("kings.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT k.id, k.name, k.reign_start, k.reign_end, k.kingship, k.gods_eyes
        FROM kings k
    """)

    kings = cursor.fetchall()
    conn.close()
    return kings