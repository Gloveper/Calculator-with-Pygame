import pygame
pygame.init()

height = 700
black = (0, 0, 0)
# white = (255, 255, 255)
grey = (142, 142, 147)
yellow = (255, 150, 0)

gameDisplay = pygame.display.set_mode((400, height))
pygame.display.set_caption('Calculator')

run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    gameDisplay.fill(black)

    for i in range(50, 300, 100):
        pygame.draw.circle(gameDisplay, grey, (i, 240), 40)

    for j in range(240, height, 100):
        pygame.draw.circle(gameDisplay, yellow, (350, j), 40)

    for i in range(50, 300, 100):
        for j in range(340, height, 100):
            pygame.draw.circle(gameDisplay, (80, 80, 80), (i,j), 40)

    pygame.draw.rect(gameDisplay, (80, 80, 80), (50, 600, 100, 80))

    pygame.display.update()

pygame.quit()
quit()


