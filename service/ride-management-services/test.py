# import json
# import os

# class RideManager:
#     def __init__ (self,rides_list):
#         self.rides = rides_list

# class GuestManager:
#     def __init__ (self,guests_list):
#         self.guests = guests_list
#         self.ticket_rides = []

#     def generate_eligibility_summary(self , ride_data: RideManager):
#         try:
#             assert not self.guests.age is None and not self.guests.height is None
#             for guest in self.guests:
#                 guest_id = guest["guest_id"]
#                 guest_name = guest["guest_name"]
#                 height = guest["height"]
#                 age = guest["age"]
                
#             if  >= ride_data.min_age and self.height >= ride_data.min_height:
#                 print(f"\n {self.guest_name} matches the {ride_data.min_age} and {ride_data.min_height} and is eligible to board the {ride_data.ride_name}")
#                 self.ticket_rides.append(ride_data.ride_id)
#             return self.ticket_rides 
#         except AssertionError as e:
#               print(f"age and height are mandatory parameters to board")  



# data = '''{

#   "rides": [
#     { "ride_id": "R001", "ride_name": "Sky Twister", "min_height": 120, "min_age": 8 },
#     { "ride_id": "R002", "ride_name": "Water Splash", "min_height": 100, "min_age": 5 },
#     { "ride_id": "R003", "ride_name": "Dragon Coaster", "min_height": 130, "min_age": 10 }
#   ],
#   "guests": [
#     { "guest_id": "G001", "guest_name": "Amy", "age": 9, "height": 125, "ticket_rides": ["R001", "R002"] },
#     { "guest_id": "G002", "guest_name": "Ben", "age": 6, "height": 105, "ticket_rides": ["R002", "R003"] },
#     { "guest_id": "G003", "guest_name": "Charlie", "age": 11, "height": 135, "ticket_rides": ["R001", "R003"] }
#   ]
# }
# '''

# def main():
#     ride_guest_data = [] 
#     ride_guest_data = json.loads(data)
#     rides_list = ride_guest_data["rides"]
#     guests_list = ride_guest_data["guests"]
#     print(rides_list)
#     print(guests_list)

#     ride_eligibility = RideManager(rides_list)
#     guest = GuestManager(guests_list)
#     guest.generate_eligibility_summary(ride_eligibility)

# main()

class RideEligibility(self , name, min_age, min_height):
    

rides = {
    "Roller Coaster": {"min_age": 12, "min_height": 140},
    "Bumper Cars": {"min_age": 5, "min_height": 100},
}

guests = {
    "Alice": {"age": 10, "height": 135},
    "Bob": {"age": 14, "height": 150},
    "Coco": {"age": 4, "height": 90}
}

ride_objects = [RideEligibility(name, r["min_age"], r["min_height"]) for name, r in rides.items()]

