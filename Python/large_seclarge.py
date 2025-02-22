def large_sec_large(arr):
    if len(arr)<2:
        return 0
    else:
        max = float('-inf')   #max = -inf
        sec = float('-inf')   #sec = -inf
        for i in arr:         #5         2    3   -1   6       8
            if i > max:       #5>-inf    2>5  3>5 -1>5 6>5     8>6
                sec = max     #sec = -inf              sec = 5 sec = 6
                max = i       #max = 5                 max = 6 max = 8
            elif i > sec and i!=max:#     2>-inf
                sec = i             #      sec=2  3 -1
        if sec!=float('-inf'):
            return max, sec
arr = [5,2,3,-1,6,8]
result = large_sec_large(arr)
print(result)

arr.sort()
print(arr[-1],arr[-2])