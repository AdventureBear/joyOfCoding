def pyramid(symbol, repeats):
    for i in range(1, repeats+1):
        print(symbol * i)

def main_pyramid():
    pyramid("*", 2)
    pyramid("+", 5)
    pyramid("x", 10)

# main_pyramid()

def absolute_difference(x,y):
    if x > y:
        print( x-y )
    else:
        print( y-x )

def main_abs():
    absolute_difference(5, 10)
    absolute_difference(10, 5)
    absolute_difference(200, -200)

main_abs()
