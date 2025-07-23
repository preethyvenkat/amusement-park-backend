class GuestDirections:   
   def __init__ (self, guest_name,guest_live_location): 
      self.guest_name = guest_name
      self.guest_live_location = guest_live_location

class ParkMap:
    def __init__ (self,location_name,cords,zone_name ):
        self.location_name =  location_name
        self.cords = cords
        self.zone_name =  zone_name

    def get_directions(self , guest_access: GuestDirections):
        if self.location_name == guest_access.guest_live_location:
            print(f"please check cordinates {self.cords} and {self.zone_name}")
            return self.zone_name
        elif self.location_name == guest_access.guest_live_location:
            print(f"please check cordinates {self.cords} and {self.zone_name}")
            return self.zone_name
        elif self.location_name == guest_access.guest_live_location:
            print(f"please check cordinates {self.cords} and {self.zone_name}")
            return self.zone_name


def create_guest_input():
    return GuestDirections(
       input("guest_name: "),
       input("guest_location: ")
    )

def main ():
    
    zones = (("Entrance", (1, 3), "Zone-A"),
        ("Roller Coaster", (2, 5), "Zone-B"),
        ("Haunted House", (5, 8), "Zone-C"),
        ("RestRoom", (1, 4), "Zone-A"),
        ("Restaurants",(4, 7), "Zone-C"),
        ("Shops",(3, 5), "Zone-B"))
    
    input_guest_location = create_guest_input()
    for zone in zones:
        navigation = ParkMap(*zone)
        zone_result = navigation.get_directions(input_guest_location)
        if zone_result:  # store only if matched
            matched_zone_name = zone_result
            if matched_zone_name:
                print(f"\n✅ {input_guest_location.guest_name} requested directions for Zone: {matched_zone_name}")
            else:
                print(f"\n❌ Location '{input_guest_location.guest_live_location}' not found in park zones.")
   
    

if __name__ == "__main__":
    main()