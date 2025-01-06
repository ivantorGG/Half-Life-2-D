import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__()

        for group in groups:
            self.add(group)

        self.image = pygame.Surface((30, 50))
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, 30, 50))
        self.rect = (pygame.Rect(300, 300, 30, 50))
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def move_player(self, plus_x, plus_y):
        self.rect = self.rect.move(plus_x, plus_y)
