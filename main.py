from z3 import *
import time

# create solver
s = Solver()

# create the board
board = [[Int('pos_%s_%s' %(i, j)) for i in range(9)] for j in range(9)]

# create the constraints

# each row contains a number
cells = [And (1<= board[i][j], board[i][j]<=9) for i in range(9) for j in range(9)]

# distinct numbered rows
distinct_rows = [ Distinct(board[i]) for i in range(9) ]


# distinct numbered cols
distinct_cols = [ Distinct([ board[i][j] for i in range(9)]) for j in range(9) ]

# distinct numbered 3x3
distinct_sqrs = [ Distinct([ board[i][j] for i in range(3*a, 3*a + 3) for j in range(3*b, 3*b + 3)]) for a in range(3) for b in range(3)]

sudoku = cells + distinct_rows + distinct_cols + distinct_sqrs

instance = ((0,6,0,0,1,2,0,5,0),
            (0,5,3,7,8,0,0,0,0),
            (0,0,7,0,0,0,0,0,9),
            (2,0,4,6,7,0,5,9,1),
            (6,0,5,3,4,1,7,8,0),
            (8,0,1,0,0,0,0,0,3),
            (0,1,0,2,0,0,0,0,0),
            (0,0,0,0,3,7,9,0,6),
            (0,0,6,0,0,0,2,7,0))

instance_constraint = []
for i in range(9):
    for j in range(9):
        if instance[i][j] != 0:
            instance_constraint.append(board[i][j] == instance[i][j])


s.add(sudoku + instance_constraint)

tic = time.perf_counter()
s.check()
toc = time.perf_counter()
print(f"Solved the constraint in {toc - tic:0.4f} seconds")

m = s.model()

for i in range(9):
    temp = []
    for j in range(9):
        temp.append(m.evaluate(board[i][j]))
        if (j+1) % 3 == 0:
            temp.append('|')
    print(temp)
    if (i+1) % 3 == 0:
        print(['-']*8)














