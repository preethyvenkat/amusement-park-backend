# store medical information of the guest and family of the guest to access ride eligibility
class GuestMedicalProfile:
    def __init__(self, guest_id, guest_name):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.family_members = []  

    def add_family_member(self, name, relation,age,height, condition, on_medication, emergency_contact, eligible_for_rides):
            # request validation 
            assert isinstance(name, str), "Name must be a string"
            assert int(age) > 0, "Age must be positive"
            assert int(height) > 0,"Height must be in cms"

             # ✅ Determine eligibility
            eligible = True
            if condition.strip().lower() == "yes" or int(height) < 111:
                eligible = False
                print("⚠️ The guest has a medical condition or doesn't meet the height requirement and cannot take the ride.")

            self.family_members.append({
                "name": name,
                "relation": relation,
                "age": age,
                "height": height,
                "condition": condition,
                "on_medication": on_medication,
                "emergency_contact": emergency_contact,
                "eligible_for_rides": eligible
            })
            return self.family_members
      
    def get_all_family_info(self):
        return self.family_members
   
   
# === Main Flow ===
guest_id = input("Enter your Guest ID: ")
guest_name = input("Enter your Name: ")

#create objects
medical_records = GuestMedicalProfile(guest_id , guest_name)

family_count = int(input("How many family members to add? "))
   
for i in range(family_count): 
    print(f"\n--- Entering details for family member #{i+1} ---")
    name = input("Name: ")
    relation = input("Relation to guest:")
    age  = input("Age:")
    height = input("Enter your height (in cms):")
    condition = input("Any medical conditions? ")
    on_medication = input("Are you currently on medication? (yes/no): ")
    emergency_contact =  input("Emergency contact number: ")

    # Add to profile
    medical_records.add_family_member(name,relation, age,height,condition, on_medication, emergency_contact)



print("\n✅ All family medical records saved!\n")

# Display stored info (optional)
for member in medical_records.get_all_family_info():
    print(f"👨‍👩‍👧‍👦 {member['name']} ({member['relation']}), Age: {member['age']},height: {member['height']}, Condition: {member['condition']}, Medication: {member['on_medication']}, Emergency Contact: {member['emergency_contact']}")