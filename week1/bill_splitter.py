total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage you would like to give (e.g., 15 for 15%): "))
people = int(input("How many people are there?"))

tip_amount=total_bill *tip_percentage /100
total_amount = total_bill + tip_amount
amount_per_person = total_amount /people

print(f"Tip Amount: {tip_amount:.2f}")
print(f"Total Amount: {total_amount:.2f}")
print(f"Amount Per Person: {amount_per_person:.2f}")