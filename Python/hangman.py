import random
words = ["kitten", "dog", "mouse", "jeff", "puppy"]
answerWord = words[random.randint(0,len(words)-1)]
answerList = []
lives = 5
letterInput = " "
rightGuess = 0
winLose = None
hangmanState=0
uniqueChar=len(set(answerWord))
for x in range(len(answerWord)):
    answerList.extend('_') 

def hangman(hangmanState):
    if hangmanState==0:
        print("---┐")
    if hangmanState==1:
        print("---┐")
        print("   O")
    if hangmanState==2:
        print("---┐")
        print("   O")
        print("   |")
    if hangmanState==3:
        print("---┐")
        print("   O")
        print("   |")
        print("  <|>")
    if hangmanState==4:
        print("---┐")
        print("   O")
        print("   |")
        print("  <|>")
        print("   |")
    if hangmanState==5:
        print("---┐")
        print("   O")
        print("   |")
        print("  <|>")
        print("   |")
        print("  | |")

#print(answerWord)
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
        hangman(hangmanState)
        
        if rightGuess == uniqueChar:
            winLose = True
            break
    
    else:   
        lives = lives-1
        print("Wrong!")
        hangman(hangmanState)
        hangmanState = hangmanState + 1
if winLose == True:
    print("You Won!")
else:
    print("You Lost!")
