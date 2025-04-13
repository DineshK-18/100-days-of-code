print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip=int(input("How much tip would you like to give?"))
act_tip=tip/100
people=int(input("How many people to split the bill?"))
total_bill=((bill*act_tip+bill)/people)
print("Each Person should pay:",round(total_bill,2))

