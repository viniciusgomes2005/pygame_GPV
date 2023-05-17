import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

image = pygame.image.load("C:/Users/gabri/OneDrive - Insper - Institudo de Ensino e Pesquisa/Insper/2023/1-semestre/DSoft(desing de software)/Sprites/Background cortado.png")
image = pygame.transform.scale(image, (800, 600))

window.blit(image, (100, 100))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
