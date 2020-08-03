# # Q1 Convert fahrenheit input to celcius 
# celcius = (fahrenheit - 32)* 5/9

def convert_to_C(input_in_F):
    temp_in_F = float(input_in_F)
    celcius = (temp_in_F - 32) * (5/9)
    print(f"Temperature {temp_in_F}F in celcius is: {celcius: .2f}C ")

input_in_F = input("Enter temperature in Fahrenheit: ")


convert_to_C(input_in_F)


#Q2 Write a program that calculates the mean of a list of numbers
def calculate_mean(total_sum, num_items):
    mean = (total_sum/num_items)
    print(total_sum)
    print(num_items)
    print(mean)

number = input("Enter a number:")
total_sum = 0
num_items = 0
while number:
    total_sum = total_sum + int(number)
    number = input("Enter a number:")
    num_items +=1
# while number != "":
#     total_sum = total_sum + int(number)
#     number = input("Enter a number:")
#     # if number != "":
#     #     num_items +=1
#     num_items +=1

calculate_mean(total_sum, num_items)


#q3 function to read csv and format output
import csv 

colour_data = []
def read_csv_file(filepath):  
    with open(filepath) as file:
        reader = csv.reader(file)
        for line in reader:
            colour_data.append(line)
    return read_csv_file


def format_colour_line(colour_data):
    for row in colour_data:
        print(f"{row[1].strip():<15}{row[2].strip():<15}{row[4].strip()}")

read_csv_file("ReadingWriting/exercise_data/colours_20.csv")
format_colour_line(colour_data)    


#4 
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

total_bill = 0
unit_cost_List = groceries

def calculate_cost(unit_price, number_purchase):
    total_item_cost = unit_price * number_purchase
    return total_item_cost

for item in groceries:
    unit_price = item[1]
    number_purchase = int(input(f"How many {item[0]}: "))
    unit_cost = round(calculate_cost(unit_price, number_purchase),2)
    item.append(unit_cost)

# print(unit_cost_List)

# print()
# print(f"====Izzy's Food Emporium====")
# for item in newList:
#     # print(f"{newList[0]:<20} : {newList[1]:2f}")
#     print(f"{item[0]:<20} : ${item[1]:.2f}")
# print('============================')
# print(f"{'$':>24}{groceryCost:.2f}")







