answer=(input("Are you a student or guest? Yes or No:"))
is_student=answer=="Yes"
if is_student:
    print("You are a student")
else:
    print("You are a guest")


name=(input("Enter your name:"))
print("Hello," + name +"!")

age=int(input("Enter your age:"))
print("you will be",  age + 1 ,"next year.")

price=int(input("Enter your price:"))
discount=price*0.1
print("Dicount is:",discount)

