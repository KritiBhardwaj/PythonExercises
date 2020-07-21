
#Q1) Given the list of foods below, output:
foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]

print()
print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][2])

#Q2) Format and print the following list:
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

print()
print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")
print()


#Q3) Ask the user for three names, append them to a list, then print the list.
namesList = []
name1 = input("Enter first name: ")
namesList.append(name1)

name2 = input("Enter second name: ")
namesList.append(name2)

name3 = input("Enter third name: ")
namesList.append(name3)

print(namesList)


# Q4)
# 1. Ask the user to enter a string.
# 2. Split the string into a list, divided by spaces (hint: yourlist.split() will be useful).
# 3. Convert the string to a list, where each character is an item in the list (hint: list(yourlist) will be
# useful).
# 4. For each list: output the length of the list, and the list itself


string = input("Enter a string of words: ")
wordlist = string.split()
characterlist = list(string)
print(f"{len(wordlist)} {wordlist}")
print(f"{len(characterlist)} {characterlist}")






