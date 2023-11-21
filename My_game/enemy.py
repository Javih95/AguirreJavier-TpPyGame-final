import pygame
import random
from bala import Bala_enemigo
from raycast import Ray

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        ROJO = (255, 0, 0)
        self.image = pygame.Surface((50, 50))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.en_suelo = False
        self.velocidad = 3
        self.direccion_move = random.choice([-1, 1])
        self.direccion = "derecha"
        self.shoot_timer = 0
    def update(self,terrenos,plataformas,balas_1,jugador,plataforma_movil):
        self.shoot_timer += 1
        if self.en_suelo:
            self.move()
        self.limitar()
        self. gravedad(terrenos,plataformas,plataforma_movil)
        self.mirar(jugador,balas_1)
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
            if self.rect.bottom <= colision_plataforma[0].rect.top+5:  # Ajusta el valor según tu necesidad
                self.en_suelo = True
        elif colision_plataforma_movil:
            if self.rect.bottom <= colision_plataforma_movil[0].rect.top+5:  # Ajustar valor de tolerancia
                self.en_suelo = True
                plataforma_movil = colision_plataforma_movil[0]
                self.rect.x += plataforma_movil.movimiento
        if not self.en_suelo:
            self.rect.y += 1
    def move(self):
        self.rect.x += self.velocidad * self.direccion_move
        if self.direccion_move == -1:
            self.direccion = "izquierda"
        elif self.direccion_move == 1:
            self.direccion = "derecha"
    def limitar(self):
        if self.rect.y >= 550:
            self.rect.y = 550
            self.en_suelo = True
        if self.rect.x < 0:
            self.direccion_move *= -1  # Cambia la dirección
        elif self.rect.x > 550:
            self.direccion_move *= -1  # Cambia la dirección
    def shoot(self, balas_1):
        if self.shoot_timer >= 20:
            bala = Bala_enemigo(self.rect.x + self.rect.width//2, self.rect.y, self.direccion_move,8)
            balas_1.add(bala)
            self.shoot_timer = 0
    def mirar(self,jugador,balas_1):
        ray = Ray(self.rect.center, pygame.Vector2(self.direccion_move, 0))  # Rayo apuntando hacia la derecha
        ray.advance(100)
        if ray.raycast([jugador]):
            self.shoot(balas_1)