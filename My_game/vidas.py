import pygame
class Vida(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((138, 43, 226))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
class Frutas(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)