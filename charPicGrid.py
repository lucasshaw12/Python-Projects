#! python3
# Transpose the grid using different concepts

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# # 1st version of printing the grid
for x in range(6):
    for y in range(9):
        if y < 8:
            print(grid[y][x], end='')
        else:
            print(grid[y][x])

# # 2nd version of printing the grid
for column in zip(*grid):
    print(''.join(column))

# 3rd version of printing the grid
print('\n'.join(map(''.join, zip(*grid))))
