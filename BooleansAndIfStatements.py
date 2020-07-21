# Q1) Write a program that determines whether or not it is time for Roary the cat to catch moths
moths_in_house = True 
if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

moths_in_house = False
if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")


# Q2) Amend the previous program to determine whether or not it is time for Roary to go moth hunting.
moths_in_house = False
mitch_is_house = False

if moths_in_house and mitch_is_house:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_house:
    print("No threats detected.")
elif moths_in_house and not mitch_is_house:
    print("Meooooooooooooow! Hissssss!")
elif not moths_in_house and mitch_is_house:
    print("Climb on Mitch.")



