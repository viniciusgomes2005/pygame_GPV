from os import path
import pygame
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Dados gerais do jogo
Altura_janela = 800
Largura_janela = 600
FPS=40
#Tamanhos
Player_largura=45
Player_altura=55
Zumbi_largura=45
Zumbie_altura=55

INIT=0
GAME=1
QUIT=2