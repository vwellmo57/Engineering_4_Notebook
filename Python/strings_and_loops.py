words = "hello there bob"
words = words.split()
str1 = ''

for x in range(0, len(words)):
    print(words[x])
    for y in range(4):
        print(y)
        str1 = ''.join(words[y])
        print(str1[y]) 
