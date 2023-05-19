# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import os

pygame.init()

# ----- Gera tela principal
Altura_janela = 800
Largura_janela = 600
window = pygame.display.set_mode((Altura_janela, Largura_janela))
pygame.display.set_caption('Pygame')

# ----- Inicia estruturas de dados
game = True
Posição_quadra=[[-3600, 3500],[-3600, 2700],[-3600, 1900],[-3600, 1100],[-3600, 300],[-3600, -500],[-3600, -1300]
,[-3600, -2100],[-3600, -2900],[-3600, -3700],[-2600, 3500],[-2600, 2700],[-2600, 1900],[-2600, 1100],[-2600, 300]
,[-2600, -500],[-2600, -1300],[-2600, -2100],[-2600, -2900],[-2600, -3700],[-1600, 3500],[-1600, 2700],[-1600, 1900]
,[-1600, 1100],[-1600, 300],[-1600, -500],[-1600, -1300],[-1600, -2100],[-1600, -2900],[-1600, -3700],[-600, 3500]
,[-600, 2700],[-600, 1900],[-600, 1100],[-600, 300],[-600, -500],[-600, -1300],[-600, -2100],[-600, -2900],[-600, -3700]
,[400, 3500],[400, 2700],[400, 1900],[400, 1100],[400, 300],[400, -500],[400, -1300],[400, -2100],[400, -2900],[400, -3700]
,[1400, 3500],[1400, 2700],[1400, 1900],[1400, 1100],[1400, 300],[1400, -500],[1400, -1300],[1400, -2100],[1400, -2900]
,[1400, -3700],[2400, 3500],[2400, 2700],[2400, 1900],[2400, 1100],[2400, 300],[2400, -500],[2400, -1300],[2400, -2100]
,[2400, -2900],[2400, -3700],[3400, 3500],[3400, 2700],[3400, 1900],[3400, 1100],[3400, 300],[3400, -500]
,[3400, -1300],[3400, -2100],[3400, -2900],[3400, -3700],[4400, 3500],[4400, 2700],[4400, 1900],[4400, 1100]
,[4400, 300],[4400, -500],[4400, -1300],[4400, -2100],[4400, -2900],[4400, -3700],[5400, 3500],[5400, 2700],[5400, 1900],
[5400, 1100],[5400, 300],[5400, -500],[5400, -1300],[5400, -2100],[5400, -2900],[5400, -3700]]

# ----- Inicia assets
quarteirao_img = pygame.image.load('C:/Users/gabri/OneDrive - Insper - Institudo de Ensino e Pesquisa/Insper/2023/1-semestre/DSoft(desing de software)/Sprites/Background cortado.png').convert()
quarteirao_img = pygame.transform.scale(quarteirao_img, (1000, 800)) 



class Quadra(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y= y
        self.speedx=2
    def atualiza(self):
        self.rect.x += self.speedx

Mapa=pygame.sprite.Group()
for posicao in Posição_quadra:
    x=posicao[0]-500
    y=posicao[1]
    Quarteirao=Quadra(quarteirao_img,x,y)
    Mapa.add(Quarteirao)

# ===== Tempo ====
clock = pygame.time.Clock()
FPS = 500
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                Quarteirao.speedx -= 8
            if event.key == pygame.K_RIGHT:
                Quarteirao.speedx += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                Quarteirao.speedx += 8
            if event.key == pygame.K_RIGHT:
                Quarteirao.speedx -= 8
    Mapa.update()
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    Mapa.draw(window)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
explosion_anim=[]
assets={}
for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets[EXPLOSION_ANIM] = explosion_anim
assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)