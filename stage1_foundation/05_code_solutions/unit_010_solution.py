# Unit 010 solution

def say_hello(name):
    print("Hello,", name)
    print("Keep learning!")


def add_numbers(first_number, second_number):
    return first_number + second_number


def is_pass(score):
    return score >= 60


say_hello("Student")
print("Add result:", add_numbers(10, 20))
print("Pass result:", is_pass(75))
