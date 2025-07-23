# from array import array

# # Guest ages array
# guest_ages = array('i', [24, 19, 32, 28, 21])

# ages = guest_ages.tolist()

# print("Original guest ages:", guest_ages.tolist())

# # Length of array
# n = len(guest_ages)

# for i in range(n):
#     for j in range(i+1,n):
#         if ages[i] > ages[j]:
#             ages[i] , ages[j] = ages[j] , ages[i]
# print(ages)

# guest_updated_ages = array( "i" ,ages)
# print(guest_updated_ages)


rides = [
    ("Haunted House", "R007"),
    ("Ferris Wheel", "R023"),
    ("Roller Coaster", "R015"),
    ("Bumper Cars", "R009"),
    ("Drop Tower", "R021"),
    ("Log Flume", "R003"),
    ("Swinging Ship", "R017"),
    ("Pirate Ride", "R002"),
    ("Carousel", "R005"),
    ("Wild Mouse Coaster", "R019")
]

# take the name of the rides and create prefix name and store in a list
message_id = []
n = len(rides)
for i in range(n):
    ride_name = rides[i][0]
    ride_id = rides[i][1]
    word = ride_name.split()
    ride_name_prefix = "".join(word[0].upper()for word in word if word)
    message = "".join([ride_name_prefix, "-", ride_id])
    message_id.append(message)         

for msg in message_id:
    print(f"{msg} is retrieved by ride_launch_services which validates ride_safety for the guest boarded!")


