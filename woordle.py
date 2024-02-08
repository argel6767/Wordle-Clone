import tkinter as tk
import random

def getWord():
    with open("words.txt", 'r') as file:
        fileContents = file.read()
    words = fileContents.split("\n")
    roundWord = words[random.randint(0,len(words))]
    return roundWord

def makeBoard(word):
    playBoard = [char for char in word]
    emptyList= []
    for i in range(len(playBoard)):
        emptyList.append("_")
    return emptyList


'''def letterTracker(word, desiredWord):
    wordArray = [char for char in word]
    desiredArray = [char for char in desiredWord]
    correctLetters = {}
    for i in range(len(desiredArray)):
        correctLetters.update({desiredArray[i]:[]})
    for i in range(len(wordArray)):
        for k in range(len(desiredArray)):
            if (wordArray[i] == desiredArray[k]):
                if i not in correctLetters[wordArray[i]]:
                    correctLetters[wordArray[i]].append(i)
    return correctLetters'''
    
def contains(guess, actual): 
    guess =[char for char in guess]
    containedLetters = []
    for i in enumerate(actual):
        if guess[i] in actual:
            containedLetters.append(guess[i])
    return containedLetters

def similarLetters(guess, actual):
    guess = sorted([char for char in guess])
    actual = sorted([char for char in actual])
    count = 0
    for i in range(len(actual)):
        if (i == len(guess) -1):
            break;
        if (guess[i] == actual[i]):
            count+=1
            
    return count/len(actual)
    
    

def correct(guess, actual):
    if guess == actual:
        return "You're guess was right!"
    if sorted(guess) == sorted(actual):
        return "you have all the letters, just not in the right order"
    else:
        return "wrong"

word1 = getWord()       
word2 = getWord()
print(word1)
print(word2)
print(letterTracker(word1, word2))
print(correct(word1, word2))
print(similarLetters(word1, word2))
            


    


window = tk.Tk()
window.title("Hello World")

##window.mainloop()