# Unit 006 solution

age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

is_adult = age >= 18
is_pass = score >= 60

print()
print("Adult:", is_adult)
print("Pass:", is_pass)
print("Can move to next step:", is_adult and is_pass)
