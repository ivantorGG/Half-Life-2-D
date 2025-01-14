import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.crouch = False
        self.player_health = 10
        self.suit_health = 10
        self.phase = 0
        self.for_slover = 1
        self.animation_phases = [
            pygame.image.load('images/gordon/animation_run_right2.jpg'),
            pygame.image.load('images/gordon/animation_run_right3.jpg'),
            pygame.image.load('images/gordon/animation_run_right4.jpg'),
            pygame.image.load('images/gordon/animation_run_right5.jpg'),
            pygame.image.load('images/gordon/animation_run_right6.jpg'),
            pygame.image.load('images/gordon/animation_run_right7.jpg'),
            pygame.image.load('images/gordon/animation_run_right8.jpg'),
        ]

        self.image = pygame.image.load('images/gordon/animation_run_right1.jpg')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def move_player(self, plus_x, plus_y):
        self.rect = self.rect.move(plus_x, plus_y)

    def print_stats(self):
        print(f'player_health:{self.player_health}')
        print(f'suit_health:{self.suit_health}')
        print()

    def update(self, *args, **kwargs):
        x, y = self.rect.x, self.rect.y
        self.for_slover += 1
        if self.for_slover % 4 == 0:
            if self.move_left or self.move_right or self.jumping:
                self.phase = (self.phase + 1) % len(self.animation_phases)
                self.update_animation_phases()
                self.image = self.animation_phases[self.phase]
                self.rect = self.image.get_rect()

            if self.move_right:
                self.rect = self.rect.move(x - self.rect.x + 25, y - self.rect.y)
            if self.move_left:
                self.rect = self.rect.move(x - self.rect.x - 25, y - self.rect.y)

            if not self.move_right and not self.move_left and not self.jumping:
                self.image = pygame.transform.scale(pygame.image.load('images/gordon/animation_run_right1.jpg'),
                                                    (103, 238))

                self.rect = self.image.get_rect()
                self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def update_animation_phases(self):
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

        # if self.move_right and self.jumping:
        #     self.animation_phases = [
        #         pygame.image.load('images/animation_run+jump_right1'),
        #         pygame.image.load('images/animation_run+jump_right2'),
        #         pygame.image.load('images/animation_run+jump_right3'),
        #         pygame.image.load('images/animation_run+jump_right4'),
        #         pygame.image.load('images/animation_run+jump_right5'),
        #         pygame.image.load('images/animation_run+jump_right6'),
        #         pygame.image.load('images/animation_run+jump_right7'),
        #         pygame.image.load('images/animation_run+jump_right8'),
        #     ]
        #     self.move_player(5, 5)
        #
        # if self.move_left and not self.jumping:
        #     self.animation_phases = [
        #         pygame.image.load('images/animation_run_left1'),
        #         pygame.image.load('images/animation_run_left2'),
        #         pygame.image.load('images/animation_run_left3'),
        #         pygame.image.load('images/animation_run_left4'),
        #         pygame.image.load('images/animation_run_left5'),
        #         pygame.image.load('images/animation_run_left6'),
        #         pygame.image.load('images/animation_run_left7'),
        #         pygame.image.load('images/animation_run_left8'),
        #     ]
        #     self.move_player(-5, 0)

        if self.move_right and not self.jumping:
            self.animation_phases = [
                pygame.image.load('images/gordon/animation_run_right2.jpg'),
                pygame.image.load('images/gordon/animation_run_right3.jpg'),
                pygame.image.load('images/gordon/animation_run_right4.jpg'),
                pygame.image.load('images/gordon/animation_run_right5.jpg'),
                pygame.image.load('images/gordon/animation_run_right6.jpg'),
                pygame.image.load('images/gordon/animation_run_right7.jpg'),
                pygame.image.load('images/gordon/animation_run_right8.jpg'),
            ]
            self.move_player(5, 0)

        # if self.jumping and not self.move_right and not self.move_left:
        #     self.animation_phases = [
        #         pygame.image.load('images/animation_jump1'),
        #         pygame.image.load('images/animation_jump2'),
        #         pygame.image.load('images/animation_jump3'),
        #         pygame.image.load('images/animation_jump4'),
        #         pygame.image.load('images/animation_jump5'),
        #         pygame.image.load('images/animation_jump6'),
        #     ]
