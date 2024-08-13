import pygame

pygame.init()
dis = pygame.display.set_mode((500,500))
pygame.display.set_caption("my space invader")


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()