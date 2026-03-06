# Unit 008 template

secret = "python"
tries = 3

while tries > 0:
    answer = input("Enter the password: ")

    if answer == secret:
        print("Correct!")
        break

    tries = tries - 1
    print("Wrong password. Tries left:", tries)

print("Program finished.")
