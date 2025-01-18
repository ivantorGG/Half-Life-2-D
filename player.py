import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/gordon/right/stand.png')
        self.image = pygame.transform.scale(self.image, (round(1.4 * 83 * k_size[0]), round(1.4 * 208 * k_size[1])))
        self.rect = self.image.get_rect(center=(x, y))

        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.is_now_jumping = False
        self.crouch = False
        self.jumping_speed = -30
        self.direction = 'right'

        self.player_health = 10
        self.suit_health = 10

        self.curr_weapon = None

        self.phase = 0
        self.for_slower = 0
        self.count_jumped = 0
        self.jumped_direction = ''

        self.k_size = k_size

    def move_player(self, plus_x, plus_y):
        self.rect.x += plus_x
        self.rect.y += plus_y

    def print_stats(self):
        print(f'player_health:{self.player_health}')
        print(f'suit_health:{self.suit_health}')
        print()

    def update(self, *args, **kwargs):
        self.update_animation_phases()
        if self.move_left:
            self.move_player(-10, 0)
        if self.move_right:
            self.move_player(10, 0)
        if self.jumping or self.jumping_speed != -30:
            if self.jumping_speed not in (30, 28, 26, 24, 22, -26, -28, -30, -24, -22):
                self.move_player(0, self.jumping_speed)
            if self.jumping_speed < 30:
                self.jumping_speed += 2
            else:
                self.jumping_speed = -30
        else:
            self.is_now_jumping = False

        if (self.move_right or self.move_left) and \
                self.direction != 'Jump-Right' and self.direction != 'Jump-Left':  # если только бегает
            self.for_slower += 1
            if self.for_slower % 3 == 0:
                self.phase = (self.phase + 1) % 8
                if not self.phase:
                    self.phase += 1
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/{self.phase}.png'),
                    (round(1.4 * 83 * self.k_size[0]), round(1.4 * 208 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
            if self.count_jumped != 0:
                self.count_jumped -= 1
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.jumped_direction}/last.png'),
                    (round(209 * self.k_size[0]), round(264 * self.k_size[1])))
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                (round(1.4 * 83 * self.k_size[0]), round(1.4 * 208 * self.k_size[1])))
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
            if self.count_jumped != 0:
                self.count_jumped -= 1
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.jumped_direction}/last.png'),
                    (round(209 * self.k_size[0]), round(264 * self.k_size[1])))

        if self.is_now_jumping:  # если прыгает
            if self.jumping_speed in (-26, -28):
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/pre-1.png'),
                    (round(284 * self.k_size[0] / 2), round(500 * self.k_size[1] / 2)))
            elif self.jumping_speed in (-22, -24):
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/pre-2.png'),
                    (round(328 * self.k_size[0] / 2), round(500 * self.k_size[1] / 2)))
            elif self.jumping_speed in (30, 28, 26):
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/last.png'),
                    (round(209 * self.k_size[0]), round(264 * self.k_size[1])))
                self.count_jumped = 3
                self.jumped_direction = self.direction
            elif -30 < self.jumping_speed <= -10:
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/1.png'),
                    (round(358 * self.k_size[0] / 2), round(500 * self.k_size[1] / 2)))
            elif -10 < self.jumping_speed <= 0:
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/2.png'),
                    (round(358 * self.k_size[0] / 2), round(500 * self.k_size[1] / 2)))
            elif 0 < self.jumping_speed <= 10:
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/3.png'),
                    (round(358 * self.k_size[0] / 2), round(500 * self.k_size[1] / 2)))
            elif 10 < self.jumping_speed <= 30:
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/4.png'),
                    (round(358 * self.k_size[0] / 2), round(500 * self.k_size[1] / 2)))

    def update_animation_phases(self):
        if self.move_left and self.jumping:
            self.direction = 'Jump-Left'

        if self.move_right and self.jumping:
            self.direction = 'Jump-Right'

        if self.move_left and not self.is_now_jumping:
            self.direction = 'left'

        if self.move_right and not self.is_now_jumping:
            self.direction = 'right'

        # if self.jumping and not self.move_right and not self.move_left:
        #     self.direction = ''
