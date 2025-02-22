a = int(input())
b = [input() for i in range(a)]

for i in range(a):
    c = b[i]
    c1, c2, c3, c4 = 0, 0, 0, 0
    
    if 8 <= len(c) <= 15:
        for char in c:
            if char.islower():
                c1 += 1
            elif char.isupper():
                c2 += 1 
            elif char.isdigit():
                c3 += 1
            elif char.isascii():
                c4 += 1
        
        if c1 >= 1 and c2 >= 1 and c3 >= 1 and c4 >= 1:
            print("isValid")
        else:
            print("Not Valid")
    else:
        print("Not Valid")
