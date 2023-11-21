import pygame
import sys
from gameManager import Game
from raycast import Ray
from auxiliar import *
if __name__ == '__main__':
    pygame.init()
    screen_w = 600
    screen_h = 600
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    boton_play = Boton(300,300,"Jugar")
    boton_pausa = Boton(450,15,"Pause")
    game = Game()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    game.en_pausa = not game.en_pausa
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if boton_play.chequear_click(mouse_pos):
                    game.en_juego = not game.en_juego
                if game.en_juego :
                    if boton_pausa.chequear_click(mouse_pos):
                        game.en_pausa = not game.en_pausa
                    if game.menu_pausa.boton_pausa.chequear_click(mouse_pos):
                        game.en_pausa = not game.en_pausa
        #mouse_pos=pygame.mouse.get_pos()
        #click = pygame.MOUSEBUTTONDOWN
        teclas = pygame.key.get_pressed()
        screen.fill((30, 30, 30))
        if not game.en_juego:
            boton_play.dibujar(screen)
        boton_pausa.dibujar(screen)
        game.run(teclas,screen)
        pygame.display.flip()
        clock.tick(60)
