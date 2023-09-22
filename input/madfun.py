# Write a program madfun.py that takes a decimal number as input from
# the user and prints out the following:
import math

userInput = eval(input("Enter a number with a decimal: "))
# a. The absolute value of the number
print(abs(userInput))
# b. The number rounded to 0 decimal places
print(round(userInput, 0))
# c. The square root of the rounded number’s absolute value
print(math.sqrt(abs(round(userInput, 0))))


# Example runs of this program might be:
# > Please enter a number: 8.88
# > 8.88
# > 9.0
# > 3.0
# > Please enter a number: -24.75
# > 24.75
# > -25.0
# > 5.0