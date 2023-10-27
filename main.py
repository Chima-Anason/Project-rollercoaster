print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
bill = 0
if height >120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?\n"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  elif age >=45 and age <=55:
    print("Everything will be fine, have a free ride on us")
  else:
    bill = 12
    print("Adult tickets are $12")

  want_photo = input("Do you want a photo? (y/n)\n")
  if want_photo == "y":
    bill += 3
  print(f"Your total bill is ${bill}")
else:
  print("Sorry, you are not tall enough to ride the rollercoaster.")
