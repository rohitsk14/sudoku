import random
def print_board(arr):
    for i in range(9):
        for j in range(9):
            print(f'{arr[i][j]} ',end='')
        print("\n")

def used_in_row(arr,row,col,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr,row,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[row+i][col+j] == num):
                return True
    return False

def if_safe(arr,row,col,num):
    if( not used_in_row(arr,row,col,num) and
        not used_in_col(arr,row,col,num) and
        not used_in_box(arr,row - row%3,col - col%3,num)
        ):
        return True
    else:
        return False

def find_empty_loc(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

def finalboard():
    for i in range(6):
        for j in range(6):
            x = random.randint(0,8)
            y = random.randint(0,8)
            board[x][y] = 0
    return board

def solve_sudoku(arr):
    l=[0,0]

    if(not find_empty_loc(arr,l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if(if_safe(arr,row,col,num)):
            arr[row][col] = num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False

index=[[1,2,3],
        [4,5,6],
        [7,8,9]]

board=[[0 for x in range(9)]for y in range(9)]
for i in range(3):
    for j in range(3):
        x = random.randint(0,8)
        y = random.randint(0,8)
        board[x][y] = index[i][j]
# print_board(board)

if(solve_sudoku(board)):
    # print_board(board)
    pass

board = finalboard()
print("-------------------------------------")
# print_board(board)