import os
import json
from datetime import datetime

class RideAlert:
    def __init__ (self,ride_alert_info):
        try:
            assert not ride_alert_info is None , "Ride data are fetched"
            self.ride_alert_info = ride_alert_info
        except AssertionError as e:
            print("Error")

    def sort_ride_data_by_name(self):
        n = len(self.ride_alert_info)
        for i in range(n):
            for j in range(i+1 , n):
                if self.ride_alert_info[i]["guest_name"] > self.ride_alert_info[j]["guest_name"]:
                    self.ride_alert_info[i],self.ride_alert_info[j] = self.ride_alert_info[j],self.ride_alert_info[i]
        #print(f"\n \n The ride data is sorted by name in alphabetical order {self.ride_alert_info} \n ")
  

    
    def send_ride_alerts(self):
        for alert in self.ride_alert_info:
            guest = alert["guest_name"]
            ride = alert["ride_name"]
            time = alert["launch_time"]
            status = alert["status"]
            message = alert["message"]
            #print(f"\n \n Hello {guest},{ride}  is {status}, {message}\n\n ")

    def send_slack_message(self):
        for alert in self.ride_alert_info:
            slack_message = {
                "channel": "#ride-alerts",
                "text": f"* Ride Alert * Guest: {alert['guest_name']} Ride: {alert['ride_name']} Status: {alert['status']} Message: {alert['message']} Time: {alert['launch_time']}"
            }
            print(f"\n📤 Simulated Slack Message:\n{json.dumps(slack_message, indent=2)}\n")
       

# Helper Function

def get_ride_info_from_file():
    ride_alert_data = {}
    file_path = "service/ride-management-services/ride-alert.json"
    with open(file_path, "r") as json_file:
        ride_alert_data = json.load(json_file)
    return ride_alert_data


def mask_guest_number(ride_alert_info, index):
    guest_phone = ride_alert_info[index]["guest_phone"]
    masked = "*" * (len(guest_phone) - 4) + guest_phone[-4:]
    #print(f"Masked number for {ride_alert_info[index]['guest_name']}: {masked}")

    

def main():
    ride_alert_info = get_ride_info_from_file()
    
    send_alert =  RideAlert(ride_alert_info)
    send_alert.send_ride_alerts()
    send_alert.sort_ride_data_by_name()
    send_alert.send_slack_message()
    mask_guest_number(ride_alert_info, 4)

if __name__ == "__main__":
    main()
    
    