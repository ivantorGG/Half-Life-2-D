# TODO: upgrade func print_pre_screen
import pygame


def print_pre_screen(screen):
    hl2_font = pygame.font.Font('fonts/halflife2.ttf', 40)

    screen.fill((205, 205, 200))
    text = hl2_font.render("HALF - LIFE'", True, (0, 0, 0))
    screen.blit(text, (40, 400))

    pygame.draw.rect(screen, (0, 0, 0), (20, 395, 505, 60), 3)

    image = pygame.image.load('images/gordon/on_minimum.png')
    screen.blit(pygame.transform.scale(image, (900, 550)), (550, 180))


def print_stats(screen, k_size, player):
    hl2_font = pygame.font.Font('fonts/halflife2.ttf', round(50 * k_size[1]))
    normal_font = pygame.font.Font('fonts/Roboto-Regular.ttf', round(23 * k_size[1]))

    # здоровье
    health_text = normal_font.render('жизнь', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.player_health), True, (244, 169, 0))

    health_text_x, health_text_y = 30, screen.get_height() - round(10 + 45 * k_size[1])
    num_health_text_x, num_health_text_y = round(50 + 62 * k_size[1]) if len(str(player.player_health)) == 3 else round(50 + 70 * k_size[1]), screen.get_height() - round(12 + 70 * k_size[1])

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128), (health_text_x - 15, num_health_text_y - 10,
                                                  round(60 + 130 * k_size[1]), num_health_text.get_height() + 25), 1, 20)

    # здоровье костюма
    health_text = normal_font.render('костюм', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.suit_health), True, (244, 169, 0))

    health_text_x, health_text_y = round(120 + 130 * k_size[1]), screen.get_height() - round(10 + 45 * k_size[1])
    num_health_text_x, num_health_text_y = round(200 + 162 * k_size[1]) if len(str(player.suit_health)) == 3 else round(200 + 170 * k_size[1]), round(screen.get_height() - (12 + 70 * k_size[1]))

    pygame.draw.rect(screen, (10, 10, 10, 128), (health_text_x - 15, num_health_text_y - 10,
                                                 round(80 + 130 * k_size[1]), num_health_text.get_height() + 25), border_radius=20)

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128), (health_text_x - 15, num_health_text_y - 10,
                                                  round(80 + 130 * k_size[1]), num_health_text.get_height() + 25), 1, 20)
