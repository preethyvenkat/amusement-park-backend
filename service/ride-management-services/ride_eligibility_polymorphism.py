class RideEligibility:
    def __init__(self, name, min_age, min_height):
        self.name = name
        self.min_age = min_age
        self.min_height = min_height

    def check_eligibility(self, guest):
        if guest.age >= self.min_age and guest.height >= self.min_height:
            print(f"{guest.name} is eligible for {self.name}")
        else:
            print(f"{guest.name} is NOT eligible for {self.name}")


class GuestEligibility:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def check_eligibility(self, ride):
        if self.age >= ride.min_age and self.height >= ride.min_height:
            print(f"{self.name} is eligible for {ride.name}")
        else:
            print(f"{self.name} is NOT eligible for {ride.name}")


# Data setup
rides = {
    "Roller Coaster": {"min_age": 12, "min_height": 140},
    "Bumper Cars": {"min_age": 5, "min_height": 100},
}

guests = {
    "Alice": {"age": 10, "height": 135},
    "Bob": {"age": 14, "height": 150},
    "Coco": {"age": 4, "height": 90}
}

# Create objects
ride_objects = [RideEligibility(name, r["min_age"], r["min_height"]) for name, r in rides.items()]
guest_objects = [GuestEligibility(name, g["age"], g["height"]) for name, g in guests.items()]

# Check eligibility using polymorphism (Ride checks Guest)
print("\n[ Ride checks Guest ]")
for ride in ride_objects:
    for guest in guest_objects:
        ride.check_eligibility(guest)

# Check eligibility using polymorphism (Guest checks Ride)
print("\n[ Guest checks Ride ]")
for guest in guest_objects:
    for ride in ride_objects:
        guest.check_eligibility(ride)