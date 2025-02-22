def find_min_and_second_min(arr):
    if len(arr) < 2:
        return "List is too short." # return when len is small

    min_val = float('inf')  # Initialize min_val to positive infinity
    second_min = float('inf')  # Initialize second_min to positive infinity

    for num in arr:                                  # 5         2    9   -1   5   6
        if num < min_val:                            # 5<+inf    2<5  9<2 -1<2 5<2 6<2
            second_min = min_val                     # sec = inf sec=5    sec=2 
            min_val = num                            # min = 5   min=2    min=-1
        elif num < second_min and num != min_val:    #                9<5      5<5 6<5
            second_min = num                         #                                exit

    if second_min == float('inf'):                   # sec!=inf
        return "No second minimum element found."
    else:
        return min_val, second_min

# Example usage:
arr = [5, 2, 9, -1, 5, 6]
result = find_min_and_second_min(arr)
print("Minimum and second minimum:", result)

arr.sort()
print(arr[0],arr[1])       # time complexity = O(nlogn)
