import pygame


class Level(pygame.sprite.Sprite):
    def __init__(self, k_size, obj, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('Game/images/objects/level1-off.png')
        self.image = pygame.transform.scale(self.image, (round(37 * 2 * k_size[0]), round(29 * 2 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))

        self.state = 'off'
        self.obj = obj
        self.k_size = k_size
        self.sound = pygame.mixer.Sound('Game/sounds/level1-on.mp3')

    def switch(self):
        if self.state == 'off':
            self.sound.play()
            self.image = pygame.image.load('Game/images/objects/level1-on.png')
            self.image = pygame.transform.scale(self.image,
                                                (round(32 * 2 * self.k_size[0]), round(26 * 2 * self.k_size[1])))
            self.rect = self.image.get_rect(center=(self.rect.centerx + 18 * self.k_size[0], self.rect.centery))
            self.state = 'on'
            if self.obj is not None:
                self.obj.go = True
            return True
        return False


class InvisibleWall(pygame.sprite.Sprite):
    def __init__(self, k_size, x1, y1, x2, y2, *groups, is_visible=False, color=(255, 255, 255), do_move=True):
        """Указываем: x1, y1, x2, y2, в каких группах и видно ли её"""
        super().__init__(*groups)
        if do_move:
            if x1 == x2:  # вертикальная стенка
                self.image = pygame.Surface([1, round(k_size[1] * y2) - round(k_size[1] * y1)], pygame.SRCALPHA)
                self.rect = pygame.Rect(round(k_size[0] * x1), round(k_size[1] * y1), 1,
                                        round(k_size[1] * y2) - round(k_size[1] * y1))
            else:  # горизонтальная стенка
                self.image = pygame.Surface([round(k_size[0] * x2) - round(k_size[0] * x1), 1], pygame.SRCALPHA)
                self.rect = pygame.Rect(round(k_size[0] * x1), round(k_size[1] * y1),
                                        round(k_size[0] * x2) - round(k_size[0] * x1), 1)
        else:
            if x1 == x2:  # вертикальная стенка
                self.image = pygame.Surface([1, y2 - y1], pygame.SRCALPHA)
                self.rect = pygame.Rect(x1, y1, 1,
                                        y2 - y1)
            else:  # горизонтальная стенка
                self.image = pygame.Surface([x2 - x1, 1], pygame.SRCALPHA)
                self.rect = pygame.Rect(x1, y1,
                                        x2 - x1, 1)
        if is_visible:
            pygame.draw.circle(self.image, color, (200, 200), 999999)

