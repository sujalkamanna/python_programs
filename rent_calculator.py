# Rent calculator in python

rent = int(input("Enter your flat rent:"))

food = int(input("Enter food bill:"))

electricity = int(input("Enter electricity units in kWh (1 kWh = 12 Rupees):")) * 12

person = int(input("Enter no of people living in flat:"))

total = (rent + food + electricity) / person

print(f"Each person will pay: {total} Rs in total ")
