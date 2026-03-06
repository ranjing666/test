# Unit 007 template

weather = input("Enter weather (sunny/rainy/cold): ")
score = int(input("Enter your score: "))

if weather == "sunny":
    print("Go outside for a short walk.")
elif weather == "rainy":
    print("Stay inside and study.")
else:
    print("Prepare well and keep warm.")

if score >= 90:
    print("Excellent!")
elif score >= 60:
    print("Good job, keep going.")
else:
    print("Review more and try again.")
