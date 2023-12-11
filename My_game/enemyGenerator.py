import pygame
import sys
import random
from gameManagercopy import *
from enemy import *
# Define una clase para el generador de enemigos
class EnemyGenerator:
    def __init__(self,screen_w,screen_h):
        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.enigo_estatico =False
    def update(self,level,screen,terrenos,plataformas,balas_1,player,plataforma_movil,trap,delta_ms):
    # Actualiza el temporizador y genera enemigos si es necesario
        self.spawn_timer += 1
        if self.spawn_timer >= 60 and len(self.enemies) < 3:  # Genera un enemigo cada segundo (60 fotogramas)
            self.spawn_enemy(level)
            self.spawn_timer = 0
        for enemy in self.enemies:
            enemy.dibujar(screen)
            enemy.update(terrenos,plataformas,balas_1,player,plataforma_movil,screen,trap,delta_ms)
    def spawn_enemy(self,level):
        if level == "1":
            enemy = Enemigo(random.randint(0, 1200), 0,self.screen_w,self.screen_h)
            self.enemies.add(enemy)
        elif level == "2":
            enemy_2 = Enemigo_2(random.randint(0, 1200), 0,self.screen_w,self.screen_h)
            self.enemies.add(enemy_2)
        elif level == "3":
            enemy_2 = Enemigo_2(random.randint(0, 1200), 0,self.screen_w,self.screen_h)
            self.enemies.add(enemy_2)
            enemy = Enemigo(random.randint(0, 1200), 0,self.screen_w,self.screen_h)
            self.enemies.add(enemy)
            if not self.enigo_estatico:
                enemy_estatico = Enemigo_estatico(1000,350,-1,200)
                self.enemies.add(enemy_estatico)
                self.enigo_estatico=True
    def eliminar_elementos(self):
        self.enemies.empty()