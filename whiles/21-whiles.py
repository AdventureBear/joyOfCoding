# Write python code to print the following using while loop
# a. 1
# 2
# 3
# 4
# 5

# i = 1
# while i < 6:
#     print(i)
#     i +=1

# b. 2
# 5
# 8
# 11

# agg = -1
# j = 0
# while j < 4:
#     agg += 3
#     print(agg)
#     j += 1

# c. -10 -8 -6 -4 -2 0

# agg = -12
# k=0
# while k < 6:
#     agg += 2
#     print(agg)
#     k+=1


# d. ****
# ****
# ****
# ****

# str = "****"
# l=0
# while l < 4:
#     print(str)
#     l+=1

# Write
# a
# while loop that prints the letters in “CSCI 150” on separate
 # lines.
#
# str = "CSCI 150"
# i = 0
# while i < len("CSCI 150"):
#     print(str[i])
#     i +=1
#

# 3. Create a program that allows the user to enter in a list of numbers,
# prints them out in sorted order, and prints the sum and average of
# the numbers. Prompt the user to continue entering numbers, and
# enter the number ‘0’ when finished.

list = []


def enter_nums():
    j = eval(input("enter the next number, enter '0' when done: "))
    while j != 0:
        list.append(j)



def sum_list():
    i = 0
    agg = 0
    while i < len(list):
        agg += list[i]
        i +=1
    return agg


def avg_list(num):
    print(len(list))
    avg = num / len(list)
    return avg


def main():
    enter_nums()
    print("Sum: ", sum_list())
    print("Avg: ", avg_list(sum_list()))


main()