import pygame



class Rocket:
    def __init__(self, speet, width, height, x, y, skin):
        self.textura = pygame.image.load(skin)
        self.textura = pygame.transform.scale(self.textura, [width, height])
        self.hitbox = self.textura.get_rect()
        self.hitbox.x= x
        self.hitbox.y = y
        self.speet = speet


    def draw(self, window):
        window.blit(self.textura, self.hitbox)


background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background,[700, 500])

pygame.init()

window =pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    window.fill([255, 0, 0])
    window.blit(background, [0,0])
    pygame.display.flip()

    fps.tick(90)



