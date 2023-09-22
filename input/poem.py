# Create a program poem.py that asks the user for 2 parts of speech as
# input (a plural noun and an adjective) and outputs the following:
# ______ are red, violets are blue
# Monty Python is _______, woo hoo!

pluralNoun = input("Enter a plural noun: ")
adjective = input("Enter an adjective: ")

print(pluralNoun.title(), "are red, violets are blue")
print("Monty Python is", adjective.lower()+ ", woo hoo")