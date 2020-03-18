grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# function to print the list partter in transpose
def gridImage(grid):

    str1 = ''

    for i in range(len(grid[0])):
        print()
        for j in range(len(grid)):
            print((grid[j][i]),end = '')
    return ''

print(gridImage(grid))
print("--------------------------------")

# in a single line of code, can be used with function
print('\n'.join(map(''.join, zip(*grid))))
