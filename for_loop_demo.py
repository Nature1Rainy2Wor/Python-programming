fruits = ["apple","banana","mango"]
for fruit in fruits:
    print(fruit)

for number in range(1,6):
    print(number)

text="Hello World"
print(text)
for letter in text:
    print(letter)

#break statement in for loop
fruits = ["apple","banana","mango"]
for fruit in fruits:
    if fruit=="banana":
        break
    print(fruit)
#continue statement
fruits = ["apple","banana","mango"]
for fruit in fruits:
    if fruit=="banana":
        continue
    print(fruit)