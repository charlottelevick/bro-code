# Weight converter

weight = float(input("Please enter your weight: "))
unit = input("Is that in Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    print(f"{round(weight, 2)}kg")
elif unit == "L":
    weight = weight / 2.205
    print(f"{round(weight, 2)}lbs")
else:
    print("Please choose a capital K or L")