import os
import json
import time

# Blueprint for ride eligibility
class RideCriteria:
    def __init__(self, ride_id, ride_name, min_age, min_height, medical_condition, duration_min, max_capacity, ride_status, location_zone):
        self.ride_id = ride_id
        self.ride_name = ride_name
        self.min_age = min_age
        self.min_height = min_height
        self.medical_condition = medical_condition
        self.duration_min = duration_min
        self.max_capacity = max_capacity
        self.ride_status = ride_status
        self.location_zone = location_zone

# Guest Eligibility Checker
class GuestCriteria:
    def __init__(self, guest_id, name, age, height, medical_condition):
        try:
            assert 7 <= int(age) <= 55, "Age must be between 7 and 55"
        except AssertionError as e:
            print(f"❌ Error: {e}")
        self.guest_id = guest_id
        self.name = name
        self.age = int(age)
        self.height = int(height)
        self.medical_condition = medical_condition
        self.selected_rides = []

    def add_ride_selection(self, ride: RideCriteria):
        if (self.age >= ride.min_age and self.height >= ride.min_height) and self.medical_condition == ride.medical_condition:
            self.selected_rides.append(ride.ride_name)
            print(f"\n{self.name} successfully selected ride: {ride.ride_name}\n")
        else:
            print(f"\n{self.name} is NOT eligible for ride: {ride.ride_name}\n")

# Class to verify safety gear and boarding status
class BoardingStatusVerifier:
    def __init__(self, guest: GuestCriteria):
        self.guest = guest

    def check_safety_gear(self, boarding_status, is_safety_gear_worn):
        try:
            assert boarding_status is not None, "Boarding status cannot be None"
            assert is_safety_gear_worn is not None, "Safety gear status cannot be None"
            boarding_status = boarding_status.lower()
            is_gear_worn = str(is_safety_gear_worn).strip().lower() == 'true'

            if boarding_status == "boarded" and is_gear_worn:
                print(f"\n✅ {self.guest.name} has boarded and worn the safety harness. Ready for ride!\n")
            elif boarding_status == "boarded" and not is_gear_worn:
                print(f"\n⚠️ {self.guest.name} has boarded but hasn't worn the safety harness. Please wear it immediately.\n")
            elif boarding_status == "not_boarded":
                print(f"\nℹ️ Guest {self.guest.name} is eligible but has not boarded yet.\n")
        except AssertionError as e:
            print(f"❌ Error: {e}")
        return boarding_status, is_safety_gear_worn
    

# Helper methods to create objects
def create_ride_from_input():
    print("\n🎢 Enter Ride Details:")
    return RideCriteria(
        input("Ride ID: "),
        input("Ride Name: "),
        int(input("Minimum Age: ")),
        int(input("Minimum Height (cm): ")),
        input("Medical Condition (yes/no): "),
        int(input("Duration (min): ")),
        int(input("Max Capacity: ")),
        input("Ride Status (Open/Close): "),
        input("Location Zone (A/B/C): ")
    )

def create_guest_from_input():
    print("\n🧑 Enter Guest Details:")
    return GuestCriteria(
        input("Guest ID: "),
        input("Name: "),
        int(input("Age: ")),
        int(input("Height (cm): ")),
        input("Medical Condition (yes/no): ")
    )

# extract some return from values from rideCriteria, GuestCriteria and boardingstatusverifier
# and store them as dict and dump them to json file.

def create_ride_eligibility_tracker_json(ride_id,ride_name,guest_id,guest_name,boarding_status,safety_gear):
    status = {
        "ride_id": ride_id,
        "ride_name": ride_name,
        "guest_id": guest_id,
        "guest_name": guest_name,  
        "boarding_status": boarding_status,
        "safety_gear": safety_gear    
    }
    file_path = "service/ride-management-services/"
    with open("ride_eligibility_tracke.json", "w") as json_file:
        json.dump(status, json_file, indent=4)
        print("\nride_eligibility_tracker.json created successfully.\n")

# === Main Execution ===
def main():
    ride = create_ride_from_input()
    guest = create_guest_from_input()
    guest.add_ride_selection(ride)

    if guest.selected_rides:
        print(f"\n{guest.name}, you are eligible for: {guest.selected_rides}")
        print("\n ✅ Please board the ride and wear your safety harness.\n")

        boarding_status = input("\n📋 Staff: Confirm if the guest has boarded (boarded/not_boarded): \n")
        is_safety_gear_worn = input("\n🪢 Staff: Is safety harness worn? (True/False): \n")

        verifier = BoardingStatusVerifier(guest)
        boarding_status , is_gear_worn = verifier.check_safety_gear(boarding_status, is_safety_gear_worn)
        print("\nstatus check {} and {}\n".format(boarding_status , is_safety_gear_worn))
        create_ride_eligibility_tracker_json(ride.ride_id,ride.ride_name,guest.guest_id,guest.name,boarding_status,is_gear_worn)    

    else:
        print(f"\n🚫 Sorry {guest.name}, you're not eligible for this ride. Please try another.\n")



if __name__ == "__main__":
    main()