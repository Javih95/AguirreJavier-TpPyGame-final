import pygame
import sys
from auxiliar import *
from level import *
from gameManagercopy import*
pygame.init()
screen_w = 600
screen_h = 600
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
boton_play = Boton(300,300,"Jugar")
boton_pausa = Boton(150,150,"Pause")
level = Level()
game = Game()
en_juego= False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                en_juego = not en_juego
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if boton_play.chequear_click(mouse_pos):
                print("play")
            if boton_pausa.chequear_click(mouse_pos):
                print("pausa")
    teclas = pygame.key.get_pressed()
    screen.fill((30, 30, 30))
    boton_pausa.dibujar(screen)
    level.update(screen)
    if not en_juego:
        boton_play.dibujar(screen)
    game.run(teclas,screen)
    pygame.display.flip()
    clock.tick(60)