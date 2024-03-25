import tkinter as tk
import random

def getWord():
    #put three possible files than be read in a dict
    fileDict = {1 : "Wordle-Clone/wordle-La.txt",
                2 : "Wordle-Clone/wordle-Ta.txt",
                3: "Wordle-Clone/words.txt"}
    #file chosen by random
    file = fileDict[random.randint(1,3)]
    
    #open now selected file
    with open(file, 'r') as fileRead:
        fileContents = fileRead.read()
    
    #changes string of file contents into array
    listOfWords = fileContents.split("\n")
    
    #creates empty string to become the chosen word
    roundWord = ""
    
    #makes sure the chosen word is exactly 5 letters long
    while (len(roundWord) != 5):
        roundWord = listOfWords[random.randint(0,(len(listOfWords)-1))]
    print(roundWord)
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
    for character in guess:
        if character in actualDict.values():
            correctchars.append(character)
    return correctchars
        
    
    

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