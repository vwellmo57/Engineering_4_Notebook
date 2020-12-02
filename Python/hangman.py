import random
words = ["kitten", "dog", "mouse", "jeff", "puppy"]
answerWord = words[random.randint(0,len(words)-1)]
answerList = []
lives = 5
letterInput = " "
rightGuess = 0
winLose = None
uniqueChar=len(set(answerWord))
for x in range(len(answerWord)):
    answerList.extend('_') 

print(answerWord)
print("Welcome to Hangman!")
while lives>0:
    letterInput = input("Enter a guess: ")
    if letterInput in answerWord:
        print("Correct!")
        for x in range(len(answerWord)):
            if letterInput == answerWord[x]:
                answerList[x] = letterInput
        print(answerList)
        rightGuess = rightGuess + 1
        if rightGuess == uniqueChar:
            winLose = True
            break
    else:   
        lives = lives-1
        print("Wrong!")
if winLose == True:
    print("You Won!")
else:
    print("You Lost!")

