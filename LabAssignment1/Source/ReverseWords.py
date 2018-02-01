#Python function that accepts a sentence of words from user and display:
#   Middle word
#   Longest word in the sentence
#   Reverse all the words in sentence
import math #To use floor methods
#function to return longest word
def longestWord(wordList):
    LongestWord=""          #Create an empty string
    for word in wordsList:  # loop through each word in wordsList
        if len(word)>len(LongestWord):  #if length of word is greater than longest word
            LongestWord = word          #then store word as longestword
    return LongestWord                  #Once we find longest word return it
#function to display middle word
def findMiddle(wordList):
    length = len(wordsList)     #store length of wordsList in variable word
    if length % 2 == 1:         #if wordsList has odd value as Length
        print("Middle Words are: ", wordsList[math.floor(length / 2)]) #print middle word which isexactly at centre
    else:                       #it has 2 middle words if wordsList has even value as Length
        print("Middle Words are: ", wordsList[((int(length / 2))-1):(int(length / 2) + 1)])
#function to return reversed word
def reverseWords(sequence):
    #returns reversed word after reversing each word using split() and joining back all the reversed words
    return ' '.join(word[::-1] for word in sequence.split())
#Take input sequence from user
sequence = input('Enter sequence of words: ')
#split and remove new line characters from user entered sequence and store it in wordList
wordsList = sequence.split()

findMiddle(wordsList)           #Call function to display Middle word in the sequence
print("Longest Word is: ",longestWord(wordsList))  #Print longest word from the word list
lowerCase = sequence.lower()    #Convert sequence into lowercase
print("Sentence with reverse words is: ",reverseWords(lowerCase))    #Print reversed words of the sequence