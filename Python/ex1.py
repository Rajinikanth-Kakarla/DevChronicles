class sol:
    def minE(arr, k):
        arr.sort()  # Corrected sorting
        b = []
        for i in range(k):
            x = arr[i]
            b.append(x)
        print(max(b) - min(b))

arr = [10, 100, 200, 1000, 2000, 20, 30]
k = 3
sol.minE(arr, k)
