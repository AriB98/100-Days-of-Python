#Day 3 of 100 days of code!
#Conditional Statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster.")
else:
  print("Sorry, you have to grow taller before you can ride.")

  
  
  #Exercise 3-1


number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
  print("This is an odd number.")


  #Exercise 3-2

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height**2))

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underwight.")
elif 18.5 < bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 < bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 < bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

  #Exercise 3-3

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else: 
  print("Not leap year.")


  #Exercise 3-4:

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
else:
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")


#Exercise 3-5

total_name = name1 + name2

lowername = total_name.lower()

t = lowername.count("t")
r = lowername.count("r")
u = lowername.count("u")
e = lowername.count("e")

l = lowername.count("l")
o = lowername.count("o")
v = lowername.count("v")
e = lowername.count("e")

total1= t + r + u + e
total2 = l + o + v + e
love_score = int(str(total1) + str(total2))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")