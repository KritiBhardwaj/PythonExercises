# Q1) Write a program that determines whether or not it is time for Roary the cat to catch moths
moths_in_house = input("Please enter True or False: ") 
if moths_in_house == "True":
    print("Get the moths!")
elif moths_in_house == "False":
    print("No threats detected.")
else:
    print("No Action")

# moths_in_house = False
# if moths_in_house:
#     print("Get the moths!")
# else:
#     print("No threats detected.")


# Q2) Amend the previous program to determine whether or not it is time for Roary to go moth hunting.
moths_in_house = False
mitch_is_house = True

if moths_in_house and mitch_is_house:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_house:
    print("No threats detected.")
elif moths_in_house and not mitch_is_house:
    print("Meooooooooooooow! Hissssss!")
elif not moths_in_house and mitch_is_house:
    print("Climb on Mitch.")

 # Q3) Write a program that implements the algorithm for Red Light Cameras
light_colour = "Green"
car_detected = False

if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do Nothing.")
# elif light_colour == "Red" and car_detected:
#     print("Flash!")
# elif light_colour == "Green" and not car_detected:
#     print("Do Nothing.")
# elif light_colour == "Green" and car_detected:
#     print("Do Nothing.")
# elif light_colour == "Amber" and not car_detected:
#     print("Do Nothing.")
# elif light_colour == "Amber" and car_detected:
#     print("Do Nothing.")


# Q4) Write a program that asks the user for their height, and determine whether or not they are tall enough to
# ride the rollercoaster, which has a height requirement of 120cms
height = input("Enter your height: ")
if int(height) >= 120:
    print("Hop On!")
else:
    print("Sorry, not today :(")



