# Unit 004 template

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print()
print("Add:", first_number + second_number)
print("Subtract:", first_number - second_number)
print("Multiply:", first_number * second_number)

if second_number != 0:
    print("Divide:", first_number / second_number)
else:
    print("Divide: cannot divide by zero")
