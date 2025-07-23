import csv

# --- Define your classes ---
class Ride:
    def __init__(self, name, min_age, min_height, wait_time):
        self.name = name
        self.min_age = int(min_age)
        self.min_height = int(min_height)
        self.wait_time = int(wait_time)

class Guest:
    def __init__(self, name, age, height):
        self.name = name
        self.age = int(age)
        self.height = int(height)

# --- Load CSV files into lists of class objects ---

# Load rides
ride_objects = []
with open("service/ride-management-services/rides.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ride_objects.append(Ride(**row))
print(ride_objects)

# Load guests
guest_objects = []
with open("service/ride-management-services/guests.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        guest_objects.append(Guest(**row))
print(guest_objects)

# --- Use the objects ---
for guest in guest_objects:
    print(f"\nGuest: {guest.name} (Age: {guest.age}, Height: {guest.height})")
    for ride in ride_objects:
        if guest.age >= ride.min_age and guest.height >= ride.min_height:
            if ride.wait_time <= 15:
                print(f"  ✅ Can board {ride.name} now (Wait time: {ride.wait_time})")
            else:
                print(f"  ⏳ Eligible for {ride.name}, but wait time is {ride.wait_time} mins")
        else:
            print(f"  ❌ Not eligible for {ride.name}")