import pygame
class Terreno(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
