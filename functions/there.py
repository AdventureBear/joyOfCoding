# Write a function there that takes a number n as a parameter, and returns 2n if
# n is positive, and 0 otherwise.

def there(n):
    if n>=0:
        return pow(2,n)
    else:
        return 0


def main():
    print(there(5)==32)
    print(there(0)==1)
    print(there(3)==8)
    print(there(-2)==0)
    print(there(-6)==0)

main()