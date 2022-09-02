
#Day 2 of 100 days of code!
#Data types 


#string
#substring
print("hello"[4])

print("123" + "345")

#integer

print(123+345)

#float

print(3.123)

#boolean
True
False

#type() function checks data type

#str() function converts data to string


#Exercise 2-1

x = int(two_digit_number[0])
y = int(two_digit_number[1])

print(x + y)


#mathematical expressions

print(3 * 3 + 3 / 3 -3)

#Exercise 2-2

bmi = float(weight) / (float(height) ** 2)

print(int(bmi))


#rounding numbers 

print(round(2 /3, 2))

print(8//3)

#shorthand 

score = score + 1
score += 1

#f-string

print(f"your score is {score}") #immediately converts all data types to string

#Exercise 2-3

days_left = (int(90*365)) - (int(age)*365)
weeks_left = (int(90*52)) - (int(age)*52)
months_left = (int(90*12)) - (int(age)*12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
