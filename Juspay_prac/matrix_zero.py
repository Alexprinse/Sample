def make_zero(grid:list)->list:
    row = len(grid)
    col = len(grid[0])
    change= []

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                change.append((i,j))
    while change:
        i,j = change.pop()
        for k in range(row):
            grid[k][j] = 0
        for l in range(col):
            grid[i][l] = 0
    
    return grid



print(make_zero([[1,1,1],[1,1,1],[0,1,0]]))
            