import pygame

pygame.init()
dis = pygame.display.set_mode((500,500))
pygame.display.set_caption("my space invader")
font = pygame.font.Font(pygame.font.get_default_font(), 20)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("image\\bullet.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
    
	def update(self):
		self.rect.y -= 1
		if enemy.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
			enemy.die()
			self.kill()
			player.score += 1
		dis.blit(self.image, self.rect)

class Player():
    def __init__(self, x, y):
        self.image = pygame.image.load("image\player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullet_group = pygame.sprite.Group()
        self.last_shot = pygame.time.get_ticks()
        self.score = 0

    def update(self):
        dx = 0
        cooldown = 300
        key = pygame.key.get_pressed()
        time_now = pygame.time.get_ticks()
        
        if key[pygame.K_a]:
            dx -= 1
        if key[pygame.K_d]:
            dx += 1
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullet(self.rect.x+12, self.rect.y)
            self.bullet_group.add(bullet)
            self.last_shot = time_now

        self.rect.x += dx
        dis.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("image\invader.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1
        
		dis.blit(self.image, self.rect)
	def die(self):
		self.kill()
		enemy_group.remove(self)
    
clock = pygame.time.Clock()

player = Player(240,450)

enemy_group = pygame.sprite.Group()
enemy = Enemy(240, 100)
enemy_group.add(enemy)

run = True

scoreX = 400
scoreY = 20

while run:
    clock.tick(60)
    dis.fill ((255 , 255 , 255))
    ScoreText = font.render("Score: " +str(player.score), True , 0)
    dis.blit (ScoreText, (scoreX, scoreY))
    player.update()
    enemy_group.update()
    player.bullet_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()