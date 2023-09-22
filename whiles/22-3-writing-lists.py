# Write a function, count_e, that takes a list of strings as a parameter and
# returns the total number of upper and lower case e’s (“E” and “e”) in all the
# strings in the list. Test that your function works with multiple examples.

def count_e(str_arr):
    total = 0

    for i in str_arr:
        for j in i:
            if j == "e":
                total += 1
            if j == "E":
                total += 1

    return total


def main():
    print(count_e(["hi", "hello", "EEK!"])==3)


main()
