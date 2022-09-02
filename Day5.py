#Day 4 of 100 days of code
#Loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  print(f"{fruit} Pie")

print(fruits)

for number in range(1,11, 3):
  print(number)

total = 0
for i in range(1,101):
  total = total + i
  
print(total)





#Exercise 5-1

count = 0
height_sum = 0

for i in (student_heights):
  count = count + 1
  height_sum = height_sum + i

print(f"total height = {height_sum}")
print(f"number of students = {count}")
 
average = height_sum / count

print(round(average))


#Exercise 5-2

max_val = 0
for score in student_scores:
  if score > max_val:
    max_val = score

print(f"The highest score in the class is: {max_val}")


#Exercise 5-3

even_total = 0

for i in range(2,101, 2):
  even_total = even_total + i

print(even_total)

#Exercise 5-4


for number in range(1,101):
  if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
  elif number%5 == 0:
    print("Buzz")
  elif number%3 == 0:
    print("Fizz")
  else:
    print(number)