import pygame
import copy
import problem
import numpy as np
pygame.init()
solved = False
curr_no = 0

board = np.zeros((9,9),dtype=int)
board2 = np.zeros((9,9),dtype=int)
hardcoded = [()]
display_width = 800
display_height = 600
black = (0, 0, 0)
grey = (171, 171, 165)
dark_grey = (255, 171, 165)
white = (255, 255, 255)
red = (255, 0, 0)
bright_red = (155, 0, 0)

GD = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Sudoku!')
clock = pygame.time.Clock()
# board = copy.deepcopy(problem.finalboard())
# board2 = copy.deepcopy(board)
# hardcoded = [()]
# for i in range(9):
#     for j in range(9):
#         if board[i][j] != 0:
#             hardcoded.append((i,j))

def start():
    global board
    global board2
    global hardcoded
    board = copy.deepcopy(problem.finalboard())
    board2 = copy.deepcopy(board)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                hardcoded.append((i,j))


# *******sudoku functions

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
            if arr[row+i][col+j] == num:
                return True
    return False

def if_safe(arr,row,col,num):
    if (not used_in_row(arr,row,col,num) and
        not used_in_col(arr,row,col,num) and
        not used_in_box(arr,row - row%3,col - col%3,num)):

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

def solve_sudoku(arr):
    l=[0,0]

    if not find_empty_loc(arr,l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if if_safe(arr,row,col,num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            arr[row][col] = 0
    return False
# *****ends here

def button(msg, x, y, h, w, pc, sc):
    global solved,board2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(GD, pc, (x, y, w, h))
        if click[0] == 1:
            if msg == "Solve":
                if solve_sudoku(board2) :
                    solved = True
    else:
        pygame.draw.rect(GD, sc, (x, y, w, h))
    drawtext(msg,x,y,h,w)

def drawtext(msg,x,y,h,w):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(msg, True, black)
    textRect = text.get_rect()
    textRect.center = (x + w // 2 , y + h // 2)
    GD.blit(text, textRect)

def drawsquares():
    mouse = pygame.mouse.get_pos()
    for x in range(0,540,60):
        for y in range(0,540,60):
            if x < mouse[0] < x + 60 and y < mouse[1] < y + 60:
                pygame.draw.rect(GD, dark_grey, [x, y,60,60])
            else:
                pygame.draw.rect(GD, grey, [x, y, 60, 60])
            if solved == True:
                drawtext(str(board2[x//60][y//60]),x,y,60,60)
            else:
                drawtext(str(board[x//60][y//60]),x,y,60,60)

def drawlines():
    for x in range(0,600,60):
        if x in [0,180,360,540]:
            pygame.draw.aalines(GD, red, False, [(x, 0), (x, 540)], 3)
    for y in  range(0,600,60):
        if y in [0,180,360,540]:
            pygame.draw.aalines(GD, red, False, [(0, y), (540, y)], 3)


def get_number(x, y,xp,yp):
    global curr_no
    curr_no = board[xp][yp]
    while 1:
        display_box(f"{curr_no}", x, y)
        inkey = get_key()
        if inkey.key == pygame.K_RETURN:
            break
        if inkey.unicode in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            curr_no = int(inkey.unicode)
        if inkey.key == pygame.K_BACKSPACE:
            curr_no = 0
    return curr_no

def display_box(message,x,y):
    pygame.draw.rect(GD, black,(x,y,50,50))
    if len(message) != 0:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(message, True, white)
        textRect = text.get_rect()
        textRect.center = (x+20, y+20)
        GD.blit(text, textRect)
        pygame.display.update()

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event
    else:
      pass

def sudocheck(num,x,y):
    for i in range(9):
        if num == board[x][i] or num == board[i][y]:
            return False
    return  True

crashed = False
def gameloop():
    start()
    global crashed
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    crashed = True
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 0 < mouse[0] < 540 and 0 < mouse[1] < 540:
                if click[0] == 1:
                    # print(f" x: {mouse[0]//60} , y : {mouse[1]//60}")
                    if (mouse[0]//60,mouse[1]//60) not in hardcoded:
                        x = mouse[0]//60
                        y = mouse[1]//60
                        num = get_number(650,50,x,y)
                        if(sudocheck(num,x,y)):
                            board[x][y] = num
            if 650 < mouse[0] < 750 and 350 < mouse[1] < 400:
                if click[0] == 1:
                    crashed = True

        GD.fill(white)
        drawsquares()
        drawlines()
        button('Solve',650,150,50,100,bright_red,red)
        button('menu', 650, 350, 50, 100, bright_red, red)
        pygame.display.update()
        clock.tick(60)
if __name__ == '__main__':


    gameloop()
    pygame.quit()
