import pygame


class GlockBullet(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, direction, *groups):
        super().__init__(*groups)

        self.speed = 50 if direction == 'right' else 50
        self.image = pygame.Surface([1, 1])
        self.rect = pygame.Rect(0, 0, 1, 1)
        pygame.draw.circle(self.image, (0, 0, 0), (10, 10), 80)

    def update(self, *args, **kwargs):
        self.rect.x += self.speed

