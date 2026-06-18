import sqlite3

conn = sqlite3.connect("parking.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS vehicles(
    vehicle_no TEXT,
    floor INTEGER,
    slot TEXT,
    entry_time TEXT
)
""")

conn.commit()


def add_vehicle(vehicle_no, floor, slot, entry_time):

    cur.execute(
        "INSERT INTO vehicles VALUES (?, ?, ?, ?)",
        (vehicle_no, floor, slot, entry_time)
    )

    conn.commit()


def remove_vehicle(vehicle_no):

    cur.execute(
        "DELETE FROM vehicles WHERE vehicle_no=?",
        (vehicle_no,)
    )

    conn.commit()


def get_vehicle(vehicle_no):

    cur.execute(
        "SELECT * FROM vehicles WHERE vehicle_no=?",
        (vehicle_no,)
    )

    return cur.fetchone()


def count_vehicles():

    cur.execute(
        "SELECT COUNT(*) FROM vehicles"
    )

    return cur.fetchone()[0]


def get_all_vehicles():

    cur.execute(
        "SELECT * FROM vehicles"
    )

    return cur.fetchall()