import pygame
import sudo3
# initialise first with init()
pygame.init()
display_width = 800
display_height = 600

green = (0, 250, 0)
bright_green = (0, 155, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
bright_red = (155, 0, 0)

def button(msg, x, y, h, w, pc, sc,size):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(GD2, pc, (x, y, w, h))
        if click[0] == 1:
            sudo3.gameloop()


    else:
        pygame.draw.rect(GD2, sc, (x, y, w, h))
    drawtext(msg,x,y,h,w,size)

def drawtext(msg,x,y,h,w,size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(msg, True, black)
    textRect = text.get_rect()
    textRect.center = (x + w // 2 , y + h // 2)
    GD2.blit(text, textRect)

GD2 = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sudoku! ')
clock = pygame.time.Clock()
def menuloop():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    crashed = True

        GD2.fill(white)
        drawtext("Sudoku!",(display_width-50)//2-50,(display_height-25)//2-100,50,100,50)
        button('New Game', (display_width-100)//2-50, (display_height-25)//2+100, 50, 200, bright_red, red,32)
        pygame.display.update()
        clock.tick(60)

menuloop()
pygame.quit()
