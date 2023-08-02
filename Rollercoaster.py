print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill += 7
    elif age < 45:
        print("Adult tickets are 12")
        bill += 12
    elif age >= 45 and age <= 55:
        print("Free ride!")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3

    print(f"Your total bil is ${bill}")

else:
    print("Sorry, you have to grow taller!")

