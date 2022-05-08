from curses import KEY_UP
from queue import Empty
from typing import TYPE_CHECKING
import pygame
from pygame.locals import *
import time
import random
dbclock = pygame.time.Clock()
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
down = 0
up = 0
score = 0
right = 0
left = 0

snakel = []
ateFood = False
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
#width, height = pygame.display.get_surface().get_size()
#print('width:', width)
#print('height:', height)

pygame.display.set_caption("Donkey From Shrek!!")

black = (0, 0, 0)
dark_red = (139, 0, 0)
green = (0, 158, 42)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
silver = (192, 192, 192)
purple = (128, 0, 128)
teal = (0, 128, 128)
navy = (0, 0, 128)
x = 1
right_pad_y = 150
right_pad_x = 545
left_pad_x = 12
left_pad_y = 150
paddle_height = 120
paddle_speed = 30
ball_speed = 15
x1 = 0
y1 = 0
flag = 0
foodx = (random.randint(0,640) // 10 ) * 10
foody = (random.randint(0,640) // 10 ) * 10
snakex = (random.randint(0,640) // 10 ) * 10
snakey = (random.randint(0,640) // 10 ) * 10
snakel.append([snakex,snakey])
colors = [dark_red, green, red, lime, blue, yellow,
          cyan, magenta, silver, purple, teal, navy]
color = random.choice(colors)
l = []
center_x = 300
center_y = 300
w = 1
q = 0
p1 = 0
p2 = 0
score_p1 = str(p1)
score_p2 = str(p2)
def show_text(msg,x,y, color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

random.randint(1, 2)
while True:

    screen.fill(black)
    show_text("score: "+ str(score),10,10,red)
    snakel.insert(0,[snakex, snakey])
    if score>10:
        show_text("You Win",100,100,blue)
        pygame.display.update()
        time.sleep(10)
        break
    if snakel[0][1] <= 0 or snakel[0][1]>=600:
        #up and down
        show_text("Game Over",100,100,blue)
        pygame.display.update()
        time.sleep(3)
        break
    if snakel[0][0]<=-10 or snakel[0][0] >= 600:
        #left and right
       show_text("Game Over",100,100,blue)
       pygame.display.update()
       time.sleep(3)
       break
    #if snakel[0][1] == 610:
        #show_text("Game Over",100,100,blue)
        #pygame.display.update()
       # time.sleep(3)
        #break
    #if snakel[0][1] == -10:
        #show_text("Game Over",100,100,blue)
        #pygame.display.update()
        #time.sleep(3)
        #break

    # Draw food
    pygame.draw.rect(screen, red,(foodx,foody,10,10))
    # draw snake
    for item in snakel:
        pygame.draw.rect(screen,color,(item[0],item[1],10,10))
        
    if foodx == snakel[0][0] and foody == snakel[0][1]:
        ateFood = True
        print(snakel)
        foodx = (random.randint(0,600) // 10 ) * 10
        foody = (random.randint(0,600) // 10 ) * 10
        pygame.draw.rect(screen,color,(snakel[0][0],snakel[0][1],10,10))
        snakel.insert(0,[snakex,snakey])
        score = score+1
        
        
        # print(snakel)
        
    
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                down = 1
                up = 0
                right = 0
                left = 0
            if event.key == K_UP:        
                up = 1
                down = 0
                right = 0
                left = 0
            if event.key == K_RIGHT: 
                right = 1
                down = 0
                up = 0
                left = 0
            if event.key == K_LEFT:
                left = 1
                down = 0
                up = 0
                right = 0
    if down == 1:

        snakey = snakey+10
        #for item in snakel:
            #item[1] = item[1] + 10
    if up == 1:
        snakey = snakey-10
        #for item in snakel:
            #item[1] = item[1] - 10
    if right == 1:
        snakex = snakex +10
        #for item in snakel:
            #item[0] = item[0]+10
    if left == 1:
        snakex = snakex-10
        #for item in snakel:
            #item[0] = item[0] - 10
    snakel.pop()
    '''if ateFood == True:   
        growth = snakel[0]
        if down == 1:
            growth[1] = growth[1] + 10
        if up == 1:
            growth[1] = growth[1] - 10
        if right == 1:
            growth[0] = growth[0] + 10
        if left == 1:
            growth[0] = growth[0] - 10
        snakel.insert(0,[growth[0], growth[1]])
        ateFood = False
    time.sleep(.1)
    '''
    pygame.time.delay(100)
