import pygame
import random

win=800
size=20
x=random.randrange(0,win,size)
y=random.randrange(0,win,size)
dx=0
dy=0
fps=10
pozition=[(x,y)]
lenth=1
food_x=random.randrange(0,win,size)
food_y=random.randrange(0,win,size)
eat_x=random.randrange(0,win,size)
eat_y=random.randrange(0,win,size)

pygame.init()

screen=pygame.display.set_mode((win,win))
clock=pygame.time.Clock()
font_score=pygame.font.SysFont('Arial',20)
font_GameOver=pygame.font.SysFont('Arial',80)
font_res=pygame.font.SysFont('Arial',20)
eat_sound=pygame.mixer.Sound('eat1.mp3')
pygame.mixer.music.load('fon.mp3')
pygame.mixer.music.play(-1)
pygame.display.set_caption('Snake')

run=True
while run:
    screen.fill('#768a49')
    text_score=font_score.render(f'Score: {lenth-1}',1,'black')
    screen.blit(text_score,(10,10))
    text_res=font_res.render('click SPACE to restart',1,'black')
    screen.blit(text_res,(600,750))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    #denesi
    for i,j in pozition:
        pygame.draw.rect(screen,'#930050',(i,j,size,size))
    #basi
    pygame.draw.rect(screen,'#56002f',(x,y,size,size))
    #awqat
    pygame.draw.rect(screen,'red',(food_x,food_y,size,size))
    pygame.draw.rect(screen,'yellow',(eat_x,eat_y,size,size))
    #juriw
    if x > 800 or y> 800 or x < 0 or y < 0 or len(pozition) != len(set(pozition)):
        print('GAME OVER')
        text_over=font_GameOver.render('GAME OVER!' , 1 , 'red')
        screen.blit(text_over,(200,400))
        pygame.mixer.stop()
    else:
        x+=dx*size
        y+=dy*size
        pozition.append((x,y))
        pozition=pozition[-lenth:]
    pygame.display.flip()
    clock.tick(fps)

    #awqat jew
    if pozition[-1]==(food_x,food_y):
        food_x=random.randrange(0,win,size)
        food_y=random.randrange(0,win,size)
        eat_x=random.randrange(0,win,size)
        eat_y=random.randrange(0,win,size)
        lenth+=1
        fps+=1
        print('Awqat jelindi')
        eat_sound.play()
    elif pozition[-1]==(eat_x,eat_y):
        eat_x=random.randrange(0,win,size)
        eat_y=random.randrange(0,win,size)
        food_x=random.randrange(0,win,size)
        food_y=random.randrange(0,win,size)
        lenth+=2
        fps+=1
        eat_sound.play()
    #basqariw
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w] and dy !=1:
        dy=-1
        dx=0
    if keys[pygame.K_s] and dy !=-1:
        dy=1
        dx=0
    if keys[pygame.K_d] and dx !=-1:
        dx=1
        dy=0
    if keys[pygame.K_a] and dx !=1:
        dx=-1
        dy=0
    if keys[pygame.K_SPACE]:
        lenth=1
        fps=10
        x=random.randrange(0,win,size)
        y=random.randrange(0,win,size)
        positions=[(x,y)]
        dx=0
        dy=0
        food_x=random.randrange(0,win,size)
        food_y=random.randrange(0,win,size)
        eat_x=random.randrange(0,win,size)
        eat_y=random.randrange(0,win,size)
        pygame.mixer.music.play(-1)


pygame.quit()