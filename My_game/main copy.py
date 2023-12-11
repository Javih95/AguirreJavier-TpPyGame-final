import pygame
import sys
from gameManagercopy import *
from raycast import Ray
from auxiliar import *
from ranking import *
from GUI_textbox import *
import unicodedata
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Guardianes de la Selva")
    pygame.mixer.init()
    screen_w = 1200
    screen_h = 650
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    boton_play = Boton(600,430,"Play")
    boton_pausa = Boton(150,15,"Pause")
    boton_settings = Boton(450,15,"Settings")
    boton_menu = Boton(450,15,"menu")
    boton_seleccion_nivel=  Boton(600,530,"Niveles")
    Principal_img = pygame.image.load('.\My_game\Assets\Principal.png')
    Principal_img = pygame.transform.scale(Principal_img,(int(screen_w), int(screen_h)))
    sonido_fondo = pygame.mixer.Sound(".\My_game\Assets\Sound\Musica_inicio.wav")
    sonido_fondo.set_volume(0.5)
    game = Game_1(screen_w,screen_h)
    mostrar_niveles = False
    lvl2= True
    lvl3= True
    en_menu=False
    menu_niveles = Menu_seleccion_niveles(600,340,screen_w,screen_h)
    menu_settings = Settings(600,400)
    white = (255, 255, 255)
    black = (0, 0, 0)   
    red = (255, 0, 0)
    green = (0, 255, 0)
    text_box = TextBox(screen,200, 200, 400,295, 400, 60,white, green, black, red, 4,"Arial",40, black)
    while True:
        for evento in pygame.event.get():
            pygame.event.pump()  
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                caracter = evento.unicode
                if text_box.is_selected:
                    if evento.key == pygame.K_BACKSPACE:
                            text_box.text = text_box.text[:-1]
                    elif len(caracter) == 1 and unicodedata.category(caracter)[0] != 'C':
                            text_box.text += caracter
                if evento.key == pygame.K_p:
                    game.en_pausa = not game.en_pausa
                if evento.key == pygame.K_m:
                    game.game_over = True
                if evento.key == pygame.K_n:
                    print(game.player.nombre)
                if evento.key == pygame.K_l:
                    lvl2 = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not game.en_juego and not mostrar_niveles:
                    if boton_play.chequear_click(mouse_pos):
                        game.en_juego = not game.en_juego
                        #game.instantiate_level("1")
                        game.load_level("Level1")
                    if boton_seleccion_nivel.chequear_click(mouse_pos):
                        mostrar_niveles = True
                    if text_box.chequear_click(mouse_pos):
                        text_box.is_selected = not text_box.is_selected
                    #    print("text click")
                if mostrar_niveles and en_menu:
                    if menu_niveles.boton_nvl_1.chequear_click(mouse_pos):
                        print("level1")
                        game.en_juego = not game.en_juego
                        game.load_level("Level1")
                        mostrar_niveles = False
                        en_menu=False
                if mostrar_niveles and en_menu:
                    if  menu_niveles.boton_nvl_2.chequear_click(mouse_pos):
                       print("level2")
                       if lvl2:
                            game.en_juego = not game.en_juego
                            game.load_level("Level2")
                            mostrar_niveles = False
                            en_menu=False
                if mostrar_niveles and en_menu:
                    if  menu_niveles.boton_nvl_3.chequear_click(mouse_pos):
                       print("level3")
                       if lvl3:
                            game.en_juego = not game.en_juego
                            game.load_level("Level3")
                            mostrar_niveles = False
                            en_menu=False
                if game.en_juego :
                    if not game.en_pausa:
                        if boton_pausa.chequear_click(mouse_pos):
                            game.en_pausa = not game.en_pausa
                        if boton_settings.chequear_click(mouse_pos):
                            game.en_setting = not game.en_setting
                    if game.en_setting:
                        if menu_settings.boton_salir.chequear_click(mouse_pos):
                            game.en_setting = False
                        if menu_settings.boton_sonido.chequear_click(mouse_pos):
                            game.sonido = not game.sonido
                    if game.en_pausa:
                        if game.menu_pausa.boton_pausa.chequear_click(mouse_pos):
                            game.en_pausa = not game.en_pausa
                        if game.menu_pausa.boton_ranking.chequear_click(mouse_pos):
                            game.ranking_menu= not game.ranking_menu
                        if game.menu_pausa.boton_salir.chequear_click(mouse_pos):
                            game = Game_1(screen_w,screen_h) 
                    if game.game_over:
                        if boton_menu.chequear_click(mouse_pos):
                            game.en_juego = False
                            game.game_over= False
                            text_box.text=""
                        if not game.en_juego:
                            game = Game_1(screen_w,screen_h) 
        teclas = pygame.key.get_pressed()
        screen.fill((30, 30, 30))
        delta_ms= clock.tick(60)
        game.run(teclas,screen,delta_ms)
        if game.game_over:
            boton_menu.dibujar(screen)
        if game.en_setting:
            menu_settings.update(game.sonido)
            menu_settings.dibujar(screen)
        if game.en_juego and not game.game_over and not game.en_pausa:
            boton_pausa.dibujar(screen)
            boton_settings.dibujar(screen)
        if not game.en_juego and not mostrar_niveles:
            screen.blit(Principal_img, screen.get_rect())
            sonido_fondo.set_volume(0.1)
            sonido_fondo.play()
            boton_play.dibujar(screen)
            boton_seleccion_nivel.dibujar(screen)
            text_box.draw()
            game.player.nombre = text_box.text
        else:
            sonido_fondo.stop()
        text_box.update()
        if mostrar_niveles:
            menu_niveles.update(lvl2,lvl3)
            menu_niveles.dibujar(screen)
            en_menu=True
        pygame.display.update()
    pygame.quit()

