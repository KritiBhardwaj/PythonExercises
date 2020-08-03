# #Q1

# names = []

# with open("txt_files/names.txt") as txt_file:
#     for line in txt_file:
#         line = line.strip()
#         names.append(line)

# counter = 0
# with open("ReadingAndWritingOutput.txt", "w") as txt_file:
#     for name in names:
#         txt_file.write(f"{counter}: {name}" + "\n")
#         counter +=1
#         print(f"{counter}: {name}")


#Q2
import csv 

colours_20 = []
#how does it know to put it as a list of lists?
with open("exercise_data/colours_20.csv") as colour20_csv:
    reader = csv.reader(colour20_csv)
    for line in reader:
        colours_20.append(line)

for row in colours_20:
    print(f"{row[1].strip():<15}{row[2].strip():<15}{row[4].strip()}")

import csv 

colours_213 = []
#how does it know to put it as a list of lists?
with open("exercise_data/colours_213.csv") as colour213_csv:
    reader = csv.reader(colour213_csv)
    for line in reader:
        colours_213.append(line)

print()
for row in colours_213:
    print(f"{row[1].strip():<15}{row[2].strip():<15}{row[4].strip()}")


#q3 
import csv

colours_20 = []
with open("exercise_data/colours_20.csv") as colours20_csv:
    reader = csv.reader(colours20_csv)
    for line in reader:
        colours_20.append(line)
    
r = "Red"
g = "Green"
y = "Yellow"
count = 0
count2 = 0
yCount = 0

for line in colours_20:
    if r in line[2]:
        count +=1
    elif g in line[2]:
        count2 +=1
    elif y in line[2]:
        ycount +=1

print(count)
print(count2)
print(yCount)



    




    
        

