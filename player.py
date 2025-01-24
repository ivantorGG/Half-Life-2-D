import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/gordon/right/stand.png')
        self.image = pygame.transform.scale(self.image, (round(1.4 * 83 * k_size[0]), round(1.4 * 208 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.mask = pygame.mask.from_surface(self.image)

        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.is_now_jumping = False
        self.crouch = False
        self.jumping_speed = -60
        self.direction = 'right'

        self.player_health = 10
        self.suit_health = 10

        self.curr_weapon = None

        self.phase = 0
        self.for_slower = 1
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

        if not pygame.sprite.spritecollideany(self, args[1]) and not (
                args[0].mask is not None and pygame.sprite.collide_mask(self, args[0]) is not None or
                args[0].car is not None and pygame.sprite.collide_mask(self, args[0].car) is not None):
            self.move_player(0, 20)

        elif self.jumping:
            self.is_now_jumping = True

        if self.move_left:
            self.move_player(-10, 0)
            if args[0].mask is not None and pygame.sprite.collide_mask(self, args[0]) is not None or \
                    args[0].car is not None and pygame.sprite.collide_mask(self, args[0].car) is not None or \
                    pygame.sprite.spritecollideany(self, args[2]):
                self.move_player(10, 0)

        if self.move_right:
            self.move_player(10, 0)
            if args[0].mask is not None and pygame.sprite.collide_mask(self, args[0]) is not None or \
                    args[0].car is not None and pygame.sprite.collide_mask(self, args[0].car) is not None or \
                    pygame.sprite.spritecollideany(self, args[2]):
                self.move_player(-10, 0)

        if (self.move_right or self.move_left) and \
                self.direction != 'Jump-Right' and self.direction != 'Jump-Left':  # если только бегает
            self.for_slower += 1
            if self.for_slower % 5 == 0:
                self.phase = (self.phase + 2) % 8
                if not self.phase:
                    self.phase += 2
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/{self.phase}.png'),
                    (round(1.4 * 83 * self.k_size[0]), round(1.4 * 208 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        elif self.direction != 'Jump-Right' and self.direction != 'Jump-Left':
            self.image = pygame.transform.scale(
                pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                (round(1.4 * 83 * self.k_size[0]), round(1.4 * 208 * self.k_size[1])))
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

        elif (self.direction == 'Jump-Right' or self.direction == 'Jump-Left') and self.is_now_jumping:
            self.image = pygame.transform.scale(pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                                                (round(352 / 2 * self.k_size[0]), round(500 / 2 * self.k_size[1])))
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
            self.move_player(0, self.jumping_speed)
            self.jumping_speed += 4
            if self.jumping_speed == 0:
                self.jumping_speed = -60
                self.is_now_jumping = False

        self.mask = pygame.mask.from_surface(self.image)

    def update_animation_phases(self):
        if self.move_left and self.jumping:
            self.direction = 'Jump-Left'

        if self.move_right and self.jumping:
            self.direction = 'Jump-Right'

        if self.move_left and not self.is_now_jumping:
            self.direction = 'left'

        if self.move_right and not self.is_now_jumping:
            self.direction = 'right'

        if self.jumping and not self.move_right and not self.move_left and \
                self.direction != 'Jump-Right' and self.direction != 'Jump-Left':
            if self.direction == 'right':
                self.direction = 'Jump-Right'
            elif self.direction == 'left':
                self.direction = 'Jump-Left'
