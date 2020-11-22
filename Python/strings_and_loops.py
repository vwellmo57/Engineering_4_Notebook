words = input("Enter the sentence: ")
words = words.split(' ')
for x in range(0, len(words)):
    for y in range(0,len(words[x])):
        print(words[x][y])
    print("-")
