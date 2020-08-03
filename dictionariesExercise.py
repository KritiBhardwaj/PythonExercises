#q1 grovery receipt

groceries = {
"Baby Spinach": 2.78, 
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Bacon": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}

unit_list = []
groceries_total = {}
total_bill = 0 

def calculate_cost(unit_price, number_purchase):
    total_item_cost = unit_price * number_purchase
    return total_item_cost

for item, price in groceries.items():
    unit_price = price
    number_purchase = int(input(f"How many {item}: "))
    unit_cost = round(calculate_cost(unit_price, number_purchase),2)
    groceries_total[item]=unit_cost
    total_bill += groceries_total[item]

# print(total_bill)

#q2 create a dictionary from a list
names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

name_count = {}

#counting frequency using a dictionary
for name in names:
    if name in name_count:
        freq += 1
    else:
        freq = 1

    name_count[name]=freq
print(name_count)

for name, freq in name_count.items():
    print(f"{name}: {freq}")


#q3 create a list of dictionary

# import csv

# with open("ReadingWriting/exercise_data/colours_20.csv") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print (row)

import csv 

# read csv file as a list of lists
with open("ReadingWriting/exercise_data/colours_20.csv") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    # print(list_of_rows)

key_list = list_of_rows[0] #headings
value_list = list_of_rows[1:] #details of colours

colours = [] #list for holding dictionaries

#iterate of list_ofrows to create key:value pair
for row in value_list:
    #build a dictionary
    colour = {}
    for index, item in enumerate(row):
        key = key_list[index]
        colour[key] = item
    colours.append(colour)

print(colours[0])






    
