#!/usr/bin/python

# Method to identify if number is even or odd
def EvenOrOdd(number):
    # Modulus operator;
    # gives the remainder of the left value divided by the right value.
    if (number % 2) == 0:
        print("Number", number, "is even")
    else:
        print("Number", number, "is odd")

# Method to obtain the square of a number
def NumSquare(number):
    # Simply do the calculation
    numSquare = (number**2)
    print("The square of", number, "is", numSquare)

# Next 2 methods conver Fahrenheit to Celsius and vice versa
# Using a simple math formula
def FahrToCel(number):
    newNum = (number - 32) * (5/9)
    print(number,"degrees Fahrenheit is", round(newNum, 2), "degrees Celsius")

def CelToFahr(number):
    newNum = (number * (9/5)) + 32
    print(number,"degrees Celsius is", round(newNum, 2), "degrees Fahrenheit")

# This method allows for me to call any method I choose above
# It's the equivalent of a Switch in Java
def switcherMet(argument, number):
    # depending on the menu each one call a different method
    switcher = {
        1: EvenOrOdd,
        2: NumSquare,
        3: FahrToCel,
        4: CelToFahr
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid choice")
    # Execute the function
    func(number)

print("1- Identify if number is Even or Odd")
print("2- Obtain the square of a number")
print("3- Convert number from Fahrenheit to Celsius")
print("4- Convert number from Celsius to Fahrenheit")
print("")
argument = int(input("Choose 1 of 4 options: "))
number = int(input("Give me a number: "))

# 2 variables are sent to the method
switcherMet(argument, number)
