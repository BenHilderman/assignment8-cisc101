"""
This program turns the strings found from a url into a list of strings. The program has additional functions which use the data from this list.
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Nov 13, 2022
"""
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def readWords(urlLink):
    """
    This function reads the data from the link provided and returns a list of strings
    Parameters: urlLink - string
    Return Value: list
    """
    try:
        # open url
        response = urllib.request.urlopen(urlLink)
        # read values and split into a list
        listWords = response.read().decode('utf-8').split()
        return listWords
    except:
        # if url gets an error
        print("The URL is invalid")
        return []

def wordCount(listWords):
    """
    This function converts the list of strings into a dictionary containing the number of letters in a word as the key and the number of words in the list of strings that are the same length as the value
    Parameters: listWords - list
    Return Value: dictionary
    """
    # creating dictionary
    numberList = {}
    list = []
    for i in range(len(listWords)):
        # making a list of the lengths of the strings
        list += [len(listWords[i])]
    for i in list:
        # using .count() to count amount of repeated words with the same length
        # adding to a dictionary
        numberList[i] = list.count(i)
    return(numberList)

def totalWords(numberList, n, m):
    """
    This function uses numberList and returns the total number of words lengths n to m
    Parameters: numberList - dictionary, n m - int
    Return Value: int
    """
    totalNumberWords = 0
    # n cant be higher than m
    if n > m:
        return 0
    else:
        # looping between the two values
        for i in range(n,m+1):
            # adding up the values to get the sum
            totalNumberWords += int(numberList[i])
        return(totalNumberWords)

def maxWordLength(numberList):
    """
    This function uses numberList and returns the maximum length of a word found
    Parameters: numberList - dictionary
    Return Value: int
    """
    max = 0
    # looping all lengths
    for i in numberList:
        # replaces max if value is higher than current max
        if i > max:
            max = i
    return max

def maxFrequency(numberList):
    """
    This function uses numberList and returns the key with the maximum length of a word found
    Parameters: numberList - dictionary
    Return Value: int
    """
    max = 0
    # looping key/value pairs in numberList
    for key, value in numberList.items():
        # replacing current max if value is higher
        if value > max:
            max = value
            # key of the highest value is what gets returned
            returnMax = key
    return returnMax

def writeToFile(numberList):
    """
    This function uses numberList. It opens a file named statWords.txt, and writes the key/value pairs from the numberList to the file
    Parameters: numberList - dictionary
    Return Value: none
    """
    # open file
    openFile = open('statWords.txt', 'w')
    # loop key/value pairs
    for key, value in numberList.items():
        # writing on the file
        openFile.write("There are " + str(value) + " words of length " + str(key) + "\n")
        # closing the file
    openFile.close()

def main():
    listWords = readWords('https://research.cs.queensu.ca/home/cords2/words.txt')
    print("Converting the data found from the link to a list of strings:")
    print(listWords)

    numberList = wordCount(listWords)
    print("Converting the list of strings into a dictionary containing the number of letters in a word and the number of words in the list of strings that are the same length as the value:")
    print(numberList)

    totalWord = totalWords(numberList, 1, 2)
    print("Returning the total number of words lengths n to m:")
    print(totalWord)

    wordLengthMax = maxWordLength(numberList)
    print("Returning the maximum length of a word found:")
    print(wordLengthMax)

    frequencyMax = maxFrequency(numberList)
    print("Returning the key with the maximum length of a word found:")
    print(frequencyMax)

    print("Opening a file named statWords.txt, and writing the key/value pairs from the numberList to the file:")
    writeToFile(numberList)

main()