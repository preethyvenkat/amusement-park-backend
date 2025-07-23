class RideEligibility:
    def __init__ (self,ride_id,min_age,height):
            self.ride_id = ride_id
            self.min_age = min_age
            self.height = height
        
class GuestEligibility:
    def __init__ (self,guest_name,age,height):
        self.guest_name = guest_name
        self.age = age
        self.height = height

    def is_eligible_guests(self, ride: RideEligibility ):
        return  self.age >= ride.min_age and self.height >= ride.height
              

def create_ride_details():
    print("\n enter the ride details:")
    return RideEligibility(
        int(input("ride_id: ")),
        int(input("min_age for ride: ")),
        int(input("min height for the ride: "))
    )

def main():
    ride = create_ride_details()
    
    riders = [{"name": "Alice", "age": 14, "height": 150},
    {"name": "Bob", "age": 11, "height": 145},
    {"name": "Dheera", "age": 20, "height": 160}]

    eligible_names = []
    for rider in riders:
       guest = GuestEligibility(rider["name"], rider["age"], rider["height"])
       if guest.is_eligible_guests(ride):
            eligible_names.append(guest.guest_name)
    print(f"\nNames eligible for ride: {eligible_names}\n")


if __name__ == "__main__":
    main()


# step1 : defining a  class RideEligibility , its a blue print to create objects like 
# ride = RideEligibility(inputs or attributes)


# step 2 : __init__ is constrcutor method , it runs when you do any action on RideEligibility
# assigns value to the object you create