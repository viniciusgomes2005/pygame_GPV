import pygame
import os
from config import Player_largura, Player_altura, Zumbi_largura, Zumbie_altura, IMG_DIR, SND_DIR, FNT_DIR
Normal_anim='animação player normal'


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
