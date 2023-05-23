import pygame
import os
from config import Player_largura, Player_altura, Zumbi_largura, Zumbie_altura, IMG_DIR, SND_DIR, FNT_DIR
Normal_anim='animação player normal'
casas = []

def load_assets():
    assets = {}
    Normal_Anim=[]
    for i in range(10):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'Player_Normal{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (Player_largura, Player_altura))
        Normal_Anim.append(img)
    assets[Normal_anim] = Normal_Anim
    return assets
predio1_img = pygame.image.load('assets/Sprites/predio1.png').convert_alpha()
predio1_img = pygame.transform.scale(predio1_img, (300, 500))
predio1=[predio1_img,350,150]
casas.append(predio1)
igreja_img = pygame.image.load('assets/Sprites/igreja.png').convert_alpha()
igreja_img = pygame.transform.scale(igreja_img, (300, 500))
igreja=[igreja_img,350,150]
casas.append(igreja)
casa1_img = pygame.image.load('assets/Sprites/casa1.png').convert_alpha()
casa1_img = pygame.transform.scale(casa1_img, (300, 500))
casa1=[casa1_img,350,150]
casas.append(casa1)
casas.append(casa1)
casa2_img = pygame.image.load('assets/Sprites/casa2.png').convert_alpha()
casa2_img = pygame.transform.scale(casa2_img, (300, 500))
casa2=[casa2_img,350,150]
casas.append(casa2)
casas.append(casa2)
casa3_img = pygame.image.load('assets/Sprites/casa3.png').convert_alpha()
casa3_img = pygame.transform.scale(casa3_img, (300, 500))
casa3=[casa3_img,350,150]
casas.append(casa3)
casas.append(casa3)
casa4_img = pygame.image.load('assets/Sprites/casa4.png').convert_alpha()
casa4_img = pygame.transform.scale(casa4_img, (300, 500))
casa4=[casa4_img,350,150]
casas.append(casa4)
casas.append(casa4)
supermercado_img = pygame.image.load('assets/Sprites/super-mercado.png').convert_alpha()
supermercado_img = pygame.transform.scale(supermercado_img, (300, 500))
supermercado=[supermercado_img,350,150]
casas.append(supermercado)
predio2_img = pygame.image.load('assets/Sprites/Prédio 2.png').convert_alpha()
predio2_img = pygame.transform.scale(predio2_img, (300, 500))
predio2=[predio2_img,350,150]
casas.append(predio2)
casas.append(predio2)
predio3_img = pygame.image.load('assets/Sprites/Prédio 3.png').convert_alpha()
predio3_img = pygame.transform.scale(predio3_img, (300, 500))
predio3=[predio3_img,350,150]
casas.append(predio3)	
casas.append(predio3)
pizzaria_img = pygame.image.load('assets/Sprites/pizzaria.png').convert_alpha()
pizzaria_img = pygame.transform.scale(pizzaria_img, (300, 500))
pizzaria=[pizzaria_img,350,150]
casas.append(pizzaria)
farmacia_img = pygame.image.load('assets/Sprites/farmacia.png').convert_alpha()
farmacia_img = pygame.transform.scale(farmacia_img, (300, 500))
farmacia=[farmacia_img,350,150]
casas.append(farmacia)
escola_img = pygame.image.load('assets/Sprites/escola.png').convert_alpha()
escola_img = pygame.transform.scale(escola_img, (300, 500))
escola=[escola_img,350,150]
casas.append(escola)
casa5_img = pygame.image.load('assets/Sprites/casa5.png').convert_alpha()
casa5_img = pygame.transform.scale(casa5_img, (300, 500))
casa5=[casa5_img,350,150]
casas.append(casa5)
casas.append(casa5)
casa6_img = pygame.image.load('assets/Sprites/casa6.png').convert_alpha()
casa6_img = pygame.transform.scale(casa6_img, (300, 500))
casa6=[casa6_img,350,150]
casas.append(casa6)
casas.append(casa6)
casa7_img = pygame.image.load('assets/Sprites/casa7.png').convert_alpha()
casa7_img = pygame.transform.scale(casa7_img, (300, 500))
casa7=[casa7_img,350,150]
casas.append(casa7)
casa8_img = pygame.image.load('assets/Sprites/casa8.png').convert_alpha()
casa8_img = pygame.transform.scale(casa8_img, (300, 500))
casa8=[casa8_img,350,150]
casas.append(casa8)
casa9_img = pygame.image.load('assets/Sprites/casa9.png').convert_alpha()
casa9_img = pygame.transform.scale(casa9_img, (300, 500))
casa9=[casa9_img,350,150]
casas.append(casa9)
casa10_img = pygame.image.load('assets/Sprites/casa10.png').convert_alpha()
casa10_img = pygame.transform.scale(casa10_img, (300, 500))
casa10=[casa10_img,350,150]
casas.append(casa10)
casas.append(casa10)