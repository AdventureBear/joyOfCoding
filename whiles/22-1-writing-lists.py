# 1. Write a program that creates a list of 20 numbers input by the user and prints
# the average (mean) of the list

num = []
sum = 0

for i in range(0,20):
    j = eval(input("Enter a number:"))
    num.append(j)
    sum += j


print("list", num)
print("avg", sum/20)

