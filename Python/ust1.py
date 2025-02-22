strV = 'aeiouAEIOU'
A = ['ELEPHANT','ANT','banana','rst','BBQ','wrty']
count = 0

for i in range(len(A)):
    x = A[i]
    has_vowels = False  
    for j in range(len(x)):
        if x[j] in strV:
            has_vowels = True  
            break
    
    if not has_vowels:
        count += 1

print(count)

        
