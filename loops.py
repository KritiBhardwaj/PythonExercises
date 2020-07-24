# # Q1) Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the
# # numbers
# # number = 0
# # sum = 0
# # while number != '':
# #     number = input("Enter a number: ")
# #     if number:
# #         sum = sum + int(number)
# #         print(sum)


# sum = 0
# number = 'number'
# while len(number) > 0:
#     number = input("Enter number: ")
#     sum = sum + int(number)
#     print(f"The sum is {sum}")



# Q2) Use a for loop to format and print the following list:
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for contact in mailing_list:
    # print(f"{item[0]: <20} ${item[1]: .2f}")
    print(f"{contact[0]:} : {contact[1]}")


# Q3) Use a while loop to ask the user for three names and append them to a list, use a for loop to print the list.
count = 0
nameList = []
while count < 3:
    name = input("Enter name: ")
    nameList.append(name)
    count += 1
print()
for name in nameList:
    print(name)


#4 Ask the user how many units of each item they bought, then output the corresponding receipt
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

print()
print(f"====Izzy's Food Emporium====")
newList = []
for item in groceries:
    n = input(f"How many {item[0]}: ")
    totalItemCost = item[1] * int(n)
    print(f"{item[0]:<20} : {totalItemCost:}")
    newList.extend([item[0], totalItemCost])
    print(newList)