# TODO: upgrade func print_pre_screen
import pygame


def print_pre_screen(screen, width, height):
    def draw_btn():
        screen.blit(text, (round(40 * (width / 1600)), round(400 * (width / 1600))))
        x1, y1, width1, height1 = round(20 * (width / 1600)), round(395 * (height / 900)), round(
            505 * (width / 1600)), round(60 * (height / 900))
        pygame.draw.rect(screen, (205, 205, 200), (x1, y1, width1, height1), round(3 * (width / 1600)))

    class PreImage(pygame.sprite.Sprite):
        def __init__(self, *groups):
            super().__init__(*groups)
            self.image = pygame.image.load('images/gordon/on_minimum.png')
            self.image = pygame.transform.scale(self.image, (width * 1.2, height * 1.2))
            self.rect = self.image.get_rect()
            self.rect.x = -(width * 1.2 - width) // 2
            self.rect.y = -(height * 1.2 - height) // 2

    all_sprites = pygame.sprite.Group()
    pre_image = PreImage(all_sprites)
    all_sprites.draw(screen)
    all_sprites.update()

    hl2_font = pygame.font.Font('fonts/halflife2.ttf', round(40 * (width / 1600)))
    text = hl2_font.render("HALF - LIFE'", True, (205, 205, 200))

    draw_btn()

    return pre_image, all_sprites, draw_btn


def print_stats(screen, k_size, player):
    hl2_font = pygame.font.Font('fonts/halflife2.ttf', round(50 * k_size[1]))
    normal_font = pygame.font.Font('fonts/Roboto-Regular.ttf', round(23 * k_size[1]))

    # здоровье
    health_text = normal_font.render('жизнь', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.player_health), True, (244, 169, 0))

    health_text_x, health_text_y = 30, screen.get_height() - round(10 + 45 * k_size[1])
    num_health_text_x, num_health_text_y = round(50 + 62 * k_size[1]) if len(str(player.player_health)) == 3 else round(
        50 + 70 * k_size[1]), screen.get_height() - round(12 + 70 * k_size[1])

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128), (health_text_x - 15, num_health_text_y - 10,
                                                  round(60 + 130 * k_size[1]), num_health_text.get_height() + 25), 1,
                     20)

    # здоровье костюма
    health_text = normal_font.render('костюм', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.suit_health), True, (244, 169, 0))

    health_text_x, health_text_y = round(120 + 130 * k_size[1]), screen.get_height() - round(10 + 45 * k_size[1])
    num_health_text_x, num_health_text_y = round(200 + 162 * k_size[1]) if len(str(player.suit_health)) == 3 else round(
        200 + 170 * k_size[1]), round(screen.get_height() - (12 + 70 * k_size[1]))

    pygame.draw.rect(screen, (10, 10, 10, 128), (health_text_x - 15, num_health_text_y - 10,
                                                 round(80 + 130 * k_size[1]), num_health_text.get_height() + 25),
                     border_radius=20)

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128), (health_text_x - 15, num_health_text_y - 10,
                                                  round(80 + 130 * k_size[1]), num_health_text.get_height() + 25), 1,
                     20)
