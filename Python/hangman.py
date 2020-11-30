import random
words = ["cat", "dog", "mouse", "jeff", "puppy"]
answerWord = words[random.randint(0,len(words)-1)]
lives = 9
letterInput = "a"

print(answerWord)
print("Welcome to Hangman!")
while lives>0:
    letterInput = input("Enter a guess: ")
    if letterInput in answerWord:
        print("Correct!")
    else:   
        lives = lives-1
        print("Wrong!")
