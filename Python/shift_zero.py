def shift_zeroes_to_left(arr):
    if not arr:
        return arr  # Empty array, nothing to do

    left = 0              #0 1 1 2 3
    right = len(arr) - 1  #6 5 4 4

    while left < right:
        if arr[left] == 0 and arr[right] != 0:
            # Swap the elements at left and right pointers
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] != 0:
            left += 1
        elif arr[right] == 0:
            right -= 1

    return arr

# Example usage:
arr = [0, 2, 0, 3, 4, 0, 5]
result = shift_zeroes_to_left(arr)
print(result)
