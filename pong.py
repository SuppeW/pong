import random, pygame

pygame.init()

win = pygame.display.set_mode((600,400))
pygame.display.set_caption("PONG")

win.fill((0,0,0))
pygame.display.update()

x, y = 5, 5
bally = 600
startpos = random.randint(5, 395)


pygame.draw.rect(win, (255,255,255),(x,y, 5,30))

vel = 5



run = True
while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and y < 400-30-vel:
        y+= vel
    if keys[pygame.K_UP] and y > vel:
        y-= vel
    if bally < 10 and y ==:
        bally = 600
        startpos = random.randint(5, 395)

    bally -= vel

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,255,255), (bally,startpos, 5,5))
    pygame.draw.rect(win,(255,255,255), (x,y,5,30))
    pygame.display.update()

pygame.quit()
