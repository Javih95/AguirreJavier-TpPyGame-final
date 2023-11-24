from auxiliar import *
class Menu_pausa:
    def __init__(self,pos_x,pos_y):
        self.boton_ranking = Boton(450,150,"Ranking")
        self.boton_pausa = Boton(150,150,"Pause")
        self.color = (0, 0, 200)
        self.rect = pygame.Rect(0,0,500,500)
        self.rect.center = (pos_x, pos_y)
    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)
        self.boton_pausa.dibujar(pantalla)
        self.boton_ranking.dibujar(pantalla)
class Ranking:
    def __init__(self,pos_x,pos_y):
        #self.jugadores = jugadores
        self.color = (0, 200, 0)
        self.rect = pygame.Rect(0,0,200,200)
        self.rect.center = (pos_x, pos_y)
    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)
class Settings:
    def __init__(self,pos_x,pos_y):
        self.color = (200, 50, 0)
        self.rect = pygame.Rect(0,0,400,400)
        self.rect.center = (pos_x, pos_y)
    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)