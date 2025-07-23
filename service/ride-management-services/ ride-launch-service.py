import os
import json
import uuid
from datetime import datetime

class RideLaunch:
    def __init__ (self,ride_status):
        self.seen_ids = set()
        try:
            assert not  ride_status is None,"Message not empty"
            self.ride_status = ride_status
        except AssertionError as e:
            print("Error")

    def is_duplicate(self):
        if self.ride_status["deduplication_id"] in  self.seen_ids:
            print(f"{self.ride_status['message_group_id']} is recieved multiple times, check DLQ for failure!")
            return True
        else:
            self.seen_ids.add(self.ride_status["deduplication_id"])
            print(f"{self.ride_status['message_group_id']} is recieved and {self.ride_status['ride_name']} can now launch safely ✅  ")
            return False
       
def read_from_file (ride_boarding_status):
    ride_boarding_status = {}
    file_path = "service/ride-management-services/ride_eligibility_tracke.json"
    with open(file_path, "r") as json_file:
        ride_boarding_status  = json.load(json_file)
    return ride_boarding_status

def main():

    # extract output from file polled by message queue
    ride_status = read_from_file({})  
    ride_name = ride_status.get("ride_name", "")
    ride_id = ride_status.get("ride_id", "")
    ride_name_prefix = "".join(word[0].upper() for word in ride_name.split() if word)

    # append new message to the list
    ride_status["message_group_id"] = f"{ride_name_prefix}-{ride_id}"
    print(ride_status["message_group_id"])
    ride_status["deduplication_id"] = str(uuid.uuid4())
    ride_status["timestamp"] = datetime.now().isoformat()

   # object created  
    ride = RideLaunch(ride_status)
    ride.is_duplicate()
   
main()
