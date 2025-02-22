arr = [1,2,3,4,5,6,7,8,9]
target = 5
for i in range(len(arr)):
    if target == arr[i]:
        print(arr[i],'element is at',i,'index')