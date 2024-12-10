import pygame



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

    class Bullet:
        def __init__(self, filename, width, height, x, y, speed):
            self.texture = pygame.image.load(filename)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed
            self.bullets = []



    def move(self):

       self.hitbox.y = self.speed

    def draw (self, window):
        window.blit(self.texture,self.hitbox)



    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            self.hitbox.x += self.speed
        if keys[pygame.K_z]:
            self.hitbox.x -= self.speed
            self.bullets.append(Bullet('bullet.png'))


            self.hitbox.x = self.hitbox.y
        for bullet in self.bullets:
            bullet.move()


class Bullet:
    def __init__(self):
        pass

    def move(self, filename):
        pass

    def draw(self):
        pass


pygame.init()

window = pygame.display.set_mode([700, 500])

background = pygame.image.load("galaxy.jpg")
background = pygame.transform.scale(background, window.get_size())
fps = pygame.time.Clock()

# cтворити обєкт ракети
player = Rocket("rocket.png", 65, 85, 250, 400, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    # викликати метод, який дозволяє рухатись ракеті
    player.move()

    window.fill([123, 123, 123])
    player.draw(window)

    # малювати ракету
    pygame.display.flip()

    fps.tick(60)




