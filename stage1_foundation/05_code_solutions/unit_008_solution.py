# Unit 008 solution

secret = "python"
tries = 3

while tries > 0:
    answer = input("Enter the password: ")

    if answer == secret:
        print("Correct!")
        print("You may continue learning.")
        break

    tries = tries - 1
    print("Wrong password. Tries left:", tries)

if tries == 0:
    print("No tries left.")

print("Program finished.")
