import sys, pygame

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

rectX = 50
rectY = 240 - 50
velX, velY = 0, 0
speed = 0.5
jump = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    dt = clock.tick(60)
    
    pressed = pygame.key.get_pressed()

    velX = 0
    if pressed[pygame.K_LEFT]:
        velX = -speed
    if pressed[pygame.K_RIGHT]:
        velX = speed

    if (velY == 0) and pressed[pygame.K_SPACE]:
        velY = -0.8
        jump = True
    if jump and velY < 0.8:
       velY += 0.05
    elif rectY > (240 - 50):
        velY = 0
        rectY = 240 - 50
        jump = False

    rectX += velX * dt
    rectY += velY * dt

    screen.fill(black)
    pygame.draw.rect(screen, white, (rectX, rectY, 50, 50), 0)
    pygame.display.flip()
