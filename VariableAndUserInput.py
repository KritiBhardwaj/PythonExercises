# Q1 program that takes two numbers from the user, and outputs their sum
num1A = input("Enter the first number: ")
num1B = input("Enter the second number: ")
sum = int(num1A) + int(num1B)
print(sum)

# Q2 program that takes two numbers from the user, and outputs the equation representing the
# multiplication of the two numbers
num2A = input("Enter the first multiple: ")
num2B = input("Enter the second multiple: ")
product = int(num2A) * int(num2B)
print(f"{num2A} * {num2B} = {product}")

# Q3 Write a program that takes a distance in kilometers from the user, and output the distance in meters and
# centimeters
distance = input("Enter distance in kilometers: ")
outputInMeters = int(distance) * 1000
outputinCentimeters = int(distance) * 100000
print(f"{distance}km = {outputInMeters}m")
print(f"{distance}km = {outputinCentimeters}cm")

# Q4 Write a program that takes the users name and height (in centimeters), and outputs a summary sentence
name = input("Please enter your preferred name: ")
height = input("How tall are you in centimeters: ")
print(f"{name} is {height}cms tall.")