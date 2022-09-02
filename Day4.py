#Day 4 of 100 days of code
#Randomisation and lists

import random 

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() 

print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")



#Exercise 4-1

import random

cointoss = random.randint(0,1)

if cointoss == 0:
  print("Tails")
else:
  print("Heads")


  #Exercise 4-2

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random


name_lenght = len(names)

rand_name = random.randint(0,name_lenght - 1)

pay = names[rand_name]
print(f"{pay} is going to buy the meal today!")








