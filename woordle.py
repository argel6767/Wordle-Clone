import tkinter as tk
import random

def getWord():
    #put three possible files than be read in a dict
    fileDict = {1 : "Wordle-Clone/wordle-La.txt",
                2 : "Wordle-Clone/wordle-Ta.txt"}
    #file chosen by random
    file = fileDict[random.randint(1,2)]
    
    #open now selected file
    with open(file, 'r') as fileRead:
        fileContents = fileRead.read()
    
    #changes string of file contents into array
    listOfWords = fileContents.split("\n")
    
    #creates empty string to become the chosen word
    roundWord = ""
    
    #makes sure the chosen word is exactly 5 letters long
    roundWord = listOfWords[random.randint(0,(len(listOfWords)-1))]
    return roundWord

def makeBoard(word):
    playBoard = [char for char in word]
    emptyList= []
    for i in range(len(playBoard)):
        emptyList.append("_")
    return emptyList

def wordToDict(word):
    listOfChars = word.split()
    
    charIndexDict = {}
    
    for index, char in enumerate(word):
        charIndexDict[index] = char
    
    return charIndexDict
    
def contains(guess, actualDict): 
    correctchars = []
    charsInRightSpot = []
    charsInWord = []
    
    for index , character in enumerate(guess):
        if character in actualDict.values() and actualDict.get(index) == character:
            charsInRightSpot.append(character)
        elif character in actualDict.values():
            charsInWord.append(character)
    correctchars.append(charsInRightSpot)
    correctchars.append(charsInWord)
    
    return correctchars
        
    
    
    

def correct(guess, actual):
    if guess == actual:
        return "You're guess was right!"
    if sorted(guess) == sorted(actual):
        return "you have all the letters, just not in the right order"
    else:
        return "wrong"


dict = wordToDict("apple")
contains("alien", dict)
##print(word1)
#print(word2)
#print(letterTracker(word1, word2))
#print(correct(word1, word2))
#print(similarLetters(word1, word2))
            


    


#window = tk.Tk()
#window.title("Hello World")

##window.mainloop()