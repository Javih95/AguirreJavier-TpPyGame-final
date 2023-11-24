import pygame
import sys
from gameManager import Game
from raycast import Ray
from auxiliar import *
from ranking import *
if __name__ == '__main__':
    pygame.init()
    screen_w = 600
    screen_h = 600
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    boton_play = Boton(300,300,"Play")
    boton_pausa = Boton(150,15,"Pause")
    boton_settings = Boton(450,15,"Settings")
    boton_menu = Boton(450,15,"menu")
    Principal_img = pygame.image.load('.\Assets\Principal.png')
    game = Game()
    input_text = Input_text(150,150)
    while True:
        for evento in pygame.event.get():
            pygame.event.pump()  
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    game.en_pausa = not game.en_pausa
                if evento.key == pygame.K_m:
                    game.game_over = True
                if evento.key == pygame.K_n:
                    print(game.player.nombre)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not game.en_juego:
                    if boton_play.chequear_click(mouse_pos):
                        game.en_juego = not game.en_juego
                if game.en_juego :
                    if not game.en_pausa:
                        if boton_pausa.chequear_click(mouse_pos):
                            game.en_pausa = not game.en_pausa
                    if game.en_pausa:
                        if game.menu_pausa.boton_pausa.chequear_click(mouse_pos):
                            game.en_pausa = not game.en_pausa
                        if game.menu_pausa.boton_ranking.chequear_click(mouse_pos):
                            game.ranking_menu= not game.ranking_menu
                            print("ranking")
                    if game.game_over:
                        if boton_menu.chequear_click(mouse_pos):
                            game.en_juego = False
                            game.game_over= False
                        if not game.en_juego:
                            game = Game() 
        teclas = pygame.key.get_pressed()
        screen.fill((30, 30, 30))
        if game.game_over:
            boton_menu.dibujar(screen)
        if game.en_juego and not game.game_over and not game.en_pausa:
            boton_pausa.dibujar(screen)
            boton_settings.dibujar(screen)
        if not game.en_juego:
            screen.blit(Principal_img, Principal_img.get_rect())
            boton_play.dibujar(screen)
            input_text.dibujar(screen)
            input_text.update(evento)
            game.player.nombre = input_text.texto
        game.run(teclas,screen)
        pygame.display.flip()
        clock.tick(60)
