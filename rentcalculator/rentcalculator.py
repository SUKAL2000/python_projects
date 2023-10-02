rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity = int (input("Enter unit = "))
chargh_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons = "))

total_bill = electricity * chargh_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)