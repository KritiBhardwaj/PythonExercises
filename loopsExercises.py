# Q1) Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the
# numbers

number = 0 
while number != "":
    number = input("Enter a number: ")
    number = int(number) + number
