class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


class Rider(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.boarded = False
        self.safety_gear = False

    def is_eligible(self):
        return self.age >= 12 and self.height >= 140

    def board(self, boarding_status, safety_gear_status):
        self.boarded = boarding_status.lower() == "boarded"
        self.safety_gear = safety_gear_status.lower() == "true"


class RideVerifier:
    def __init__(self, riders):
        self.riders = riders

    def process_riders(self):
        print("\n📋 Ride Eligibility Report:")
        for rider in self.riders:
            if rider.is_eligible():
                print(f"\n✅ {rider.name} is eligible based on age and height.")
                boarding_status = input(f"Has {rider.name} boarded? (boarded/not_boarded): ")
                safety_gear_status = input(f"Is safety gear worn by {rider.name}? (True/False): ")
                rider.board(boarding_status, safety_gear_status)

                if rider.boarded and rider.safety_gear:
                    print(f"🎢 {rider.name} is ready to enjoy the ride! ✅")
                elif rider.boarded and not rider.safety_gear:
                    print(f"⚠️ {rider.name} boarded but forgot safety gear. Please fix immediately.")
                else:
                    print(f"ℹ️ {rider.name} hasn’t boarded yet.")
            else:
                print(f"\n🚫 {rider.name} is NOT eligible (Age: {rider.age}, Height: {rider.height})")


# Sample data
riders_data = [
    {"name": "Alice", "age": 14, "height": 150},
    {"name": "Bob", "age": 11, "height": 145},
    {"name": "Charlie", "age": 13, "height": 135},
    {"name": "Dheera", "age": 20, "height": 160},
    {"name": "Elieana", "age": 7, "height": 112},
    {"name": "Fardeen", "age": 12, "height": 125}
]

# Create Rider objects
riders = [Rider(**data) for data in riders_data]

# Run Verifier
verifier = RideVerifier(riders)
verifier.process_riders()