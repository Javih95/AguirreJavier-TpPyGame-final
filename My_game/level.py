import pygame
import sys
from ground import Terreno
from plataforma import *
from vidas import *
from trap import Trap
class Level:
    def __init__(self) -> None:
        # Crear terrenos y plataformas de ejemplo
        self.terrenos = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.plataforma_movil = pygame.sprite.Group()
        terreno = Terreno(0, 550, 600, 50)
        plataforma = Plataforma(200, 380, 200, 20)
        plataforma_1= Plataforma(200, 500, 200, 20)
        plataforma_movil = Plataforma_movil(50,450,200,20,4)
        self.terrenos.add(terreno)
        self.plataformas.add(plataforma)
        self.plataformas.add(plataforma_1)
        self.plataforma_movil.add(plataforma_movil)
        #Trampas
        self.trap = pygame.sprite.Group()
        trampa = Trap(200,540,60,20)
        self.trap.add(trampa)
        self.colision_jugador_enemigo_procesada = False
        self.collision_clock =0
        self.vidas = pygame.sprite.Group()
        vida = Vida(50,500,15,15)
        self.vidas.add(vida)
        #Frutas
        self.frutas =pygame.sprite.Group()
        fruta = Frutas (150,500,20,20)
        self.frutas.add(fruta)
    def update(self,screen):
        self.terrenos.draw(screen)
        self.plataformas.draw(screen)
        self.plataforma_movil.draw(screen)
        self.trap.draw(screen)
        #self.frutas.draw(screen)
        #self.vidas.draw(screen)