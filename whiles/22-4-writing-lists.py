# Write a function, count_vowels, that takes a list of strings as a parameter
# and returns the total number of upper and lower case vowels (A, E, I, O, U) in all
# the strings in the list.

def count_vowels(str_arr):
    vowels = "AEIOU"
    total = 0
    for i in str_arr:
        upper = i.upper()
        for v in vowels:
            total += upper.count(v)
        # total += upper.count("E")
        # total += upper.count("I")
        # total += upper.count("O")
        # total += upper.count("U")

        # print (i)
        # for j in i:
        #     print (j)
        #     if j in vowels:
        #         print(j in vowels)
        #         total += 1
    return total


def main():
    print((count_vowels(["hi", "hello", "OOF!"]))==5)


main()
