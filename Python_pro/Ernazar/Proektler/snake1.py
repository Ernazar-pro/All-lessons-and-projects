import pygame
import random

win=1320
x=random.randint(0,win)
y=random.randint(0,win)
size = 30
dx=0
dy=0
fps=15
lenth=10
positions=[(x,y)]

#baslaw
pygame.init()

#ekran jaratiw
screen=pygame.display.set_mode((win,win))
clock=pygame.time.Clock()

run=True
while run:
    screen.fill('#2E2E2E')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    for i,j in positions:
        pygame.draw.ellipse(screen,'#930050',(i,j,size,size))

    pygame.draw.ellipse(screen,'blue',(x,y,size,size))

    pygame.display.flip()
    clock.tick(fps)

    x+=dx*size/2
    y+=dy*size/2
    positions.append((x,y))
    positions = positions[-lenth:]
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dx !=1:
        dx = -1
        dy = 0
    if keys[pygame.K_RIGHT] and dx !=-1:
        dx = 1
        dy = 0
    if keys[pygame.K_UP] and dy !=1:
        dx = 0
        dy = -1
    if keys[pygame.K_DOWN] and dy !=-1:
        dx = 0
        dy = 1
    
#toqtatiw
pygame.quit()