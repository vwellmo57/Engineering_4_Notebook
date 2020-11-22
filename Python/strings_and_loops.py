words = 'This is random text we’re going to split apart'
words2 = words.split(' ')
print(type(words))
for x in range(0, len(words2)):
    print(words2[x])
