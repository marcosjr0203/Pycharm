message = "WeLcOmE tO tHe RoLlErCoAsTeR"
bill = 0
print(f"{message:~^40}")
height = int(input("Please, inform your height, in cm: "))
if height < 120:
    print("I'm sorry, you're you can't ride.")
else:
    age = int(input("Inform your age: "))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    elif age > 45 < 55:
        pass
    else:
        bill += 12
photo = input("Do you want a photo? ")
if photo.lower() == "y":
    bill += 3
else:
    pass
print(f"The total bill is ${bill:.2f}")
