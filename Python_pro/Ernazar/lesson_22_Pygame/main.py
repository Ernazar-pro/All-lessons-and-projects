import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

x=50
y=50
width=40
height=60

run=True

while run:
    functs=pygame.event.get()
    for event in functs:
        if event.type == pygame.QUIT:
            run=False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=1
    if keys[pygame.K_RIGHT]:
        x+=1
    if keys[pygame.K_UP]:
        y-=1
    if keys[pygame.K_DOWN]:
        y+=1

    pygame.draw.rect(screen,'red',(x,y,width,height))
    pygame.display.update()
    screen.fill('black')


pygame.quit()