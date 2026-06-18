# Parking Configuration

ROWS = 10
COLS = 10

FLOORS = 3

TOTAL_SLOTS_PER_FLOOR = 20

PARKING_SLOTS = {
    1: [(i, j) for i in range(2, 6) for j in range(2, 7)],
    2: [(i, j) for i in range(2, 6) for j in range(2, 7)],
    3: [(i, j) for i in range(2, 6) for j in range(2, 7)]
}

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

CELL_SIZE = 50

DB_NAME = "parking.db"

ENTRY_POINT = (0, 0)

PARKING_FEE_PER_HOUR = 20