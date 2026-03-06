# Unit 004 solution

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

add_result = first_number + second_number
subtract_result = first_number - second_number
multiply_result = first_number * second_number

print()
print("Add:", add_result)
print("Subtract:", subtract_result)
print("Multiply:", multiply_result)

if second_number != 0:
    divide_result = first_number / second_number
    print("Divide:", divide_result)
else:
    print("Divide: cannot divide by zero")
