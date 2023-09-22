# Write a function are_we that takes a number of times to repeat and a phrase to
# be repeated as parameters and outputs the following for the given calls:

def are_we(num, phrase):
    string_phrase = (("Are we " + phrase + " yet? ") * num)
    print(string_phrase)

def main():
    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey!")


main()
