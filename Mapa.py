# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random


pygame.init()

# ----- Gera tela principal
player_WIDTH = 120
player_HEIGHT = 122
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
player_img = pygame.image.load('assets/Sprites/Player_Normal1.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (player_WIDTH, player_HEIGHT))



zombie_img = pygame.image.load('assets/Sprites/Idle (1).png').convert_alpha()
zombie_img = pygame.transform.scale(zombie_img, (player_WIDTH, player_HEIGHT))

bullet_img = pygame.image.load('assets/Sprites/VIDA_1.png').convert_alpha()


pygame.display.set_caption('Hello World!')

#gera class


class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def atira(self):
        #atira
        new_bullet = Bullet(self.bullet_img, self.rect.top, self.rect.centerx)
        self.all_sprites.add(new_bullet)
        self.all_bullets.add(new_bullet)
            
class Zombie(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 200


    def move(self, speed=3):
        # Move em x
        if self.rect.x > player.rect.x:
            self.rect.x -= speed
        elif self.rect.x < player.rect.y:
            self.rect.x += speed
        # Move em y
        if self.rect.y < player.rect.y:
            self.rect.y += speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= speed
            
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial 
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 0 # velocidade
        self.speedx = 0 
        

    def update(self):
        # A bala move
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()




#  Inicia estruturas de dados
game = True

# aInicia assets
image = pygame.image.load('assets/Sprites/background cortado.png').convert()
image = pygame.transform.scale(image, (500, 600))

#posiciona
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60

# Criando um grupo
all_sprites = pygame.sprite.Group()
# Criando o jogador
player = Player(player_img)
all_sprites.add(player)
#criando zombies
zombie = Zombie(zombie_img)
all_sprites.add(zombie)

#grupo colisoes
zombies = pygame.sprite.Group()
zombies.add(zombie)

all_bullets = pygame.sprite.Group()

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
                player.speedx -= 4
            if event.key == pygame.K_RIGHT:
                player.speedx += 4
            if event.key == pygame.K_UP:
                player.speedy -= 4
            if event.key == pygame.K_DOWN:
                player.speedy += 4
                
            if event.key == pygame.K_SPACE:
                player.shoot()
                
                
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 4
            if event.key == pygame.K_RIGHT:
                player.speedx -= 4
            if event.key == pygame.K_UP:
                player.speedy += 4
            if event.key == pygame.K_DOWN:
                player.speedy -= 4
        
    zombie.move()



    # Atualiza estado do jogo
    all_sprites.update()

    # Verifica se houve colisão 
    hits = pygame.sprite.spritecollide(player, zombies, True)
    if len(hits)>0:
        game = False
        
    #  Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (10, 10))

    # Desenhando 
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit() 

