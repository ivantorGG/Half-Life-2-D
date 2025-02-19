import pygame
from Game.connecting_objects import InvisibleWall
from Game.player import Player


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, name, wall_groups, obj, *groups):
        """Создаёт прямоугольное препятствие. Указывать:
        k_size, x, y, путь к изображению, [горизонтальную группу стен, вертикальную группу стен, группу уровней]"""
        super().__init__(*groups)

        self.obj = obj
        self.image = pygame.image.load(name)
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() / 3 * k_size[0]), round(self.image.get_height() / 3 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.falling_speed = 10
        self.stopped = False
        self.walls_resized = False
        self.wall_groups = wall_groups
        self.k_size = k_size
        horizontal_wall1 = InvisibleWall(k_size, self.rect.x - 1, self.rect.y - 1, self.rect.x + self.rect.width + 1,
                                         self.rect.y - 1, wall_groups[0], wall_groups[2], color=(255, 255, 255, 0), do_move=False)
        horizontal_wall2 = InvisibleWall(k_size, self.rect.x - 1, self.rect.y + self.rect.height + 1,
                                         self.rect.x + self.rect.width + 1, self.rect.y + self.rect.height + 1,
                                         wall_groups[0], wall_groups[2], color=(255, 255, 255, 0), do_move=False)
        vertical_wall1 = InvisibleWall(k_size, self.rect.x - 1, self.rect.y + 20 * k_size[1], self.rect.x - 1,
                                       self.rect.y + self.rect.height + 1, wall_groups[1], wall_groups[2], color=(255, 255, 255, 0), do_move=False)
        vertical_wall2 = InvisibleWall(k_size, self.rect.x + self.rect.width + 1, self.rect.y + 20 * k_size[1],
                                       self.rect.x + self.rect.width + 1, self.rect.y + self.rect.height + 1,
                                       wall_groups[1], wall_groups[2], color=(255, 255, 255, 0), do_move=False)
        self.walls = [horizontal_wall1, vertical_wall1, horizontal_wall2, vertical_wall2]

    def update(self, *args, **kwargs):
        if not pygame.sprite.spritecollideany(self, args[0]):
            self.rect.y += self.falling_speed
        else:
            self.stopped = True
            if not self.walls_resized:
                for wall in self.walls:
                    wall.kill()

                horizontal_wall1 = InvisibleWall(self.k_size, self.rect.x, self.rect.y,
                                                 self.rect.x + self.rect.width,
                                                 self.rect.y, self.wall_groups[0], self.wall_groups[2], color=(0, 0, 0, 0), do_move=False)
                horizontal_wall2 = InvisibleWall(self.k_size, self.rect.x, self.rect.y + self.rect.height,
                                                 self.rect.x + self.rect.width,
                                                 self.rect.y + self.rect.height, self.wall_groups[0],
                                                 self.wall_groups[2], color=(0, 0, 0, 0), do_move=False)
                vertical_wall1 = InvisibleWall(self.k_size, self.rect.x, self.rect.y + 20 * self.k_size[1], self.rect.x,
                                               self.rect.y + self.rect.height, self.wall_groups[1],
                                               self.wall_groups[2], color=(0, 0, 0, 0), do_move=False)
                vertical_wall2 = InvisibleWall(self.k_size, self.rect.x + self.rect.width,
                                               self.rect.y + 20 * self.k_size[1],
                                               self.rect.x + self.rect.width, self.rect.y + self.rect.height,
                                               self.wall_groups[1], self.wall_groups[2], color=(0, 0, 0, 0), do_move=False)
                self.walls = [horizontal_wall1, vertical_wall1, horizontal_wall2, vertical_wall2]
                self.walls_resized = True
        if not self.stopped:
            for wall in self.walls:
                wall.rect.y += self.falling_speed
        if abs(self.rect.x - self.obj.rect.x) > 2000 or abs(self.rect.y - self.obj.rect.y) > 2000:
            self.kill()


class GameLevel(pygame.sprite.Sprite):
    def __init__(self, k_size, img, portal1, portal2, obj_groups, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * k_size[0]), round(self.image.get_height() * k_size[1])))
        self.rect = self.image.get_rect(center=(300 * k_size[0], -265 * k_size[1]))
        self.start_portal = Portal(k_size, portal1[0], portal1[1], True, portal1[2], *obj_groups, *self.groups())
        self.end_portal = Portal(k_size, portal2[0], portal2[1], False, portal2[2], *obj_groups, *self.groups())

        self.completed = False

    def update(self, *args, **kwargs):
        if self.end_portal.is_done:
            del self.end_portal
            self.completed = True


class Portal(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, is_first, color, obj_groups, *groups):
        super().__init__(*groups)

        if is_first:
            self.phase = 'starting'
        else:
            self.phase = 'waiting'

        self.color = color

        self.is_first = is_first
        self.is_done = False
        self.k_size = k_size
        self.obj_groups = obj_groups

        self.i = 1
        self.counting_i = 0
        self.counting_max = 3
        self.for_slower = 0

        self.image = pygame.image.load(f'Game/images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * 6 * self.k_size[0]), round(self.image.get_height() * 6 * self.k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        start_snd = pygame.mixer.Sound('Game/sounds/teleport_entering.mp3')
        start_snd.play()

    def update(self, *args, **kwargs):
        self.for_slower += 1
        if self.for_slower % 2 == 0:
            if self.phase == 'starting':
                self.image = pygame.image.load(f'Game/images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 6 * self.k_size[0]),
                    round(self.image.get_height() * 6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.i += 1
                if self.i == 8:
                    self.i = 1
                    self.phase = 'waiting'

            if self.phase == 'waiting':
                self.image = pygame.image.load(f'Game/images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 6 * self.k_size[0]),
                    round(self.image.get_height() * 6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.i += 1

                if self.i == 8:
                    self.i = 1
                    if self.is_first:
                        self.counting_i += 1

                if self.counting_i == self.counting_max:
                    self.phase = 'ending'

            if self.phase == 'ending':
                self.image = pygame.image.load(f'Game/images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 6 * self.k_size[0]),
                    round(self.image.get_height() * 6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.i += 1
                if self.i == 6:
                    self.i = 1
                    self.is_done = True
                    close_snd = pygame.mixer.Sound('Game/sounds/teleport_closing.mp3')
                    close_snd.play()
                    self.kill()
        if self.phase != 'ending' and isinstance(pygame.sprite.spritecollideany(self, self.obj_groups),
                                                 Player) and not self.is_first:
            self.phase = 'ending'
            self.i = 1
