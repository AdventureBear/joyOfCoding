def sum_r(n):
    #base case
    if n==1:
        return n
    else:
        return sum_r(n-1) + n


def sum_i(n):
    result = 0
    for i in range(1, n+1):
        result +=i
    return result


def main():
    print(sum_r(2))
    print(sum_r(3))
    print(sum_r(5))
    print(sum_i(2))
    print(sum_i(3))
    print(sum_i(5))


main()