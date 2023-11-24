from typing import Any
import pygame
import sys
import random
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
class Plataforma_movil(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height,speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.velocidad = speed
        self.direccion_move = random.choice([-1, 1])
        self.movimiento= self.velocidad * self.direccion_move
    def update(self):
        self.movimiento= self.velocidad * self.direccion_move
        self.rect.x += self.movimiento
        if self.rect.x < 0:
            self.direccion_move *= -1  # Cambia la dirección
        elif self.rect.x > 550:
            self.direccion_move *= -1  # Cambia la dirección