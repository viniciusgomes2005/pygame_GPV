import pygame
class button:
    def __init__(self, color,x,y,largura,altura,texto,fontsize,fontname):
        self.color = color
        self.x=x
        self.y=y
        self.largura=largura
        self.altura=altura
        self.texto=texto
        self.fontsize=fontsize
        self.fontname=fontname
    def draw(self,window,outline=None):
        if outline:
            pygame.draw.rect(window,outline,(self.x-2,self.y-2,self.largura+4,self.altura+4),0)
        pygame.draw.rect(window,self.color,(self.x,self.y,self.largura,self.altura))
        if self.texto!="":
            font = pygame.font.SysFont('Inter',60)
            texto = font.render(self.texto,1,(0,0,1))
            window.blit(texto,(self.x+(self.largura/2 -texto.get_width()/2),self.y+(self.altura/2-texto.get_height()/2)))
    def over(self,pos):
        if pos[0]>self.x and pos[0]<self.x+self.largura:
            if pos[1]>self.y and pos[1]<self.y+self.altura:
                return True
        return False