#start
def greet():
  your_name = input("What is your name?: ")
  print(f"Hello {your_name}!")
  print("My name is Ari")
  print("Let's learn Python")


greet()


def greet_with_name(your_name):
  print(f"Hello {your_name}!")
  print("My name is Ari")
  print("Let's learn Python")

greet_with_name("susan")

def greet_with(name, location):
  print(f"Hello {name}!")
  print(f"What is it like in {location}?")

greet_with(location="nowhere", name= "Aribim")

#exercise 8-1
import math

def paint_calc(height, width, cover):
  number_of_cans = (height * width)/cover
  print(f"You'll need {math.ciel(number_of_cans)} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#exercise 8-2

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It is a prime number")
  else:
    print("It is not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
