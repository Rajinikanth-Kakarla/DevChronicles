matrix = [[0,1,2,0],[3,4,5,0],[1,3,1,5]]
position = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        target = 0
        if matrix[i][j] == target:
            position.append([i,j])
print(position)
