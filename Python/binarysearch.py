arr = [1,4,3,5,2,6,9,8,7]
target = 2
left = 0
right = len(arr)-1
while left<=right:
    mid = (left+right)//2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        left=mid + 1
    else:
        right=mid - 1

"""
0+8/2 = 4
"""