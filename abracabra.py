import os
import pygame
import sys
import random
from assets import *

# Inicialização do Pygame
pygame.init()

######################  JANELA  #############################

# Dimensões da janela
altura_janela = 800
largura_janela = 1000
window = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Pygame')

#####################  SPRITES  ################################
assets=load_assets()
quarteirao_img = pygame.image.load('assets/Sprites/Background cortado.png').convert()
quarteirao_img = pygame.transform.scale(quarteirao_img, (1000, 800))
zombie_img = pygame.image.load('assets/Sprites/Idle (1).png').convert_alpha()
zombie_img = pygame.transform.scale(zombie_img, (120, 130))
htp = pygame.image.load('assets/Sprites/oie_transparent (6) (1) (1) (2).png')
htp = pygame.transform.scale(htp,(800,600))
gameover=pygame.image.load('assets/Sprites/gameover (1).png')
gameover=pygame.transform.scale(gameover,(800,600))
Parado=1
Correndo=2
Facada=3
Shot=4
fonte=pygame.font.SysFont("Comic Sans MS",60)
################################  GRUPOS  ####################################

Player_Grupo= pygame.sprite.Group()
Construcoes_Grupo= pygame.sprite.Group()
Zombie_Grupo = pygame.sprite.Group()
mapa = pygame.sprite.Group()
bullet_Grupo = pygame.sprite.Group()

posicoes_quadra = posicoes_quadra = [[-3600, 3500], [-3600, 2700], [-3600, 1900], [-3600, 1100], [-3600, 300], [-3600, -500],[-3600, -1300], [-3600, -2100], [-3600, -2900], [-3600, -3700], [-2600, 3500], [-2600, 2700],[-2600, 1900], [-2600, 1100], [-2600, 300], [-2600, -500], [-2600, -1300], [-2600, -2100],[-2600, -2900], [-2600, -3700], [-1600, 3500], [-1600, 2700], [-1600, 1900], [-1600, 1100],[-1600, 300], [-1600, -500], [-1600, -1300], [-1600, -2100], [-1600, -2900], [-1600, -3700],[-600, 3500], [-600, 2700], [-600, 1900], [-600, 1100], [-600, 300], [-600, -500], [-600, -1300],[-600, -2100], [-600, -2900], [-600, -3700], [400, 3500], [400, 2700], [400, 1900], [400, 1100],[400, 300], [400, -500], [400, -1300], [400, -2100], [400, -2900], [400, -3700], [1400, 3500],[1400, 2700], [1400, 1900], [1400, 1100], [1400, 300], [1400, -500], [1400, -1300], [1400, -2100],[1400, -2900], [1400, -3700], [2400, 3500], [2400, 2700], [2400, 1900], [2400, 1100], [2400, 300],[2400, -500], [2400, -1300], [2400, -2100], [2400, -2900], [2400, -3700], [3400, 3500],[3400, 2700], [3400, 1900], [3400, 1100], [3400, 300], [3400, -500], [3400, -1300], [3400, -2100],[3400, -2900], [3400, -3700], [4400, 3500], [4400, 2700], [4400, 1900], [4400, 1100], [4400, 300], [4400, -500], [4400, -1300],[4400, -2100], [4400, -2900], [4400, -3700], [5400, 3500], [5400, 2700], [5400, 1900], [5400, 1100],[5400, 300], [5400, -500], [5400, -1300], [5400, -2100], [5400, -2900], [5400, -3700]]
mapa_largura = 800 * 6  # Largura total do mapa
mapa_altura = 600 * 6  # Altura total do mapa
map_data = [[None] * 6 for _ in range(6)]  # Matriz 6x6 para representar o mapa

quadra_possivel = []
for i in range(36):
    quadra_possivel.append('assets/Sprites/Background cortado.png')

def gerar_bloco_aleatorio(quadra_possivel):
    bloco_aleatorio = random.choice(quadra_possivel)
    del quadra_possivel[quadra_possivel.index(bloco_aleatorio)]
    return bloco_aleatorio

###############################  CLASSES  #################################

class Quadra(pygame.sprite.Sprite): # Classe para representar uma quadra
    def __init__(self, img, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = img # define imagem
        self.rect = self.image.get_rect() #torna imagem em um retangulo
        self.rect.x = x # X do canto superior esquerdo do retangulo
        self.rect.y = y # Y do canto superior esquerdo do retangulo
        self.speedx = speedx # VELOCIDADE DO PLAYER NO EIXO X
        self.speedy = speedy # VELOCIDADE DO PLAYER NO EIXO Y

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    
class casa(pygame.sprite.Sprite):
    def __init__(self, img, quadra_x,quadra_y,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask= pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = quadra_x+x
        self.rect.y = quadra_y+y
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y +=self.speedy

class Player(pygame.sprite.Sprite):
    def __init__(self,anim,anim2,move, direcao):
        pygame.sprite.Sprite.__init__(self)
        self.frame=0
        self.anim=anim
        self.anim2=anim2
        self.img=self.anim[self.frame]
        self.mask= pygame.mask.from_surface(self.img)
        self.rect=self.img.get_rect()
        self.rect.center = (largura_janela/2, altura_janela/ 2)
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks=50
        self.move=move #1=sim 2=não
        self.direcao=direcao
    def update(self):
        now=pygame.time.get_ticks()
        elapsed_ticks= now - self.last_update
        if self.move==Parado:
            if elapsed_ticks>self.frame_ticks:
                self.last_update=now
                self.frame+=1
                if self.frame >= 10:
                    self.frame=0
                self.img=self.anim[self.frame]
        elif self.move==Correndo:
            if elapsed_ticks>self.frame_ticks:
                if self.direcao==1:
                    if self.frame<10 or self.frame >= 17:
                        self.frame=10
                    else:
                        self.frame+=1
                    self.last_update=now
                    self.img=self.anim[self.frame]
                elif self.direcao == 2:
                    if self.frame>=7:
                        self.frame=0
                    else:
                        self.frame+=1
                    self.last_update=now
                    self.img=self.anim2[self.frame]
        elif self.move==Facada: 
            if elapsed_ticks>self.frame_ticks:
                if self.direcao==1:
                    if self.frame<18 or self.frame>=25:
                        self.frame=18
                    else:
                        self.frame+=1
                    self.last_update=now
                    self.img=self.anim[self.frame]
                    if self.frame==24:
                        self.move=Correndo
                        self.direcao=1
                        self.frame=10
                elif self.direcao==2:
                    if self.frame<8 or self.frame>14:
                        self.frame=8
                    else:
                        self.frame+=1
                    self.last_update=now
                    self.img=self.anim2[self.frame]
                    if self.frame==14:
                        self.move=Correndo
                        self.direcao=2
                        self.frame=0
        elif self.move==Shot:
            if elapsed_ticks>self.frame_ticks:
                if self.direcao==1:
                    if self.frame<25 or self.frame>=28:
                        self.frame=25
                    else:
                        self.frame+=1
                    self.last_update=now
                    self.img=self.anim[self.frame]
                    if self.frame>=27:
                        self.move=Correndo
                        self.direcao=1
                        self.frame=10
                elif self.direcao==2:
                    if self.frame<15 or self.frame>19:
                        self.frame=15
                    else:
                        self.frame+=1
                    self.last_update=now
                    self.img=self.anim2[self.frame]
                    if self.frame==17:
                        self.move=Correndo
                        self.direcao=2
                        self.frame=0
    def shot(self,b_shoot):
        new_bullet = Bullet(assets['bullet_img'],  altura_janela/2-40, largura_janela/2-20, b_shoot)
        bullet_Grupo.add(new_bullet)

class Zombie(pygame.sprite.Sprite):
    def __init__(self, anim, speedx, speedy,speedxmap,speedymap,x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frame=0
        self.anim=anim
        self.img=self.anim[self.frame]
        self.mask= pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect()
        self.rect.x =  x
        self.rect.y = y
        self.speedy = speedy
        self.speedx = speedx
        self.speedxmap = speedxmap
        self.speedymap = speedymap
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks=50
        self.direcao_z=1
    def move(self):
        # Move em x
        if self.speedx>-1:
            if self.rect.x > P1.rect.x:
                self.rect.x -= self.speedx
                self.direcao_z=2
            elif self.rect.x < P1.rect.x:
                self.rect.x += self.speedx
                self.direcao_z=1
            # Move em y
            if self.rect.y < P1.rect.y:
                self.rect.y += self.speedy
            elif self.rect.y > P1.rect.y:
                self.rect.y -= self.speedy
        else:
            deltax=self.rect.x-P1.rect.x
            deltax=abs(deltax)
            deltay=self.rect.y-P1.rect.y
            deltay=abs(deltay)
            if deltax<50 and deltax<50:
                self.speedx*=-1
                self.speedy*=-1
            else:
                if self.rect.x > P1.rect.x:
                    self.rect.x -= self.speedx
                    self.direcao_z=1
                elif self.rect.x < P1.rect.x:
                    self.rect.x += self.speedx
                    self.direcao_z=2
                # Move em y
                if self.rect.y < P1.rect.y:
                    self.rect.y += self.speedy
                elif self.rect.y > P1.rect.y:
                    self.rect.y -= self.speedy
    def update(self):
        self.rect.x += self.speedxmap
        self.rect.y += self.speedymap
    def Animacao(self):
        now=pygame.time.get_ticks()
        elapsed_ticks= now - self.last_update
        if elapsed_ticks>self.frame_ticks:
            if self.direcao_z==1:
                self.last_update=now
                if self.frame >= 10:
                    self.frame=0
                else:
                    self.frame+=1
                self.img=self.anim[self.frame]
            elif self.direcao_z==2:
                self.last_update=now
                if self.frame<31 or self.frame>=39:
                    self.frame=31
                else:
                    self.frame+=1
                self.img=self.anim[self.frame]

class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, bullet_img, y, x, b_speed):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.img = bullet_img
        self.rect = self.img.get_rect()
        self.mask= pygame.mask.from_surface(self.img)
        self.rect.x = x
        self.rect.y = y
        self.speedx = b_speed

    def update(self):
        # A bala move
        self.rect.x += self.speedx
        if self.rect.x < 0  or self.rect.x>800: # Se o tiro passar do inicio da tela, morre.
            self.kill()
class barreira(pygame.sprite.Sprite):
    def __init__(self, x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.rect=self.get_rect()
        self.rect.x=w
        self.rect.y=h
class Vida(pygame.sprite.Sprite):
    def __init__(self, anim):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frame= 0
        self.anim=anim
        self.img=self.anim[self.frame//20]
        self.rect = self.img.get_rect()
        self.rect.x = largura_janela-400
        self.rect.y = 0
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks=400
    def update(self, vida_seg):
        now=pygame.time.get_ticks()
        elapsed_ticks= now - self.last_update
        self.frame=vida_seg
        if elapsed_ticks>self.frame_ticks:
            self.last_update=now
            if self.frame<201:
                self.img=self.anim[self.frame//20]
            else:
                game = False
                return game
direcao=1
P1=Player(assets['Player_Normal_Anim'],assets['Player_Normal_E_Anim'],Parado, direcao)
Player_Grupo.add(P1)
for i in range (20):
    variavel=random.randint(0,len(posicoes_quadra)-1)
    Z = Zombie(assets['Zombie_Anim'],1 ,1,0,0,posicoes_quadra[variavel][0],posicoes_quadra[variavel][1])
    Zombie_Grupo.add(Z)

for i in range(6):
    for j in range(6):
        x = j * 1000 - 3600
        y = i * 800 - 2900
        quarteirao = Quadra(quarteirao_img, x, y,0,0)
        predio1=gerar_bloco_aleatorio(assets["casas"])
        predio = casa(predio1[0],x,y,predio1[1],predio1[2])
        mapa.add(quarteirao,predio)
        Construcoes_Grupo.add(predio)
retangulo_cima=barreira(0,0,4800,-10)
retangulo_baixo=barreira(0,3600,4800,10)
retangulo_esquerda=barreira(0,0,-10,3600)
retangulo_direita=barreira(4800,0,10,3600)
mapa.add(retangulo_baixo,retangulo_cima,retangulo_esquerda,retangulo_direita)
Construcoes_Grupo.add(retangulo_baixo,retangulo_cima,retangulo_esquerda,retangulo_direita)
##########################  LOOP PRINCIPAL ###############################

# Loop principal
clock = pygame.time.Clock()
FPS = 60
menu = True 
vida=Vida(assets['Vida_Anim'])
vida_seg=0
Zumbis_Mortos=0
game=False
def sair():
    pygame.quit()
def como_jogar():
    while como_jogar:
        window.blit(htp,(100,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return 0
def game_over():
    while game_over:
        window.fill((0,0,0))
        window.blit(gameover,(100,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 0
def menu_(window):
    while menu_:
        window.fill((0,0,0))
        retangulo_iniciar = pygame.Rect(300, 200, 200, 100)
        retangulo_comojogar = pygame.Rect(300, 300, 200, 100)
        retangulo_sair = pygame.Rect(300, 400, 200, 100)
        texto_iniciar = fonte.render("Iniciar jogo", True, ((255,255,255)))
        texto_comojogar = fonte.render("Como Jogar", True, ((255,255,255)))
        texto_sair = fonte.render("Sair", True, ((255,255,255)))
        window.blit(texto_iniciar, (retangulo_iniciar.x,retangulo_iniciar.y))
        window.blit(texto_comojogar, (retangulo_comojogar.x,retangulo_comojogar.y))
        window.blit(texto_sair, (retangulo_sair.x,retangulo_sair.y))
        pygame.display.update()
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sair()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_iniciar.collidepoint(event.pos):
                    return True # Inicia o jogo e oculta o menu
                elif retangulo_comojogar.collidepoint(event.pos):
                    como_jogar()
                elif retangulo_sair.collidepoint(event.pos):
                    return False
menu_ativo = menu_(window)
if menu_ativo ==True:
    game=True
while game:
    clock.tick(FPS)
    font = pygame.font.SysFont(None, 48)
    text = font.render('Zumbis Mortos: ', True, (0, 0, 0))
    text2=font.render('{}'.format(Zumbis_Mortos),True,(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_w:
                P1.move= Correndo
                for quadra in mapa:
                    quadra.speedy += 2
                for zumbi in Zombie_Grupo:
                    zumbi.speedymap +=2
            elif event.key == pygame.K_s :
                P1.move=Correndo
                for quadra in mapa:
                    quadra.speedy -= 2
                for zumbi in Zombie_Grupo:
                    zumbi.speedymap -=2
            elif event.key == pygame.K_a :                   
                P1.direcao=2
                P1.move=Correndo
                for quadra in mapa:
                    quadra.speedx += 2
                for zumbi in Zombie_Grupo:
                    zumbi.speedxmap +=2
            elif event.key == pygame.K_d :                
                P1.direcao=1
                P1.move=Correndo
                for quadra in mapa:
                    quadra.speedx -= 2
                for zumbi in Zombie_Grupo:
                    zumbi.speedxmap -=2
            elif event.key == pygame.K_l:
                P1.move=Facada
            elif event.key== pygame.K_k:
                P1.move=Shot
                if P1.direcao==1:
                    b_shoot=20
                if P1.direcao==2:
                    b_shoot=-20
                P1.shot(b_shoot)
        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_w :
                for quadra in mapa:
                    quadra.speedy =0
                for zumbi in Zombie_Grupo:
                    zumbi.speedymap =0
            elif event.key == pygame.K_s :
                for quadra in mapa:
                    quadra.speedy =0
                for zumbi in Zombie_Grupo:
                    zumbi.speedymap =0
            elif event.key == pygame.K_a :
                for quadra in mapa:
                    quadra.speedx =0
                for zumbi in Zombie_Grupo:
                    zumbi.speedxmap =0
            elif event.key == pygame.K_d :
                for quadra in mapa:
                    quadra.speedx =0
                for zumbi in Zombie_Grupo:
                    zumbi.speedxmap =0
    
    if quarteirao.speedx==0 and quarteirao.speedy==0:
        P1.move=Parado
    hits_Construcoes= pygame.sprite.groupcollide(Player_Grupo,Construcoes_Grupo,False,False,pygame.sprite.collide_mask) #verifica colisões com os prédios
    mapa.update() # Atualiza os sprites do mapa
    Player_Grupo.update()
    for zumbi in Zombie_Grupo:
        zumbi.move()
        zumbi.update()
        zumbi.Animacao()
    if len(bullet_Grupo)!=0:
        bullet_Grupo.update()
    # Atualiza os sprites do Player
    for zumbi in Zombie_Grupo:
        if hits_Construcoes=={}: 
            zumbi.update()
        zumbi.move()
        zumbi.Animacao()

    hits_Construcoes= pygame.sprite.groupcollide(Player_Grupo,Construcoes_Grupo,False,False,pygame.sprite.collide_mask) #verifica colisões com os prédios
    if hits_Construcoes!= {}:
        for quadra in mapa:
            quadra.speedx= 0
            quadra.speedy=0

    Hit_do_zumbi=pygame.sprite.groupcollide(Player_Grupo,Zombie_Grupo,False,False,pygame.sprite.collide_mask)
    if Hit_do_zumbi!={} and P1.move!=Facada:
        vida_seg+=1
        if vida_seg<201:
            vida.update(vida_seg)
        else:
            game=False

    hits_zumbi_construcao = pygame.sprite.groupcollide(Zombie_Grupo,Construcoes_Grupo,False,False,pygame.sprite.collide_mask)
    if hits_zumbi_construcao!={}:
        for zumbi in hits_zumbi_construcao:
            construcao =hits_zumbi_construcao[zumbi][0]
            if zumbi.rect.right>=construcao.rect.left and zumbi.speedx!=0 :
                zumbi.speedx*=-1
            if zumbi.rect.left>=construcao.rect.right and zumbi.speedx!=0 :
                zumbi.speedx*=-1
            if zumbi.rect.top>=construcao.rect.bottom and zumbi.speedy!=0 :
                zumbi.speedy*=-1
            if zumbi.rect.bottom>=construcao.rect.top and zumbi.speedy!=0 :
                zumbi.speedy*=-1
    else:
        for zumbi in hits_zumbi_construcao:
            construcao =hits_zumbi_construcao[zumbi][0]
            if zumbi.rect.right<construcao.rect.left and zumbi.speedx!=0 :
                zumbi.speedx=1
            if zumbi.rect.left<construcao.rect.right and zumbi.speedx!=0 :
                zumbi.speedx=1
            if zumbi.rect.top<construcao.rect.bottom and zumbi.speedy!=0 :
                zumbi.speedy=1
            if zumbi.rect.bottom<construcao.rect.top and zumbi.speedy!=0 :
                zumbi.speedy=1
    Hit_do_Player=pygame.sprite.groupcollide(Player_Grupo,Zombie_Grupo,False,False,pygame.sprite.collide_mask)
    if P1.move==Facada and Hit_do_Player!={}:
        for i in Hit_do_Player.values():
            for i2 in i:
                for x in range (len(i)):
                    variavel=random.randint(0,len(posicoes_quadra))
                    Z = Zombie(assets['Zombie_Anim'],1,1,0,0,posicoes_quadra[variavel][0],posicoes_quadra[variavel][1])
                    Zombie_Grupo.add(Z)
                i2.kill()
        Zumbis_Mortos+=1
    
    Hit_da_Bala=pygame.sprite.groupcollide(bullet_Grupo,Zombie_Grupo,True,False,pygame.sprite.collide_mask)
    if Hit_da_Bala!={}:
        for i in Hit_da_Bala.values():
            for i2 in i:
                for x in range (len(i)):
                    variavel=random.randint(0,len(posicoes_quadra))
                    Z = Zombie(assets['Zombie_Anim'],1,1,0,0,posicoes_quadra[variavel][0],posicoes_quadra[variavel][1])
                    Zombie_Grupo.add(Z)
                i2.kill()
        Zumbis_Mortos+=1
    mapa.update()
    Player_Grupo.update()
    for zumbi in Zombie_Grupo:
        if hits_Construcoes=={}:
             zumbi.update()
        zumbi.move()
        zumbi.Animacao()

    window.fill((0, 0, 0))  
    mapa.draw(window)
    window.blit(Player_Grupo.sprites()[0].img, Player_Grupo.sprites()[0].rect)
    if len(Zombie_Grupo)>0:
        for i in range(len(Zombie_Grupo)):
            window.blit(Zombie_Grupo.sprites()[i].img, Zombie_Grupo.sprites()[i].rect)
    if len(bullet_Grupo)!=0:
        window.blit(bullet_Grupo.sprites()[0].img, bullet_Grupo.sprites()[0].rect)
    window.blit(vida.img, vida.rect)
    window.blit(text, (10, 10))
    window.blit(text2, (275, 10))
    pygame.display.update() # Atualiza a janela
if menu_ativo ==True:
    game_over()
menu_ativo=False

pygame.quit() # Finalização
