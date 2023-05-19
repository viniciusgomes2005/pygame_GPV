import pygame
import os
from config import Player_largura, Player_altura, Zumbi_largura, Zumbie_altura, IMG_DIR, SND_DIR, FNT_DIR
def load_assets():
    assets = {}
    
    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        
    return assets