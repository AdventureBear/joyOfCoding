#average
#prints the average of 10 numbers entered by a user

sum = 0
for i in range(0,10):
    #enter a number
    sum=sum + eval(input('Enter a number: '))

print(sum/10)
