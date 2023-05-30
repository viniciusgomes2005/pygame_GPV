import pygame
import random
from assets import *

# Inicialização do Pygame
pygame.init()

######################  JANELA  #############################

altura_janela = 800 # altura da janela
largura_janela = 1000 # largura da janela
window = pygame.display.set_mode((largura_janela, altura_janela)) # define tamanho da janela
pygame.display.set_caption('Pygame') # Da o nome do jogo

#####################  SPRITES  ################################
assets=load_assets()
fonte=pygame.font.SysFont("Comic Sans MS",60)
################################  GRUPOS  ####################################

Player_Grupo= pygame.sprite.Group() #Grupo do Player
Construcoes_Grupo= pygame.sprite.Group() # Grupo das Construções 
Zombie_Grupo = pygame.sprite.Group() # Grupo dos Zumbis
mapa = pygame.sprite.Group() #Grupo que forma o mapa
bullet_Grupo = pygame.sprite.Group() # Grupo para as balas
Quadras=pygame.sprite.Group()

posicoes_possiveis=[] #posições possiveis para spawn de zumbis
mapa_largura = 800 * 6  # Largura total do mapa
mapa_altura = 600 * 6  # Altura total do mapa

quadra_possivel = [] # lista de quadras
for i in range(36):
    quadra_possivel.append('assets/Sprites/Background cortado.png')

def gerar_bloco_aleatorio(quadra_possivel): #seleciona uma quadra aleatória
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

    def update(self): # atualiza o movimento das quadras
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    
class casa(pygame.sprite.Sprite): # Classe para representar uma Construção
    def __init__(self, img, quadra_x,quadra_y,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img # define imagem
        self.mask= pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect() #torna imagem em um retangulo
        self.rect.x = quadra_x+x # X da posição em que a construção vai estar 
        self.rect.y = quadra_y+y # Y da posição em que a construção vai estar
        self.speedx = 0 # VELOCIDADE DA CONSTRUÇÃO NO EIXO X
        self.speedy = 0 # VELOCIDADE DA CONSTRUÇÃO NO EIXO Y
    def update(self): # atualiza o movimento das Construções
        self.rect.x += self.speedx
        self.rect.y +=self.speedy

class Player(pygame.sprite.Sprite): # Classe do PLayer
    def __init__(self,anim,anim2,move, direcao):
        pygame.sprite.Sprite.__init__(self)
        self.frame=0 # Armazena o índice atual na animação
        self.anim=anim # Animação do Player olhando para a direita
        self.anim2=anim2 # Animação do Player olhando para a esquerda
        self.img=self.anim[self.frame] #define a imagem do Player como uma das imagens da animação
        self.mask= pygame.mask.from_surface(self.img)
        self.rect=self.img.get_rect() #torna imagem em um retangulo
        self.rect.center = (largura_janela/2, altura_janela/ 2) #define a posição do Player
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks=50 #minimo de ticks para mudar o frame
        self.move=move #Qual ação o Player está fazendo
        self.direcao=direcao #direção em que o jogador está olhando
    def update(self):
        now=pygame.time.get_ticks() # Verifica o tick atual.
        elapsed_ticks= now - self.last_update # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        if self.move==Parado: #Se o Player está Parado...
            if elapsed_ticks>self.frame_ticks:# Se já está na hora de mudar de imagem...
                self.last_update=now # Marca o tick da nova imagem.
                self.frame+=1 # Avança um quadro
                if self.frame >= 10:
                    self.frame=0
                self.img=self.anim[self.frame] #define a nova imagem
        elif self.move==Correndo: #Se o Player está Correndo...
            if elapsed_ticks>self.frame_ticks:# Se já está na hora de mudar de imagem...
                if self.direcao==1: #Se está olhando para a direita...
                    if self.frame<10 or self.frame >= 17:
                        self.frame=10
                    else:
                        self.frame+=1 # Avança um quadro
                    self.last_update=now # Marca o tick da nova imagem.
                    self.img=self.anim[self.frame] #define a nova imagem
                elif self.direcao == 2: #Se está olhando para a esquerda...
                    if self.frame>=7:
                        self.frame=0
                    else:
                        self.frame+=1 # Avança um quadro
                    self.last_update=now # Marca o tick da nova imagem.
                    self.img=self.anim2[self.frame] #define a nova imagem
        elif self.move==Facada: #Se o Player está dando Facada...
            if elapsed_ticks>self.frame_ticks: # Se já está na hora de mudar de imagem...
                if self.direcao==1: #Se está olhando para a direita...
                    if self.frame<18 or self.frame>=25:
                        self.frame=18
                    else:
                        self.frame+=1 # Avança um quadro
                    self.last_update=now # Marca o tick da nova imagem
                    self.img=self.anim[self.frame] #define a nova imagem
                    if self.frame==24: #Se a animação chegou ao fim, volta para a animação de correr
                        self.move=Correndo
                        self.direcao=1
                        self.frame=10
                elif self.direcao==2: #Se está olhando para a esquerda...
                    if self.frame<8 or self.frame>14:
                        self.frame=8
                    else:
                        self.frame+=1 # Avança um quadro
                    self.last_update=now # Marca o tick da nova imagem.
                    self.img=self.anim2[self.frame] #define a nova imagem
                    if self.frame==14: #Se a animação chegou ao fim, volta para a animação de correr
                        self.move=Correndo
                        self.direcao=2
                        self.frame=0
        elif self.move==Shot:
            if elapsed_ticks>self.frame_ticks: # Se já está na hora de mudar de imagem...
                if self.direcao==1: #Se está olhando para a direita...
                    if self.frame<25 or self.frame>=28:
                        self.frame=25
                    else:
                        self.frame+=1 # Avança um quadro
                    self.last_update=now # Marca o tick da nova imagem.
                    self.img=self.anim[self.frame] #define a nova imagem
                    if self.frame>=27: #Se a animação chegou ao fim, volta para a animação de correr
                        self.move=Correndo
                        self.direcao=1
                        self.frame=10
                elif self.direcao==2: #Se está olhando para a esquerda...
                    if self.frame<15 or self.frame>19:
                        self.frame=15
                    else:
                        self.frame+=1 # Avança um quadro
                    self.last_update=now # Marca o tick da nova imagem.
                    self.img=self.anim2[self.frame] #define a nova imagem
                    if self.frame==17: #Se a animação chegou ao fim, volta para a animação de correr
                        self.move=Correndo
                        self.direcao=2
                        self.frame=0
    def shot(self,b_shoot): #função em que o Player da tiro
        new_bullet = Bullet(assets['bullet_img'],  altura_janela/2-40, largura_janela/2-20, b_shoot) #cria bala
        bullet_Grupo.add(new_bullet) #adiciona bala criada ao Grupo de balas

class Zombie(pygame.sprite.Sprite): # Classe de zumbis
    def __init__(self, anim, speedx, speedy,speedxmap,speedymap,x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frame=0 # Armazena o índice atual na animação
        self.anim=anim # Animação do Player
        self.img=self.anim[self.frame] #define a imagem do Zumbi como uma das imagens da animação
        self.mask= pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect() #torna imagem em um retangulo
        self.rect.x =  x # X do canto superior esquerdo do retangulo
        self.rect.y = y # Y do canto superior esquerdo do retangulo
        self.speedy = speedy # VELOCIDADE DO Zumbi NO EIXO Y
        self.speedx = speedx # VELOCIDADE DO Zumbi NO EIXO X
        self.speedxmap = speedxmap # velocidade do mapa no Eixo X
        self.speedymap = speedymap # velocidade do mapa no Eixo Y
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks=50#minimo de ticks para mudar o frame
        self.direcao_z=1 # Direção em que 1 é olhando para a direita e 2 é para a esquerda
    def move(self): # função para decidir em qual direção o Zumbi vai se mover
        if self.speedx>-1: #Verifica se a velocidade em x é positiva
            if self.rect.x > P1.rect.x:
                self.rect.x -= self.speedx
                self.direcao_z=2
            elif self.rect.x < P1.rect.x:
                self.rect.x += self.speedx
                self.direcao_z=1
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
    def update(self): #Atualiza a posição do Zumbi
        self.rect.x += self.speedxmap
        self.rect.y += self.speedymap
    def Animacao(self): #Muda a imagem para criar a animação 
        now=pygame.time.get_ticks() # Verifica o tick atual.
        elapsed_ticks= now - self.last_update # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        if elapsed_ticks>self.frame_ticks:
            if self.direcao_z==1:
                self.last_update=now # Marca o tick da nova imagem.
                if self.frame >= 10:
                    self.frame=0
                else:
                    self.frame+=1
                self.img=self.anim[self.frame] #define a nova imagem
            elif self.direcao_z==2:
                self.last_update=now # Marca o tick da nova imagem.
                if self.frame<31 or self.frame>=39:
                    self.frame=31
                else:
                    self.frame+=1
                self.img=self.anim[self.frame] #define a nova imagem

class Bullet(pygame.sprite.Sprite): #Classe das balas
    def __init__(self, bullet_img, y, x, b_speed): # Construtor da classe.
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.img = bullet_img # define a imagem da bala
        self.rect = self.img.get_rect()#torna imagem em um retangulo
        self.mask= pygame.mask.from_surface(self.img)
        self.rect.x = x #Posição no Eixo X
        self.rect.y = y #Posição no Eixo Y
        self.speedx = b_speed #Velocidade da Bala

    def update(self): #Atualiza a posição da Bala
        self.rect.x += self.speedx
        if self.rect.x < 0  or self.rect.x>largura_janela: # Se o tiro passar do inicio da tela, morre.
            self.kill()

class Vida(pygame.sprite.Sprite): #Classe da Barra de Vida
    def __init__(self, anim):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.frame= 0 # Armazena o índice atual na animação
        self.anim=anim #Animação da Barra de Vida
        self.img=self.anim[self.frame//20]  #define a imagem da Barra de Vida como uma das imagens da animação
        self.rect = self.img.get_rect()  #torna imagem em um retangulo
        self.rect.x = largura_janela-400 #Posição da Barra de Vida no Eixo X
        self.rect.y = 0 #Posição da Barra de Vida no Eixo Y
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks=400 #minimo de ticks para mudar o frame
    def update(self, vida_seg): # Atualiza a Barra de Vida
        now=pygame.time.get_ticks() # Verifica o tick atual.
        elapsed_ticks= now - self.last_update # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        self.frame=vida_seg # vida é o indice da animação da Barra de Vida
        if elapsed_ticks>self.frame_ticks:
            self.last_update=now # Marca o tick da nova imagem.
            if self.frame<201: # Se os frames ainda estão na vida
                self.img=self.anim[self.frame//20] # define a imagem para a vida correspondente
            else: # Se os frames ultrapassaram a vida máxima
                game = False # Jogo acaba
                return game 
P1=Player(assets['Player_Normal_Anim'],assets['Player_Normal_E_Anim'],Parado, direcao) # Cria o Personagem
Player_Grupo.add(P1) #Adiciona o personagem no Grupo do Player
for i in range(6): #Cria o Mapa juntando as quadras
    for j in range(6):
        x = j * 1000 - 3600
        y = i * 800 - 2900
        posicao=[x,y]
        posicoes_possiveis.append(posicao)
        posicoes_quadra=posicoes_possiveis
        quarteirao = Quadra(assets['quarteirao_img'], x, y,0,0)
        predio1=gerar_bloco_aleatorio(assets["casas"])
        predio = casa(predio1[0],x,y,predio1[1],predio1[2])
        mapa.add(quarteirao,predio)
        Construcoes_Grupo.add(predio)
for i in range (20): # cria 20 Zumbis
    variavel=random.randint(0,len(posicoes_quadra)-1) #Define aleatóriamente onde o Zumbi irá surgir
    Z = Zombie(assets['Zombie_Anim'],1 ,1,0,0,posicoes_quadra[variavel][0],posicoes_quadra[variavel][1]) # Cria Zumbi
    Zombie_Grupo.add(Z) #Adiciona Zumbi no Grupo de Zmubis
retangulo_cima=casa(assets['black'],-2400,-1800,0,0)
retangulo_baixo=casa(assets['black'],-2400,1800,0,0)
retangulo_esquerda=casa(assets['preto'],-2400,-1800,0,0)
retangulo_direita=casa(assets['preto'],2400,-1800,0,0)
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
        window.blit(assets['htp'],(100,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return 0
def game_over():
    while game_over:
        window.fill((0,0,0))
        window.blit(assets['gameover'],(100,100))
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
        if P1.move!=Shot:
            P1.move=Parado
    hits_Construcoes= pygame.sprite.groupcollide(Player_Grupo,Construcoes_Grupo,False,False,pygame.sprite.collide_mask) #verifica colisões com os prédios
    mapa.update() # Atualiza os sprites do mapa
    Quadras.update()
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
                posq=random.choice(Quadras.sprites())
                Z = Zombie(assets['Zombie_Anim'],1,1,0,0,posq.rect.x,posq.rect.y)
                Zombie_Grupo.add(Z)
                i2.kill()
        Zumbis_Mortos+=1
    
    Hit_da_Bala=pygame.sprite.groupcollide(bullet_Grupo,Zombie_Grupo,True,False,pygame.sprite.collide_mask)
    if Hit_da_Bala!={}:
        for i in Hit_da_Bala.values():
            for i2 in i:
                if len(Quadras.sprites())==0:
                    print('grupo vazio')
                posq=random.choice(Quadras.sprites())
                Z = Zombie(assets['Zombie_Anim'],1,1,0,0,posq.rect.x,posq.rect.y)
                Zombie_Grupo.add(Z)
                i2.kill()
        Zumbis_Mortos+=1
    mapa.update()
    Quadras.update()
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
