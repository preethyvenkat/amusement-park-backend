# Handles new user registration
class SignupGuest:
    def __init__(self,signup_mode,guest_id,password):
        self.signup_mode = signup_mode
        self.guest_id = guest_id
        self.password = password
        
    def getMode(self):
        return self.signup_mode
    def getUser(self):
        return self.guest_id
    def getPwd(self):
        return self.password

# Ask how the user wants to sign up  
mode_choice = input ("Do you want to signup using \n1.Google \n2.Facebook \n3.Apple \n4.Email ID \nEnter your choice:").strip()

if mode_choice == '1':
    signup_mode = "Google"
    print("Redirecting to Google... Please approve.")
elif mode_choice == '2':
    signup_mode = "Facebook"
    print("Redirecting to Facebook... Please approve.")
elif mode_choice == '3':
    signup_mode = "Apple"
    print("redirecting to Apple.....Please approve.")
elif mode_choice == '4':
    signup_mode = "Email"
    print("You chose Email. Please enter details to register.")

    # 📥 Ask for user credentials
    guest_id = input("Enter a username: ").strip().lower()
    password = input("enter password:")

    # CREATING THE OBJECT   
    guestSignup = SignupGuest(signup_mode,guest_id,password)

     # ✅ Output confirmation
    print(f"\nHello {guestSignup.getUser()}! Thank you for signing up via {guestSignup.getMode()}.")
    print("Kindly login and access profile page to edit details.")
else:
    print("❌ Invalid option. Please signup and register to proceed.")


