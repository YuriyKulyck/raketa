import random

import pygame

#створити клас для ракет
class Rocket:
    def __init__(self, filename, width, height, x, y, speed):
        self.texture = pygame.image.load(filename)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []

    def draw(self, window):
        window.blit(self.texture, self.hitbox)
        for bullet in self.bullets:
            bullet.draw(window)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            self.hitbox.x += self.speed
        if keys[pygame.K_z]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_x]:
            self.bullets.append(Bullet("bullet.png",
                                       10, 10,
                                       self.hitbox.x, self.hitbox.y,
                                       10))
        for bullet in self.bullets:
            bullet.move()



class Bullet:
    def __init__(self,  filename, width, height, x, y, speed):
        self.texture = pygame.image.load(filename)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        self.hitbox.y -= self.speed


class Enemy:
    def __init__(self, filename, width, height, x, y, speed):
        self.texture = pygame.image.load(filename)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        self.hitbox.y += self.speed



pygame.init()

window = pygame.display.set_mode([700, 500])

background = pygame.image.load("galaxy.jpg")
background = pygame.transform.scale(background, window.get_size())
fps = pygame.time.Clock()

#cтворити обєкт ракети
player = Rocket("rocket.png",65, 85, 250, 400, 5)


enemies = []
y = 200
for i in range(10):
    enemies.append(Enemy("asteroid.png", 50, 50, random.randint(0, 650), y, 5))
    y -= 100

score = 0
score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [0,0,0])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [0, 0, 0])
    #викликати метод, який дозволяє рухатись ракеті
    for e in enemies:
        e.move()
        if e.hitbox.y > 500:
            e.hitbox.y = -100
            e.hitbox.x = random.randint(0, 650)

    for e in enemies:
        for b in player.bullets:
            if e.hitbox.colliderect(b.hitbox):
                b.hitbox.x = 5000
                player.bullets.remove(b)
                e.hitbox.y = -100
                e.hitbox.x = random.randint(0, 650)
                score += 1
                break

    player.move()

    window.fill([123,123,123])
    window.blit(score_lbl, [0,0])
    player.draw(window)
    for e in enemies:
        e.draw(window)
    #малювати ракету
    pygame.display.flip()

    fps.tick(60)

