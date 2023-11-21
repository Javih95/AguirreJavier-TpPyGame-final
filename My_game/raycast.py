import pygame
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction  # Normaliza la dirección del rayo

    def advance(self, distance):
        # Avanza el rayo en la dirección especificada
        self.origin += self.direction * distance
    def raycast(ray, objects):
        for obj in objects:
            if obj.rect.collidepoint(ray.origin):
                return True
        return False
