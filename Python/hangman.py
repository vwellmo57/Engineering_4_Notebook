import random   #lets us generate a random number
words = ["kitten", "dog", "mouse", "jeff", "puppy"]   #list of words
answerWord = words[random.randint(0,len(words)-1)]  #picks a random word from list
answerList = []   #making a list for the user answers
lives = 5   #amount of lives
letterInput = " " 
rightGuess = 0  #amount of correct guesses
winLose = None  #set to true or false, triggers an end game messege 
hangmanState=0   #state of the hangman drawing
uniqueChar=len(set(answerWord))   #finds the amount of unique characters
for x in range(len(answerWord)):  #makes the answer array as long as the answer
    answerList.extend('_') 

def hangman(hangmanState):   #this is the array of the hangman drawings
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

#print(answerWord)  #prints the answer for testing
print("Welcome to Hangman!")
while lives>0:  #while the user is alive
    letterInput = input("Enter a guess: ")    #takes user input
    if letterInput in answerWord:   #if they guessed a letter in the answer
        print("Correct!")
        for x in range(len(answerWord)):  #runs the amount of characters in the answer
            if letterInput == answerWord[x]: #if they match a letter
                answerList[x] = letterInput   #sets it into the answer list
        print(answerList)   #prints their progress
        rightGuess = rightGuess + 1   #specifiying the state of the hangman drawing
        hangman(hangmanState)   #calls the drawing function
        
        if rightGuess == uniqueChar:   #if they finish the word
            winLose = True   
            break       #exits the loop
    
    else:   
        lives = lives-1   #lose a life
        print("Wrong!")   #tell them
        hangman(hangmanState)  #print the hangman
        hangmanState = hangmanState + 1   #add one so that the drawing gets bigger next time
if winLose == True:   #if they win tell them
    print("You Won!")
else:    #if they lose tell them
    print("You Lost!")
