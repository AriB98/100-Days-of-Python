
print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")

tip = input("What percentage tip would you like to give? 10, 12 or 15? ")

people = input("How many people should split the bill? ")

total_bill = float(bill) + (float(bill) * (float(tip) / 100)) 

pay_per_person = total_bill / int(people)

print(f"Each person should pay: ${round(pay_per_person, 2)}")
