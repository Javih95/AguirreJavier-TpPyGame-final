import pygame
import sys
import math
from explosion import *
class Bala_enemigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direccion,speed):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.color =(0, 0, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.direccion = direccion
        self.speed = speed
    def update(self):
        self.rect.x += self.speed * self.direccion
        # Eliminar la bala si sale de la pantalla
        if self.rect.y < 0 or self.rect.x < 0 or self.rect.x > 600:
            self.kill()
class Bala(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direccion,speed,speed_y):
        super().__init__()
        ROJO = (255, 0, 0)
        self.image = pygame.Surface((10, 10))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.direccion = direccion
        self.speed = speed
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed * self.direccion
        self.rect.y -= self.speed_y
        # Eliminar la bala si sale de la pantalla
        if self.rect.y < 0 or self.rect.x < 0 or self.rect.x > 600:
            self.kill()
class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,angulo, velocidad_inicial,direccion):
        super().__init__()
        color = (255, 99, 71)
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.direccion_player = direccion
        # Convertir el ángulo a radianes
        angulo_radianes = math.radians(angulo)
        velocidad_x = (velocidad_inicial*direccion)* math.cos(angulo_radianes)
        velocidad_y = -velocidad_inicial * math.sin(angulo_radianes)
        # Velocidades iniciales
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        # Gravedad
        self.gravedad = 0.5 
        self.explocion_timer = 0
        self.destroy_timer = 0
        self.explotar = False
        self.contador_explosion = 0
    def update(self):
        self.explocion_timer += 1
        self.destroy_timer += 1
        self.velocidad_y += self.gravedad
        # Actualizar posición
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        if self.explocion_timer > 30 and not self.explotar:
            original_image = self.image.copy()
            new_width = int(original_image.get_width() * 3)
            new_height = int(original_image.get_height() * 3)
            self.image = pygame.transform.scale(original_image, (new_width, new_height))
            self.contador_explosion +=1
            if self.contador_explosion > 30:
                self.explotar=True
    # Escalar el rectángulo
            self.rect.width = new_width
            self.rect.height = new_height
            self.explocion_timer = 0
        if self.rect.y >= 500:
            self.rect.y = 500
            self.velocidad_x = 0

        # Eliminar el proyectil si sale de la pantalla
        if self.rect.y > 600 or self.destroy_timer > 100:
            self.kill()

