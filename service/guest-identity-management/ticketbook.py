import os
from datetime import datetime
import uuid

class TicketBooking:
    def __init__(self, guest_name, ride_name, price):
        self.guest_name = guest_name
        self.ride_name = ride_name
        self.price = price
        self.ticket_id = str(uuid.uuid4())[:8]
        self.timestamp = datetime.now().isoformat()
        self.guest_booking_history = []

    def confirm_booking(self):
        print(f"\n✅ Booking Confirmed!")
        print(f"Guest: {self.guest_name}")
        print(f"Ride: {self.ride_name}")
        print(f"Price: ${self.price}")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Time: {self.timestamp}\n")

        booking_record = {
            "guest_name": self.guest_name,
            "ride_name": self.ride_name,
            "price": self.price,
            "ticket_id": self.ticket_id,
            "timestamp": self.timestamp
        }

        self.guest_booking_history.append(booking_record)
        return booking_record  # optional return


def get_ride_price():
    guest_name = input("Enter Guest Name: ")
    ride_name = input("Enter Ride Name: ")
    price = int(input("Enter Price: $"))
    return TicketBooking(guest_name, ride_name, price)  # <- correct order


def main():
    all_bookings = []

    while True:
        answer = input("\nDo you want to book a ticket? (yes/no): ").strip().lower()
        if answer == "no":
            break

        booking = get_ride_price()
        booking.confirm_booking()
        all_bookings.append(booking)

    print(f"\n🎟️ Total Bookings: {len(all_bookings)}")
    for i, b in enumerate(all_bookings, 1):
        print(f"{i}. {b.guest_name} → {b.ride_name} (${b.price}) | Ticket ID: {b.ticket_id}")

if __name__ == "__main__":
    main()