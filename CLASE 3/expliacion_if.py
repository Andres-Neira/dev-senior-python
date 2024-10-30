age=int(input("hoe old are you"))
country="GER"
if age >= 21 and country == "USA":
    print("you can buy alcohol")
elif age>=18 and country=="COL":
    print("you can buy alcohol")
elif age>=16 and country=="GER":
    print("you can buy alcohol")
else:
    print("you can't buy alcohol")

