# Write a function mangle that takes a string as a parameter and returns the
# string after performing the following operations:
# i. Converting the string to all upper case letters
# ii. Removing the third character
# iii. Removing the third to last character

#convert to uppercase
def upper_case(strng):
    strng = strng.upper()
    return strng


def remove_third(strng):
    return strng[0:2] + strng[3:]


def remove_third_to_last(strng):
    return strng[:-3] + strng[-2:]


def mangle(strng):
    return remove_third_to_last(remove_third((upper_case(strng))))


def main():
    # print(mangle("archie is fun"))
    print(mangle("hellothere")=="HELOTHRE")
    print(mangle("42 degrees Celsius")=="42DEGREES CELSUS")
    print(mangle("eeeeeee")=="EEEEE")


main()