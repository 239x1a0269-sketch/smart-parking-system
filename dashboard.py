from parking_manager import (
    available_slots,
    occupied_count
)

from config import (
    FLOORS,
    TOTAL_SLOTS_PER_FLOOR
)

def get_dashboard_data():

    total = FLOORS * TOTAL_SLOTS_PER_FLOOR

    return {

        "total": total,

        "available": available_slots(),

        "occupied": occupied_count()

    }