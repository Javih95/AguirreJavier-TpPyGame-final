import pygame
import sys
class Auxiliar:
    def __init__(self) -> None:
        pass
class Cronometro:
    def __init__(self, tiempo_inicial_segundos):
        self.tiempo_inicial = tiempo_inicial_segundos
        self.tiempo_restante = tiempo_inicial_segundos*60
        self.font = pygame.font.Font(None, 36)
        self.texto = None
    def update(self):
        self.tiempo_restante -= 1
        if self.tiempo_restante < 0:
            self.tiempo_restante = 0
            # Aquí puedes agregar lógica para manejar el fin del tiempo del nivel o del juego
            pygame.quit()
            sys.exit()
        self.texto = self.font.render(f"Tiempo: {self.tiempo_restante//60}", True, (255, 255, 255))
    def dibujar(self, pantalla):
        pantalla.blit(self.texto, (10, 10))
class Boton():
    def __init__(self,pos_x, pos_y,texto):
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0,0,200,50)
        self.rect.center = (pos_x, pos_y)
        self.texto_color = (128, 128, 128)
        self.font = pygame.font.Font(None, 36)
        self.texto_constructor(texto)
    def texto_constructor(self,texto):
        self.texto = self.font.render(texto, True, self.texto_color,self.color)
        self.texto_rect = self.texto.get_rect()
        self.texto_rect.center = self.rect.center
    def dibujar(self, pantalla):
        pantalla.fill(self.color, self.rect)
        pantalla.blit(self.texto,self.texto_rect)
    def chequear_click(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)