# Authenticates an existing guest
class LoginGuest:
    def __init__(self,guest_id,password):
        self.guest_id = guest_id.strip().lower()
        self.password = password
    def getUser(self):
        return self.guest_id
    def getPwd(self):
        return self.password
    
    def validate(self, guest_db):
        if self.guest_id in guest_db:
            if self.password == guest_db[self.guest_id]["password"]:
                return True
        return False
    
    def get_guest_profile(self, guest_db):
        return guest_db.get(self.guest_id, {})

guest_db = {
    "jumbolove": {"password": "secure123", "name": "Seline"},
}  

print(f"\n Welcome back!, Please log in\n")
guest_id = input("Enter a username: ").strip().lower()
password = input("\n Enter password:").strip().lower()

# CREATING THE OBJECT   
loginGuest = LoginGuest(guest_id,password)

# ✅ Validate login
if loginGuest.validate(guest_db):
    profile = loginGuest.get_guest_profile(guest_db)
    print(f"\n✅ Hello {profile['name']}! Login successful.")
    print("\n Welcome back! You can access your profile page to edit details.\n")
else:
    print("\n❌ Login failed. Please check your credentials.\n")





