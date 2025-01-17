import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.crouch = False
        self.jumping_speed = -30
        self.direction = 'right'

        self.player_health = 10
        self.suit_health = 10
        self.phase = 0
        self.for_slower = 0
        self.animation_phases = [
            pygame.image.load('images/gordon/right/1.png'),
            pygame.image.load('images/gordon/right/2.png'),
            pygame.image.load('images/gordon/right/3.png'),
            pygame.image.load('images/gordon/right/4.png'),
            pygame.image.load('images/gordon/right/5.png'),
            pygame.image.load('images/gordon/right/6.png'),
            pygame.image.load('images/gordon/right/7.png')
        ]

        self.image = pygame.image.load('images/gordon/right/stand.png')
        self.rect = self.image.get_rect(center=(x, y))

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
            self.move_player(-15, 0)
        if self.move_right:
            self.move_player(15, 0)
        if self.jumping or self.jumping_speed != -30:
            self.move_player(0, self.jumping_speed)
            if self.jumping_speed < 30:
                self.jumping_speed += 2
            else:
                self.jumping_speed = -30

        if self.move_right or self.move_left or self.jumping:
            self.for_slower += 1
            if self.for_slower % 3 == 0:
                self.phase = (self.phase + 1) % len(self.animation_phases)
                self.image = self.animation_phases[self.phase]
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        else:

            self.image = pygame.image.load(f'images/gordon/{self.direction}/stand.png')
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

        # x, y = self.rect.x, self.rect.y
        # self.for_slower += 1
        # if self.for_slower % 4 == 0:
        #     if self.move_left or self.move_right or self.jumping:
        #         self.phase = (self.phase + 1) % len(self.animation_phases)
        #         self.update_animation_phases()
        #         self.image = self.animation_phases[self.phase]
        #         self.rect = self.image.get_rect()
        #
        #     if self.move_right:
        #         self.rect = self.rect.move(x - self.rect.x + 25, y - self.rect.y)
        #     if self.move_left:
        #         self.rect = self.rect.move(x - self.rect.x - 25, y - self.rect.y)
        #
        #     if not self.move_right and not self.move_left and not self.jumping:
        #         self.image = pygame.transform.scale(pygame.image.load('images/gordon/animation_run_right1.png'),
        #                                             (103, 238))
        #
        #         self.rect = self.image.get_rect()
        #         self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def update_animation_phases(self):
        pass
        # if self.move_left and self.jumping:
        #     self.animation_phases = [
        #         pygame.image.load('images/animation_run+jump_left1'),
        #         pygame.image.load('images/animation_run+jump_left2'),
        #         pygame.image.load('images/animation_run+jump_left3'),
        #         pygame.image.load('images/animation_run+jump_left4'),
        #         pygame.image.load('images/animation_run+jump_left5'),
        #         pygame.image.load('images/animation_run+jump_left6'),
        #     ]
        #     if self.phase <= 3:
        #         self.move_player(-5, 5)
        #     else:
        #         self.move_player(-5, -5)
        #
        # if self.move_right and self.jumping:
        #     self.animation_phases = [
        #         pygame.image.load('images/gordon/animation_run_right2.jpg'),
        #         pygame.image.load('images/gordon/animation_run_right3.jpg'),
        #         pygame.image.load('images/gordon/animation_run_right4.jpg'),
        #         pygame.image.load('images/gordon/animation_run_right5.jpg'),
        #         pygame.image.load('images/gordon/animation_run_right6.jpg'),
        #         pygame.image.load('images/gordon/animation_run_right7.jpg'),
        #         pygame.image.load('images/gordon/animation_run_right8.jpg'),
        #     ]
        #     self.move_player(5, self.jump_speed)
        #     self.jump_speed += 5
        #     if self.jump_speed == 30:
        #         self.jumping = False
        #         self.jump_speed = -30
        #
        # if self.move_left and not self.jumping:
        #     self.direction = 'left'
        #     self.animation_phases = [
        #             pygame.image.load('images/gordon/left/1.png'),
        #             pygame.image.load('images/gordon/left/2.png'),
        #             pygame.image.load('images/gordon/left/3.png'),
        #             pygame.image.load('images/gordon/left/4.png'),
        #             pygame.image.load('images/gordon/left/5.png'),
        #             pygame.image.load('images/gordon/left/6.png'),
        #             pygame.image.load('images/gordon/left/7.png')
        #         ]

        if self.move_right and not self.jumping:
            self.direction = 'right'
            self.animation_phases = [
                pygame.image.load('images/gordon/right/1.png'),
                pygame.image.load('images/gordon/right/2.png'),
                pygame.image.load('images/gordon/right/3.png'),
                pygame.image.load('images/gordon/right/4.png'),
                pygame.image.load('images/gordon/right/5.png'),
                pygame.image.load('images/gordon/right/6.png'),
                pygame.image.load('images/gordon/right/7.png')
            ]

        # if self.jumping and not self.move_right and not self.move_left:
        #     self.animation_phases = [
        #         pygame.image.load('images/animation_jump1'),
        #         pygame.image.load('images/animation_jump2'),
        #         pygame.image.load('images/animation_jump3'),
        #         pygame.image.load('images/animation_jump4'),
        #         pygame.image.load('images/animation_jump5'),
        #         pygame.image.load('images/animation_jump6'),
        #     ]


