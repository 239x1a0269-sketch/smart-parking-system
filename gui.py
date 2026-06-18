import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from database import (
    add_vehicle,
    remove_vehicle,
    search_vehicle,
    get_all_vehicles,
    vehicle_count
)

from parking_manager import (
    assign_slot,
    release_slot,
    available_slots,
    occupied_count
)

from dashboard import get_dashboard_data


class ParkingGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("Advanced Smart Parking System")

        self.root.geometry("900x700")

        self.root.configure(bg="#1e1e2f")

        title = tk.Label(
            root,
            text="ADVANCED SMART PARKING SYSTEM",
            font=("Arial", 20, "bold"),
            fg="cyan",
            bg="#1e1e2f"
        )

        title.pack(pady=10)

        self.vehicle_entry = tk.Entry(
            root,
            font=("Arial", 14),
            width=30
        )

        self.vehicle_entry.pack(pady=10)

        tk.Button(
            root,
            text="Park Vehicle",
            command=self.park_vehicle,
            bg="green",
            fg="white"
        ).pack(pady=5)

        tk.Button(
            root,
            text="Exit Vehicle",
            command=self.exit_vehicle,
            bg="red",
            fg="white"
        ).pack(pady=5)

        tk.Button(
            root,
            text="Search Vehicle",
            command=self.search_vehicle
        ).pack(pady=5)

        tk.Button(
            root,
            text="Show History",
            command=self.show_history
        ).pack(pady=5)

        self.status = tk.Label(
            root,
            text="System Ready",
            fg="yellow",
            bg="#1e1e2f",
            font=("Arial", 12)
        )

        self.status.pack(pady=10)

        self.dashboard = tk.Label(
            root,
            text="",
            bg="#1e1e2f",
            fg="white",
            font=("Arial", 12)
        )

        self.dashboard.pack(pady=20)

        self.update_dashboard()

    def update_dashboard(self):

        data = get_dashboard_data()

        self.dashboard.config(
            text=
            f"Total Slots : {data['total']}\n"
            f"Available Slots : {data['available']}\n"
            f"Occupied Slots : {data['occupied']}\n"
            f"Vehicles Parked : {vehicle_count()}"
        )

    def park_vehicle(self):

        vehicle = self.vehicle_entry.get().strip()

        if vehicle == "":
            messagebox.showerror(
                "Error",
                "Enter Vehicle Number"
            )
            return

        floor, slot = assign_slot()

        if floor is None:
            messagebox.showerror(
                "Parking Full",
                "No Slots Available"
            )
            return

        entry_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        add_vehicle(
            vehicle,
            floor,
            slot,
            entry_time
        )

        self.status.config(
            text=f"{vehicle} -> Floor {floor} Slot {slot}"
        )

        self.update_dashboard()

    def exit_vehicle(self):

        vehicle = self.vehicle_entry.get().strip()

        data = search_vehicle(vehicle)

        if not data:
            messagebox.showerror(
                "Error",
                "Vehicle Not Found"
            )
            return

        floor = data[1]
        slot = int(data[2])

        release_slot(
            floor,
            slot
        )

        remove_vehicle(vehicle)

        self.status.config(
            text=f"{vehicle} Exited"
        )

        self.update_dashboard()

    def search_vehicle(self):

        vehicle = self.vehicle_entry.get().strip()

        data = search_vehicle(vehicle)

        if data:

            messagebox.showinfo(
                "Vehicle Found",
                f"Vehicle : {data[0]}\n"
                f"Floor : {data[1]}\n"
                f"Slot : {data[2]}\n"
                f"Entry : {data[3]}"
            )

        else:

            messagebox.showerror(
                "Not Found",
                "Vehicle Not Found"
            )

    def show_history(self):

        history = get_all_vehicles()

        text = ""

        for row in history:

            text += (
                f"{row[0]} | "
                f"Floor {row[1]} | "
                f"Slot {row[2]}\n"
            )

        if text == "":
            text = "No Vehicles"

        messagebox.showinfo(
            "Parking History",
            text
        )