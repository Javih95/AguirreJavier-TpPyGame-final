import pygame as pg
import sys
from bala import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        BLANCO = (255, 255, 255)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.velocidad = 5
        self.velocidad_salto = 75
        self.en_suelo = False
        self.direccion_move = 1
        self.angulo_bomba = 45
        self.vidas = 5
        self.puntos = 0
        self.shoot_timer = 0
        self.speed_bala_y = 0
        self.nombre = ""
    def update(self,balas,bombas,teclas,terrenos, plataformas,plataforma_movil):
        self.shoot(balas,teclas)
        self.shoot_timer += 1
        self.limitar()
        self.jump(teclas)
        self.move(teclas)
        self.shoot_1(teclas,bombas)
        self.muerte()
        self. gravedad(terrenos,plataformas,plataforma_movil)
    def gravedad(self,terrenos,plataformas,plataforma_movil):
        colision_terreno = pygame.sprite.spritecollide(self, terrenos, False)
        colision_plataforma = pygame.sprite.spritecollide(self, plataformas, False)
        colision_plataforma_movil = pygame.sprite.spritecollide(self, plataforma_movil, False)
        if not colision_terreno and not colision_plataforma and not colision_plataforma_movil :
            self.rect.y += 1  # Aplicar gravedad
            self.en_suelo = False
        elif colision_terreno:
            self.en_suelo = True
        elif colision_plataforma:
            if self.rect.bottom <= colision_plataforma[0].rect.top+5:  # Ajustar valor de tolerancia
                self.en_suelo = True
        elif colision_plataforma_movil:
            if self.rect.bottom <= colision_plataforma_movil[0].rect.top+5:  # Ajustar valor de tolerancia
                self.en_suelo = True
                plataforma_movil = colision_plataforma_movil[0]
                self.rect.x += plataforma_movil.movimiento
        if not self.en_suelo:
            self.rect.y += 1 # Aplicar gravedad
    def move(self,teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
            self.direccion_move = -1
            self.speed_bala_y = 0
            self.angulo_bomba = 45
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
            self.direccion_move = 1
            self.speed_bala_y = 0
            self.angulo_bomba = 45
        if teclas[pygame.K_UP]:
            self.direccion_move = 0
            self.angulo_bomba = 90
            self.speed_bala_y = 10
        if teclas[pygame.K_DOWN]:
            self.direccion_move = 0
            self.angulo_bomba = 90
            self.speed_bala_y = -10
        if teclas[pygame.K_UP] and teclas[pygame.K_LEFT]:
            self.direccion_move = -1
            self.speed_bala_y = 10
        if teclas[pygame.K_UP] and teclas[pygame.K_RIGHT]:
            self.direccion_move = 1
            self.speed_bala_y = 10
        if teclas[pygame.K_DOWN] and teclas[pygame.K_LEFT]:
            self.direccion_move = -1
            self.speed_bala_y = -10
        if teclas[pygame.K_DOWN] and teclas[pygame.K_RIGHT]:
            self.direccion_move = 1
            self.speed_bala_y = -10
    def jump(self,teclas):
        if teclas[pygame.K_SPACE]:
            if self.en_suelo:
                self.rect.y -= self.velocidad_salto
                self.en_suelo = False
    def shoot(self, balas,teclas):
        # Crear una nueva bala en la posición del jugador y con la dirección actual
        if teclas[pygame.K_s]:
            if self.shoot_timer >= 20:
                bala = Bala(self.rect.x + self.rect.width // 2, self.rect.y, self.direccion_move,10,self.speed_bala_y)
                balas.add(bala)
                self.shoot_timer = 0
    def shoot_1(self,teclas,bombas):
        # Crear una nueva bala en la posición del jugador y con la dirección actual
        if teclas[pygame.K_a]:
            if self.shoot_timer >= 20:
                bomba = Bomb(self.rect.x + self.rect.width // 2, self.rect.y,self.angulo_bomba,10,self.direccion_move)
                bombas.add(bomba)
                self.shoot_timer = 0
    def limitar(self):
        if self.rect.y >= 550:
            self.rect.y = 550
            self.en_suelo = True
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 550:
            self.rect.x = 550
    def muerte(self):
        if self.vidas <= 0:
            print("has muerto")
            
    