#!/usr/bin/python

# Method that gets the largest number of a randon generated list
def Largest():
    import random

    theList = []
# Creates the random list of 10 (from 1 to 50)
    for i in range(10):
        x = random.randint(1,50)
        theList.append(x)

# Prints the list to view
    print("The list:", theList)
# Uses the sort in reverse to get the first number of the list
# Which should be the largest
    theList.sort(reverse=True)
    print("Largest number in the list:", theList[0])

def palindrome():

    word = input("Add a word: ")
# This turns the word backwards
    bWord = word[::-1]
# Compares to see if the word is the same
    if word == bWord:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

def vowelCount():

    word = input("Add a word: ")

# List of vowels
    vowels = "aeiou"
    count = 0
# In the if all letters are changed to lowercase
# Because the comparison is case sensitive
    for i in word:
        if i.lower() in vowels:
            count = count + 1
    print("Number of vowels:", count)

# Switch like Method to call above methods
def switcherMet(argument):
    switcher = {
        1: Largest,
        2: palindrome,
        3: vowelCount,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid choice")
    # Execute the function
    func()

print("1- From a random generated list of numbers, get the largest")
print("2- Find out if a word is a palindrome")
print("3- How many vowels are in your word?")
print("")
argument = int(input("Choose 1 of 3 options: "))
print("")

# For this switch only the number chosen is sent
switcherMet(argument)
