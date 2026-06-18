from config import FLOORS, TOTAL_SLOTS_PER_FLOOR

occupied_slots = {
    floor: [] for floor in range(1, FLOORS + 1)
}

def assign_slot():

    for floor in range(1, FLOORS + 1):

        for slot in range(1, TOTAL_SLOTS_PER_FLOOR + 1):

            if slot not in occupied_slots[floor]:

                occupied_slots[floor].append(slot)

                return floor, slot

    return None, None


def release_slot(floor, slot):

    if slot in occupied_slots[floor]:

        occupied_slots[floor].remove(slot)


def available_slots():

    total = FLOORS * TOTAL_SLOTS_PER_FLOOR

    occupied = sum(
        len(v)
        for v in occupied_slots.values()
    )

    return total - occupied


def occupied_count():

    return sum(
        len(v)
        for v in occupied_slots.values()
    )