# Automatic Dice Roller
# Written by Vann W.

import random #needed for the random functionality


print ("Automatic Dice Roller")
#print("Press enter to roll or x and enter to exit")
val = input #giving val a user specified value
while val != "x": #while val is not x the program will run
    print("Press enter to roll and x to stop")
    val = input("") #another input for val
    if val == "x": #kills the program if x is entered
        quit()
    print (random.randint(1,6)) #generates and prints a number 1-6
