import pygame


class GlockBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, enemies, *groups):
        super().__init__(*groups)

        self.speed = 50 if direction == 'right' else -50
        self.image = pygame.Surface([1, 1])
        self.rect = pygame.Rect(0, 0, 1, 1)
        self.rect.x = x
        self.rect.y = y
        self.enemies = enemies
        pygame.draw.circle(self.image, (0, 0, 0), (10, 10), 80)

    def update(self, *args, **kwargs):
        self.rect.x += self.speed
        if not isinstance(pygame.sprite.spritecollideany(self, *self.groups()), GlockBullet) and \
                pygame.sprite.spritecollideany(self, *self.groups()):
            target, target_x = None, None
            for enemy in self.enemies:
                if target_x is None or abs(enemy.rect.centerx - self.rect.centerx) < target_x:
                    target_x = abs(enemy.rect.centerx - self.rect.centerx)
                    target = enemy
            target.health -= 5
            self.kill()
