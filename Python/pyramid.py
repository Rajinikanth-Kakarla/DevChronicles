def even_pyramid(n):

    for i in range(n):
        print(" "*(n-i)+"*"*i+"*"*i)
even_pyramid(5)

def odd_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

odd_pyramid(4)
