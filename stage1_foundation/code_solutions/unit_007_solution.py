# Unit 007 solution

weather = input("Enter weather (sunny/rainy/cold): ")
score = int(input("Enter your score: "))

if weather == "sunny":
    print("Weather advice: Go outside for a short walk.")
elif weather == "rainy":
    print("Weather advice: Stay inside and study.")
else:
    print("Weather advice: Prepare well and keep warm.")

if score >= 90:
    print("Study advice: Excellent!")
elif score >= 60:
    print("Study advice: Good job, keep going.")
else:
    print("Study advice: Review more and try again.")
