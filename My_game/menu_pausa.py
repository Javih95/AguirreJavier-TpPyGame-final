from auxiliar import *
class Menu_pausa:
    def __init__(self,pos_x,pos_y):
        self.boton_play = Boton(500,150,"Jugar")
        self.boton_pausa = Boton(150,150,"Pause")
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0,0,500,500)
        self.rect.center = (pos_x, pos_y)
    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)
        self.boton_pausa.dibujar(pantalla)
        self.boton_play.dibujar(pantalla)
        