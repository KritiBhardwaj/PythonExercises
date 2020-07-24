# Q1) Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the
# numbers
number = input("Enter a number: ")
while len(number) > 0:
    sum = 0
    sum = sum + int(number)
    print(sum)





# name = input("What is your name? ")
# while len(name) > 1:
#     if name == "Vivian":
#         print("You are awesome!")
#     else:
#         print(f"Hi, {name}.")
#     name = input("What is your name? ")