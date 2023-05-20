import pygame

pygame.init()

Altura_janela = 600
Largura_janela = 800
window = pygame.display.set_mode((Largura_janela,Altura_janela))
pygame.display.set_caption('Pygame')

quarteirao_img = pygame.image.load('assets/Sprites/Background cortado.png').convert()
quarteirao_img = pygame.transform.scale(quarteirao_img, (1000, 800))

Player_Normal_Anim = []
for i in range(1, 10):
    filename = 'assets/Sprites/Player_Normal{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (80, 100))
    Player_Normal_Anim.append(img)

Mapa = pygame.sprite.Group()
Player_Grupo = pygame.sprite.Group()

class Quadra(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

Posição_quadra = [[-3600, 3500], [-3600, 2700], [-3600, 1900], [-3600, 1100], [-3600, 300], [-3600, -500], [-3600, -1300],
                  [-3600, -2100], [-3600, -2900], [-3600, -3700], [-2600, 3500], [-2600, 2700], [-2600, 1900], [-2600, 1100],
                  [-2600, 300], [-2600, -500], [-2600, -1300], [-2600, -2100], [-2600, -2900], [-2600, -3700], [-1600, 3500],
                  [-1600, 2700], [-1600, 1900], [-1600, 1100], [-1600, 300], [-1600, -500], [-1600, -1300], [-1600, -2100],
                  [-1600, -2900], [-1600, -3700], [-600, 3500], [-600, 2700], [-600, 1900], [-600, 1100], [-600, 300],
                  [-600, -500], [-600, -1300], [-600, -2100], [-600, -2900], [-600, -3700], [400, 3500], [400, 2700],
                  [400, 1900], [400, 1100], [400, 300], [400, -500], [400, -1300], [400, -2100], [400, -2900], [400, -3700],
                  [1400, 3500], [1400, 2700], [1400, 1900], [1400, 1100], [1400, 300], [1400, -500], [1400, -1300], [1400, -2100],
                  [1400, -2900], [1400, -3700], [2400, 3500], [2400, 2700], [2400, 1900], [2400, 1100], [2400, 300], [2400, -500],
                  [2400, -1300], [2400, -2100], [2400, -2900], [2400, -3700], [3400, 3500], [3400, 2700], [3400, 1900], [3400, 1100],
                  [3400, 300], [3400, -500], [3400, -1300], [3400, -2100], [3400, -2900], [3400, -3700], [4400, 3500], [4400, 2700],
                  [4400, 1900], [4400, 1100], [4400, 300], [4400, -500], [4400, -1300], [4400, -2100], [4400, -2900], [4400, -3700],
                  [5400, 3500], [5400, 2700], [5400, 1900], [5400, 1100], [5400, 300], [5400, -500], [5400, -1300], [5400, -2100],
                  [5400, -2900], [5400, -3700]]

for posicao in Posição_quadra:
    x = posicao[0]
    y = posicao[1]
    speedx = 0
    speedy = 0
    quarteirao = Quadra(quarteirao_img, x, y, speedx, speedy)
    Mapa.add(quarteirao)

class Player(pygame.sprite.Sprite):
    def __init__(self, anim):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.anim = anim
        self.img = self.anim[self.frame]
        self.rect = self.img.get_rect()
        self.rect.center = (Largura_janela / 2, Altura_janela / 2)
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
            self.img = self.anim[self.frame]

Player_Grupo.add(Player(Player_Normal_Anim))

game = True
clock = pygame.time.Clock()
FPS = 70

while game:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    Mapa.update()
    Player_Grupo.update()
    
    window.fill((0, 0, 0))
    Mapa.draw(window)
    window.blit(Player_Grupo.sprites()[0].img, Player_Grupo.sprites()[0].rect)
    pygame.display.update()

pygame.quit()
