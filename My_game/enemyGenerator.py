import pygame
import sys
import random
from enemy import Enemigo
# Define una clase para el generador de enemigos
class EnemyGenerator:
    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
    def update(self):
    # Actualiza el temporizador y genera enemigos si es necesario
        self.spawn_timer += 1
        if self.spawn_timer >= 60 and len(self.enemies) < 3:  # Genera un enemigo cada segundo (60 fotogramas)
            self.spawn_enemy()
            self.spawn_timer = 0
    def spawn_enemy(self):
        enemy = Enemigo(random.randint(0, 550), 0)
        self.enemies.add(enemy)