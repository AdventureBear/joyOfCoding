# Writing Loops
# by Suzanne Atkinson

#1a

for i in range(5):
    print(i+1)
print("======")

#1b
for j in range(2, 12, 3):
    print(j)

print("======")

#1c
for k in range(4):
    print("****")

print("======")
#1d
list = ""
for j in range(-10, 1, 2):
    list = list + " " + str(j)

print(list)
print("======")
#2
#prints CSCI 150 on separate lines
course = "CSCI 150"
for char in course:
    print(char)
print("======")
#3
for k in range(0,11):
    print(k)
