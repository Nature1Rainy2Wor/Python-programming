#simple_interest
Principle_Amount=int(input("Enter your Principle_Amount:"))
Number_of_years=int(input("Enter your Number_of_years:"))
Rate_of_interest=float(input("Enter your Rate_of_interest:"))
Interest_amount=int(Principle_Amount*Number_of_years*Rate_of_interest/100)
Total_amount=Principle_Amount+Interest_amount
Monthly_amount=Interest_amount/12*Number_of_years
print("Total amount:",Total_amount)
print("Monthly amount:",Monthly_amount)