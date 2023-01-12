# Print the values below from the grid list values:
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for j in range(len(grid[0])):
        for i in range(len(grid)):
                print(grid[i][j], end='')
        print()





