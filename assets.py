import pygame
import os
from config import Player_largura, Player_altura, Zumbi_largura, Zumbie_altura, IMG_DIR, SND_DIR, FNT_DIR
construcoes = []
predio1_img = pygame.image.load('assets/Sprites/predio1.png').convert()
predio1_img = pygame.transform.scale(predio1_img, (300, 500))
predio1=[predio1_img,350,150]
construcoes.append(predio1)
predio2_img = pygame.image.load('assets/Sprites/Prédio 2.png').convert()
predio2_img = pygame.transform.scale(predio2_img, (300, 500))
predio2=[predio2_img,350,150]
construcoes.append(predio2)
predio3_img = pygame.image.load('assets/Sprites/Prédio 3.png').convert()
predio3_img = pygame.transform.scale(predio3_img, (300, 500))
predio3=[predio3_img,350,150]
construcoes.append(predio3)
igreja_img = pygame.image.load('assets/Sprites/igreja.png').convert()
igreja_img = pygame.transform.scale(igreja_img, (300, 500))
igreja = [igreja_img,350,150]
construcoes.append(igreja)
casa1_img = pygame.image.load('assets/Sprites/casa1.png').convert()
casa1_img = pygame.transform.scale(casa1_img, (300, 500))
casa1 = [casa1_img,350,150]
construcoes.append(casa1)
casa2_img = pygame.image.load('assets/Sprites/casa2.png').convert()
casa2_img = pygame.transform.scale(casa2_img, (300, 500))
casa2 = [casa2_img,350,150]
construcoes.append(casa2)
casa3_img = pygame.image.load('assets/Sprites/casa3.png').convert()
casa3_img = pygame.transform.scale(casa3_img, (300, 500))
casa3 = [casa3_img,350,150]
construcoes.append(casa3)
def load_assets():
    assets = {}
    
    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))

    return assets