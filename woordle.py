
import random

def getWord():
    fileDict = {1 : "wordle-La.txt",
                2 : "wordle-Ta.txt"}
    file = fileDict[random.randint(1,2)]
    with open(file, 'r') as fileRead:
        fileContents = fileRead.read()
    listOfWords = fileContents.split("\n")
    
    roundWord = listOfWords[random.randint(0,(len(listOfWords)-1))]
    return roundWord

def makeBoard(word):
    playBoard = [char for char in word]
    emptyList = ['_' for _ in playBoard]
    return emptyList

def wordToDict(word):
    charIndexDict = {}
    
    for index, char in enumerate(word):
        charIndexDict[index] = char
    
    return charIndexDict
    
def contains(guess, actualWord): 
    actualWord = wordToDict(actualWord)
    charsInRightSpot = []
    charsInWord = []
    
    for index , character in enumerate(guess):
        if character in actualWord[index]:
            charsInRightSpot.append(character)
        elif character in actualWord.values():
            charsInWord.append(character)
    
    return charsInRightSpot, charsInWord


def updateBoard(charsInRightSpot, actualWord):
    updatedBoard = []
    for chars in actualWord:
        if chars in charsInRightSpot:
            updatedBoard.append(chars)
        else:
            updatedBoard.append("_")
    return updatedBoard

def charNotInTheRightSpot(charsInWord):
    if charsInWord:
        print("The following character are in the word, just not in the right place: ")
        for char in charsInWord:
            print(f"{char}, ", end="")
        print()
        
         
    
    
    

def isGuessCorrect(guess, actual):
    return guess == actual
   


if __name__ == "__main__":
    roundWord = getWord()
    print(makeBoard(roundWord))
    guesses = []
    flag = True
    
    while(flag):
        playerGuess = input("The word is 5 letters. Guess a five letter word! ")
        charsInRightSpot, charsInWord = contains(playerGuess, roundWord)
        print(updateBoard(charsInRightSpot, roundWord))
        charNotInTheRightSpot(charsInWord)
        
        if(isGuessCorrect(playerGuess, roundWord)):
            print("You win!")
            flag = False
        
        

    
            


    


