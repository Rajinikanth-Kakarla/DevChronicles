def num_trees(n):
    if n == 0:
        return 0

    num_trees_arr = [0] * (n + 1)

    num_trees_arr[0] = 1

    for nodes in range(1, n + 1):
        for left_nodes in range(nodes):
            num_trees_arr[nodes] += num_trees_arr[left_nodes] * num_trees_arr[nodes - 1 - left_nodes]

    return num_trees_arr[n]

n = 3  
num_unique_trees = num_trees(n)
print(num_unique_trees)
