names = []

#reading include the extension 
#same folder location as tx_files.py

with open("names.txt") as txt_file:
    # print(txt_file)
    for line in txt_file:
        #to remove the new line in between
        line = line.strip()
        names.append(line)
        
#it will print \n for new line by default
#by unindenting we are closing the connection with the file, we dont file to be open for too long
print(names)

for name in names:
    print(name)

# # "w" tells it to write as by default it will read
# with open("names_output.txt", "w") as txt_file:
#     for name in names:
#         # \n is needed if you want the output in the new file with names on new line
#         txt_file.write(name + "\n")

counter = 1
with open("names_output.txt", "w") as txt_file:
    for name in names:
        txt_file.write(f"{counter}. {name}" + "\n")
        counter +=1


