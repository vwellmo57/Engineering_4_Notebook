words = input("Enter the sentence: ").split(' ')   #takes the input from the user and puts it in a list with a space in between
for x in range(0, len(words)):  #a loop that runs for the length of the string
    for y in range(0,len(words[x])):  #loop that runs for the length 
        print(words[x][y])  #prints a letter from a part of the loop
    print("-")  #prints - in between words
