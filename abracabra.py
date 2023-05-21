import pygame
import random

# Inicialização do Pygame
pygame.init()

# Dimensões da janela
altura_janela = 1000
largura_janela = 800
window = pygame.display.set_mode((altura_janela, largura_janela))
pygame.display.set_caption('Pygame')

# Gera tela principal
game = True

# Posições das quadras
posicoes_quadra = [[-3600, 3500], [-3600, 2700], [-3600, 1900], [-3600, 1100], [-3600, 300], [-3600, -500],
                   [-3600, -1300], [-3600, -2100], [-3600, -2900], [-3600, -3700], [-2600, 3500], [-2600, 2700],
                   [-2600, 1900], [-2600, 1100], [-2600, 300], [-2600, -500], [-2600, -1300], [-2600, -2100],
                   [-2600, -2900], [-2600, -3700], [-1600, 3500], [-1600, 2700], [-1600, 1900], [-1600, 1100],
                   [-1600, 300], [-1600, -500], [-1600, -1300], [-1600, -2100], [-1600, -2900], [-1600, -3700],
                   [-600, 3500], [-600, 2700], [-600, 1900], [-600, 1100], [-600, 300], [-600, -500], [-600, -1300],
                   [-600, -2100], [-600, -2900], [-600, -3700], [400, 3500], [400, 2700], [400, 1900], [400, 1100],
                   [400, 300], [400, -500], [400, -1300], [400, -2100], [400, -2900], [400, -3700], [1400, 3500],
                   [1400, 2700], [1400, 1900], [1400, 1100], [1400, 300], [1400, -500], [1400, -1300], [1400, -2100],
                   [1400, -2900], [1400, -3700], [2400, 3500], [2400, 2700], [2400, 1900], [2400, 1100], [2400, 300],
                   [2400, -500], [2400, -1300], [2400, -2100], [2400, -2900], [2400, -3700], [3400, 3500],
                   [3400, 2700], [3400, 1900], [3400, 1100], [3400, 300], [3400, -500], [3400, -1300], [3400, -2100],
                   [3400, -2900], [3400, -3700], [4400, 3500], [4400, 2700], [4400, 1900], [4400, 1100], [4400, 300], [4400, -500], [4400, -1300],
                   [4400, -2100], [4400, -2900], [4400, -3700], [5400, 3500], [5400, 2700], [5400, 1900], [5400, 1100],
                   [5400, 300], [5400, -500], [5400, -1300], [5400, -2100], [5400, -2900], [5400, -3700]]

mapa_largura = 800 * 6  # Largura total do mapa
mapa_altura = 600 * 6  # Altura total do mapa
map_data = [[None] * 6 for _ in range(6)]  # Matriz 6x6 para representar o mapa

quadra_possivel = []
for i in range(36):
    quadra_possivel.append('assets/Sprites/Background cortado.png')

def gerar_bloco_aleatorio(quadra_possivel):
    blocos_possiveis = quadra_possivel  # Lista com os blocos possíveis (imagens, texturas, etc.)
    bloco_aleatorio = random.choice(blocos_possiveis)  # Escolhe aleatoriamente um bloco da lista
    return bloco_aleatorio

for i in range(6):
    for j in range(6):
        random_block = gerar_bloco_aleatorio(quadra_possivel)
        map_data[i][j] = random_block

# Carrega imagens
quarteirao_img = pygame.image.load('assets/Sprites/Background cortado.png').convert()
quarteirao_img = pygame.transform.scale(quarteirao_img, (1000, 800))
predio1_img = pygame.image.load('assets/Sprites/predio1.png').convert()
predio1_img = pygame.transform.scale(predio1_img, (300, 500))
# Classe para representar uma quadra
class Quadra(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y +=self.speedy
    def colisao(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)
class casa(pygame.sprite.Sprite):
    def __init__(self, img, quadra_x,quadra_y,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = quadra_x+x
        self.rect.y = quadra_y+y
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y +=self.speedy
predio1=[predio1_img,350,150]
casas=[predio1_img]*36

# Cria o grupo de sprites para o mapa
mapa = pygame.sprite.Group()
for i in range(6):
    for j in range(6):
        x = j * 1000 - 3600
        y = i * 800 - 2900
        quarteirao = Quadra(quarteirao_img, x, y)
        predio = casa(predio1[0],x,y,predio1[1],predio1[2])
        mapa.add(quarteirao,predio)

# Loop principal
clock = pygame.time.Clock()
FPS = 60

while game:
    clock.tick(FPS)

    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for quadra in mapa:
                    quadra.speedx += 8
            elif event.key == pygame.K_RIGHT:
                for quadra in mapa:
                    quadra.speedx -= 8
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                for quadra in mapa:
                    quadra.speedy += 8
            elif event.key == pygame.K_RIGHT:
                for quadra in mapa:
                    quadra.speedy -= 8 

    # Atualiza os sprites do mapa
    mapa.update()

    # Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    mapa.draw(window)

    # Atualiza a janela
    pygame.display.update()

# Finalização
pygame.quit()