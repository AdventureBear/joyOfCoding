# Write a python program that asks the user for the name of a file, and then repeatedly
# asks the user to enter a number, entering the number ‘0’ when finished. Output each of
# these numbers to the file on a separate line.

prompt="Enter the name of your file: "

file_name = input(prompt)

dataFile = open(file_name, "w")

prompt2 = "Enter a number, enter '0' when finished: "

response = eval(input(prompt2))

while response != 0:
    print(response, file=dataFile)
    response = eval(input(prompt))

dataFile.close()

