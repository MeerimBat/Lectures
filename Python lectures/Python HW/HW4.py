bill_amount = float(input("enter the amount: $"))
tip_percentage = float(input("Enter the tip percentage: "))
tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount
print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total bill (including tip): ${total_bill:.2f}")

num_people= int(input("How many people are splitting the bill? "))
names = []
for i in range(num_people):
        name = input(f"Enter the name of person {i + 1}: ")
        names.append(name)
    
amount_per_person = total_bill/num_people
    
    # Display the result
print("\n--- Bill Split Details ---")
for name in names:
        print(f"{name} owes: ${amount_per_person:.2f}")

if tip_percentage>=20:
        print("Thank you for your generosity!")
