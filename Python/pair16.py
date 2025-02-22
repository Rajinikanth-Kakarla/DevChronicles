from itertools import combinations

def pair16(arr):
    pairs = []

    for combo in combinations(arr, 2):
        if sum(combo) == 16:
            pairs.append(combo)

    return pairs

arr = [2, 10, 3, 5, 6, 8, 9, 12, 11, 13]
result = pair16(arr)
print(result)
