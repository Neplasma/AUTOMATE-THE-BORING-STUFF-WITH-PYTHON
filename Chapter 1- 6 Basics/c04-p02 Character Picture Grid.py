# Chapter 04 Practice 02 Character Picture Grid
# Shift x and y of a matrix

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def charShift(inputGrid):
    for j in range(len(inputGrid[0])):
        print('')
        for i in range(len(inputGrid)):
            print(grid[i][j]+' ',end='')
         
charShift(grid)   
    
