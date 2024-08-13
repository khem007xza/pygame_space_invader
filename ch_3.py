import pygame

pygame.init()
dis = pygame.display.set_mode((500,500))
pygame.display.set_caption("my space invader")

class Player():
    def __init__(self, x, y):
        self.image = pygame.image.load("image/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        dx = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx -= 1
        if key[pygame.K_d]:
            dx += 1

        self.rect.x += dx
        dis.blit(self.image, self.rect)

clock = pygame.time.Clock()
player = Player(240,450)

run = True
while run:
    clock.tick(60)
    dis.fill ((255 , 255 , 255)) 
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()