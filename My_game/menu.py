from auxiliar import *
from funciones import *
class Menu_pausa:
    def __init__(self,pos_x,pos_y):
        self.boton_ranking = Boton(400,150,"Ranking")
        self.boton_pausa = Boton(100,150,"Pause")
        self.boton_salir = Boton(700,150,"Salir")
        self.color = (0, 0, 200)
        self.rect = pygame.Rect(0,0,500,500)
        self.rect.center = (pos_x, pos_y)
    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)
        self.boton_pausa.dibujar(pantalla)
        self.boton_ranking.dibujar(pantalla)
        self.boton_salir.dibujar(pantalla)
class Ranking:
    def __init__(self,pos_x,pos_y,lista_jugadores):
        #self.jugadores = jugadores
        self.color = (0, 200, 0)
        self.rect = pygame.Rect(0,0,200,200)
        self.pos_x= pos_x
        self.pos_y = pos_y
        self.rect.topleft = (pos_x, pos_y)
        self.lista_jugadores = lista_jugadores
        self.font_tabla = pygame.font.Font(None, 36)
    def dibujar(self, pantalla):
        self.lista_jugadores.sort(key=lambda x: x[1],reverse=True)
        pantalla.fill(self.color, self.rect)
        lista_jugadores_txt = []
        y = self.pos_y
        x= self.pos_x

        for item in self.lista_jugadores:
            # Si estamos en la primera vuelta, utilizamos la tipografía color blanco
            if len(lista_jugadores_txt) == 0:
                color_txt = (255, 255, 255)
            else:
                color_txt = (109, 30, 3)
            nombre_txt = self.font_tabla.render(formatear_nombre_jugador(str(item[0])),True, color_txt)
            puntos_txt = self.font_tabla.render(formatear_puntaje(str(item[1])),True, color_txt)
            lista_jugadores_txt.append((nombre_txt, (x, y)))
            lista_jugadores_txt.append((puntos_txt, (x+100, y)))
            y += 50
        for texto, posicion in lista_jugadores_txt[:11]:
            pantalla.blit(texto, posicion)
class Settings:
    def __init__(self,pos_x,pos_y):
        self.color = (100, 150, 200)
        self.rect = pygame.Rect(0,0,400,400)
        self.rect.center = (pos_x, pos_y)
        self.boton_sonido = Boton(600,400,"Audio On")
        self.boton_salir = Boton(600,300,"Salir")
    def update(self,sonido):
        if sonido:
            self.boton_sonido = Boton(600,400,"Audio Off")
        else:
            self.boton_sonido = Boton(600,400,"Audio On")

    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)
        self.boton_salir.dibujar(pantalla)
        self.boton_sonido.dibujar(pantalla)
class  Menu_seleccion_niveles:
    def __init__(self,pos_x,pos_y, width, height):
        original_image = pygame.image.load(".\My_game\Assets\menu_seleccion_nivel.png")
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.boton_nvl_1 = Boton_nivel(200,500,"1")     
        self.boton_nvl_2 = Boton_nivel(600,500,"2")
        self.boton_nvl_3 = Boton_nivel(1000,500,"3")
    def update(self,lvl2,lvl3):
        if lvl2== False:
            self.boton_nvl_2 = Boton_nivel(600,500,"x")
        else:
            self.boton_nvl_2 = Boton_nivel(600,500,"2")
        if lvl3== False:
            self.boton_nvl_3 = Boton_nivel(1000,500,"x")
        else:
            self.boton_nvl_3 = Boton_nivel(1000,500,"3")

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
        self.boton_nvl_1.dibujar(pantalla)
        self.boton_nvl_2.dibujar(pantalla)
        self.boton_nvl_3.dibujar(pantalla)