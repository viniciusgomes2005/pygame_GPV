import pygame
import os
from config import Player_largura, Player_altura, Zumbi_largura, Zumbie_altura, IMG_DIR, SND_DIR, FNT_DIR
Normal_anim='animação player normal'


def load_assets():
    assets = {}
    casas = []
    Player_Normal_Anim=[]
    Zombie_Anim=[]
    Vida_Anim=[]
    Player_Normal_E_Anim=[]

    ####  JOGADOR  #######
    for i in range(1,11):
        Player_Normal = 'assets/Sprites/Player_Normal{}.png'.format(i)
        Player_Normal_img = pygame.image.load(Player_Normal).convert_alpha()
        Player_Normal_img = pygame.transform.scale(Player_Normal_img, (120, 130))
        Player_Normal_Anim.append(Player_Normal_img)

    for i in range(1,9):
        Player_Run = 'assets/Sprites/Player_Run{}.png'.format(i)
        Player_Run_img = pygame.image.load(Player_Run).convert_alpha()
        Player_Run_img = pygame.transform.scale(Player_Run_img, (120, 130))
        Player_Normal_Anim.append(Player_Run_img)

    for i in range(1,8):
        Player_Ataca = 'assets/Sprites/Player_atacar{}.png'.format(i)
        Player_Ataca_img = pygame.image.load(Player_Ataca).convert_alpha()
        Player_Ataca_img = pygame.transform.scale(Player_Ataca_img, (120, 130))
        Player_Normal_Anim.append(Player_Ataca_img)

    for i in range(1,9):
        Player_Run = 'assets/Sprites/Player_i_Run{}.png'.format(i)
        Player_Run_img = pygame.image.load(Player_Run).convert_alpha()
        Player_Run_img = pygame.transform.scale(Player_Run_img, (120, 130))
        Player_Normal_E_Anim.append(Player_Run_img)

    for i in range(1,8):
        Player_Ataca = 'assets/Sprites/Player_i_atacar{}.png'.format(i)
        Player_Ataca_img = pygame.image.load(Player_Ataca).convert_alpha()
        Player_Ataca_img = pygame.transform.scale(Player_Ataca_img, (120, 130))
        Player_Normal_E_Anim.append(Player_Ataca_img)
    
    for i in range(1,4):
        Player_shot='assets/Sprites/Player_Shot{}.png'.format(i)
        Player_shot_img= pygame.image.load(Player_shot).convert_alpha()
        Player_shot_img= pygame.transform.scale(Player_shot_img, (120, 130))
        Player_Normal_Anim.append(Player_shot_img)
    
    for i in range(1,4):
        Player_shot='assets/Sprites/Player_i_Shot{}.png'.format(i)
        Player_shot_i_img= pygame.image.load(Player_shot).convert_alpha()
        Player_shot_i_img= pygame.transform.scale(Player_shot_i_img, (120, 130))
        Player_Normal_E_Anim.append(Player_shot_i_img)

    for i in range(1,11):#10
        Zombie_Run = 'assets/Sprites/Walk ({}).png'.format(i)
        Zombie_Run_img = pygame.image.load(Zombie_Run).convert_alpha()
        Zombie_Run_img = pygame.transform.scale(Zombie_Run_img, (120, 130))
        Zombie_Anim.append(Zombie_Run_img)

    for i in range(1,9):#11-18
        Zombie_Ataca = 'assets/Sprites/Attack ({}).png'.format(i)
        Zombie_Ataca_img = pygame.image.load(Zombie_Ataca).convert_alpha()
        Zombie_Ataca_img = pygame.transform.scale(Zombie_Ataca_img, (120, 130))
        Zombie_Anim.append(Zombie_Ataca_img)

    for i in range(1,13):#19-30
        Zombie_Morre = 'assets/Sprites/Dead ({}).png'.format(i)
        Zombie_Morre_img = pygame.image.load(Zombie_Morre).convert_alpha()
        Zombie_Morre_img = pygame.transform.scale(Zombie_Morre_img, (120, 130))
        Zombie_Anim.append(Zombie_Morre_img)
    
    for i in range(10,-1,-1):
        Vida= 'assets/Sprites/VIDA_{}.png'.format(i)
        Vida_img= pygame.image.load(Vida).convert_alpha()
        Vida_img = pygame.transform.scale(Vida_img, (400, 50))
        Vida_Anim.append(Vida_img)
    for i in range(1,11): #31-41
        zumbi='assets/Sprites/Walk2 ({}).png'.format(i)
        zumbi_img = pygame.image.load(zumbi).convert_alpha()
        zumbi_img=pygame.transform.scale(zumbi_img, (120, 130))
        Zombie_Anim.append(zumbi_img)
    
    assets['Player_Normal_Anim'] = Player_Normal_Anim
    assets['Zombie_Anim']=Zombie_Anim
    assets['Vida_Anim']=Vida_Anim
    assets['Player_Normal_E_Anim']=Player_Normal_E_Anim

    bullet= 'assets/Sprites/bullet.png'
    bullet_img= pygame.image.load(bullet).convert_alpha()
    bullet_img = pygame.transform.scale(bullet_img, (50, 50))
    assets['bullet_img']=bullet_img
    predio1_img = pygame.image.load('assets/Sprites/predio1.png').convert_alpha()
    predio1_img = pygame.transform.scale(predio1_img, (300, 500))
    predio1=[predio1_img,350,150]
    casas.append(predio1)
    igreja_img = pygame.image.load('assets/Sprites/igreja.png').convert_alpha()
    igreja_img = pygame.transform.scale(igreja_img, (300, 500))
    igreja=[igreja_img,350,150]
    casas.append(igreja)
    casa1_img = pygame.image.load('assets/Sprites/casa1.png').convert_alpha()
    casa1_img = pygame.transform.scale(casa1_img, (575, 475))
    casa1=[casa1_img,210,180]
    casas.append(casa1)
    casas.append(casa1)
    casa2_img = pygame.image.load('assets/Sprites/casa2.png').convert_alpha()
    casa2_img = pygame.transform.scale(casa2_img, (570, 500))
    casa2=[casa2_img,230,120]
    casas.append(casa2)
    casas.append(casa2)
    casa3_img = pygame.image.load('assets/Sprites/casa3.png').convert_alpha()
    casa3_img = pygame.transform.scale(casa3_img, (300, 300))
    casa3=[casa3_img,325,250]
    casas.append(casa3)
    casas.append(casa3)
    casa4_img = pygame.image.load('assets/Sprites/casa4.png').convert_alpha()
    casa4_img = pygame.transform.scale(casa4_img, (575, 475))
    casa4=[casa4_img,225,145]
    casas.append(casa4)
    casas.append(casa4)
    supermercado_img = pygame.image.load('assets/Sprites/super-mercado.png').convert_alpha()
    supermercado_img = pygame.transform.scale(supermercado_img, (575, 475))
    supermercado=[supermercado_img,220,145]
    casas.append(supermercado)
    predio2_img = pygame.image.load('assets/Sprites/Prédio 2.png').convert_alpha()
    predio2_img = pygame.transform.scale(predio2_img, (550,450))
    predio2=[predio2_img,230,170]
    casas.append(predio2)
    casas.append(predio2)
    predio3_img = pygame.image.load('assets/Sprites/Prédio 3.png').convert_alpha()
    predio3_img = pygame.transform.scale(predio3_img, (600, 500))
    predio3=[predio3_img,200,120]
    casas.append(predio3)	
    casas.append(predio3)
    pizzaria_img = pygame.image.load('assets/Sprites/pizzaria.png').convert_alpha()
    pizzaria_img = pygame.transform.scale(pizzaria_img, (600, 550))
    pizzaria=[pizzaria_img,200,150]
    casas.append(pizzaria)
    farmacia_img = pygame.image.load('assets/Sprites/farmacia.png').convert_alpha()
    farmacia_img = pygame.transform.scale(farmacia_img, (550, 450))
    farmacia=[farmacia_img,225,170]
    casas.append(farmacia)
    escola_img = pygame.image.load('assets/Sprites/escola.png').convert_alpha()
    escola_img = pygame.transform.scale(escola_img, (600, 500))
    escola=[escola_img,200,130]
    casas.append(escola)
    casa5_img = pygame.image.load('assets/Sprites/casa5.png').convert_alpha()
    casa5_img = pygame.transform.scale(casa5_img, (730, 475))
    casa5=[casa5_img,150,145]
    casas.append(casa5)
    casas.append(casa5)
    casa6_img = pygame.image.load('assets/Sprites/casa6.png').convert_alpha()
    casa6_img = pygame.transform.scale(casa6_img, (520, 500))
    casa6=[casa6_img,240,120]
    casas.append(casa6)
    casas.append(casa6)
    casa7_img = pygame.image.load('assets/Sprites/casa7.png').convert_alpha()
    casa7_img = pygame.transform.scale(casa7_img, (775, 500))
    casa7=[casa7_img,120,150]
    casas.append(casa7)
    casa8_img = pygame.image.load('assets/Sprites/casa8.png').convert_alpha()
    casa8_img = pygame.transform.scale(casa8_img, (800, 625))
    casa8=[casa8_img,110,100]
    casas.append(casa8)
    casa9_img = pygame.image.load('assets/Sprites/casa9.png').convert_alpha()
    casa9_img = pygame.transform.scale(casa9_img, (600,600))
    casa9=[casa9_img,180,90]
    casas.append(casa9)
    casa10_img = pygame.image.load('assets/Sprites/casa10.png').convert_alpha()
    casa10_img = pygame.transform.scale(casa10_img, (575, 475))
    casa10=[casa10_img,200,150]
    casas.append(casa10)
    casas.append(casa10)
    casa11_img = pygame.image.load('assets/Sprites/casa11.png').convert_alpha()
    casa11_img = pygame.transform.scale(casa11_img, (600, 500))
    casa11=[casa11_img,200,120]
    casas.append(casa11)
    casa12_img = pygame.image.load('assets/Sprites/casa12.png').convert_alpha()
    casa12_img = pygame.transform.scale(casa12_img, (650, 550))
    casa12=[casa12_img,170,110]
    casas.append(casa12)
    casas.append(casa12)
    casa13_img = pygame.image.load('assets/Sprites/casa13.png').convert_alpha()
    casa13_img = pygame.transform.scale(casa13_img, (550, 450))
    casa13=[casa13_img,230,170]
    casas.append(casa13)
    casas.append(casa13)
    casa14_img = pygame.image.load('assets/Sprites/casa14.png').convert_alpha()
    casa14_img = pygame.transform.scale(casa14_img, (900, 750))
    casa14=[casa14_img,90,0]
    casas.append(casa14)
    casa15_img = pygame.image.load('assets/Sprites/casa15.png').convert_alpha()
    casa15_img = pygame.transform.scale(casa15_img, (600, 500))
    casa15=[casa15_img,200,120]
    casas.append(casa15)
    casa16_img = pygame.image.load('assets/Sprites/casa16.png').convert_alpha()
    casa16_img = pygame.transform.scale(casa16_img, (500, 400))
    casa16=[casa16_img,250,200]
    casas.append(casa16)
    casas.append(casa16)
    assets["casas"] = casas
    return assets
