# Write a function average_neg_evens that takes a list of numbers as a
# parameter, and adds all the negative even numbers (less than 0 and
# divisible by 2) together and returns their average.
# Example function call:
# print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
# Outputs: -3

def average_neg_evens(num_list):
    new_list = []
    for i in num_list:
        if i< 0 and i%2==0:
            new_list.append(i)


    return sum(new_list)/len(new_list)


# Write a function count_letter that takes a list of strings and a string
# letter as parameters and returns the number of times this letter
# occurs, both upper- & lower-cased.
# Example function call:
# list = [“HELLO”, “goodbye”, “1234 Oooh!”]
# print(count_letter(list, “o”))
# Outputs: 6

def count_letter(list, letter):
    count = 0
    upper = letter.upper()
    # print(upper)
    i=0
    while i < len(list):
        # print(i)
        word = list[i].upper()
        # print(word, upper)
        count += word.count(upper)
        i += 1

    return count


def main():
    print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])==-3)
    list = ["HELLO", "goodbye", "1234  Oooh!"]
    print(count_letter(list, "o")==6)

main()
