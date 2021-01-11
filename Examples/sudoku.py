import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

def print_solution(Sudoku):
    if Sudoku.stop == 1:
        for i in range(1, variables + 1):
            if (i - 1) % 9 == 0:
                print('|', sep='', end='')
            print('|', sep='', end='')
            print(Sudoku.value[i], end='')
            if i % 3 == 0:
                print('|', sep='', end='')
            if i % 9 == 0:
                print('|')

variables = 81
Sudoku = CS.CSP(variables, problem_name='Sudoku')
Sudoku.commonDomain([i for i in range(1, 10)])

for i in range(1,variables + 1):
    row1, col1 = (i - 1) // 9, (i - 1) % 9
    box1 = (row1 // 3, col1 // 3)
    for j in range(i + 1, variables + 1):
        row2, col2 = (j - 1) // 9, (j - 1) % 9
        box2 = (row2 // 3, col2 // 3) 
        if row1 == row2 or col1 == col2 or box1 == box2:
            Sudoku.addConstraint('value[' + str(i) + '] != value[' + str(j) + ']')

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

for i in range(0,9):
    for j in range(0, 9):
        if grid[i][j] != 0:
            Sudoku.setValue(i * 9 + j + 1, grid[i][j])
            
Sudoku.testAllDefaultParams(timeout = 1)

print_solution(Sudoku)
