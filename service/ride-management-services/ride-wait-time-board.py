class Ride:
    def __init__(self, name, min_age, min_height, wait_time):
        self.name = name
        self.min_age = min_age
        self.min_height = min_height
        self.wait_time = wait_time


class Guest:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def check_rides(self, rides):
        print(f"\nChecking rides for {self.name} (Age: {self.age}, Height: {self.height}cm)")

        for ride in rides:
            print(f"\n🔍 Ride: {ride.name} (Wait time: {ride.wait_time} mins)")

            if self.age >= ride.min_age and self.height >= ride.min_height:
                if ride.wait_time <= 15:
                    print(f"✅ {self.name} can board '{ride.name}' now! 🚨 Alert: Go to the ride!")
                else:
                    print(f"🕒 {self.name} is eligible, but must wait ({ride.wait_time} mins).")
            else:
                reasons = []
                if self.age < ride.min_age:
                    reasons.append(f"needs to be at least {ride.min_age} years old")
                if self.height < ride.min_height:
                    reasons.append(f"needs to be at least {ride.min_height} cm tall")
                reason_text = " and ".join(reasons)
                print(f"❌ Not eligible for '{ride.name}': {reason_text}")


# ---------- Sample Data ----------

rides = [
    Ride("Roller Coaster", min_age=12, min_height=140, wait_time=20),
    Ride("Bumper Cars", min_age=5, min_height=100, wait_time=10),
    Ride("Ferris Wheel", min_age=3, min_height=90, wait_time=5)
]

guests = [
    Guest("Alice", age=10, height=135),
    Guest("Bob", age=14, height=150),
    Guest("Coco", age=4, height=95)
]

# ---------- Run Checks ----------

for guest in guests:
    guest.check_rides(rides)