grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

gridWidth = len(grid)
gridLen = len(grid[0])
i = 0
j = 0
for i in range(gridLen):
    if i < gridLen:
        for j in range(gridWidth):
            if j < gridWidth:
                print(grid[j][i], end='')
                j += 1
        print('\n')
        i += 1