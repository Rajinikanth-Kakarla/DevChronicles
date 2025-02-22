def print_number_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(j) for j in range(1, 2 * i)))
print_number_pyramid(4)

print('\n')

def print_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
print_number_triangle(4)

print('\n')

def print_reverse_number_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
print_reverse_number_triangle(4)

print('\n')

def print_pascals_triangle(n):
    for line in range(1, n + 1):
        c = 1
        for j in range(1, n - line + 1):
            print(" ", end=" ")
        for i in range(1, line + 1):
            print(c, end=" ")
            c = c * (line - i) // i
        print()

# Example usage:
print_pascals_triangle(5)
