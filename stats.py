import pygame


def print_stats(screen, player):
    hl2_font = pygame.font.Font('fonts/halflife2.ttf', 50)
    normal_font = pygame.font.Font('fonts/Roboto-Regular.ttf', 23)

    # здоровье
    health_text = normal_font.render('жизнь', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.player_health), True, (244, 169, 0))

    health_text_x, health_text_y = 30, screen.get_height() - 55
    num_health_text_x, num_health_text_y = 112 if len(str(player.player_health)) == 3 else 120, screen.get_height() - 82

    r = pygame.draw.rect(screen, (10, 10, 10, 128), (health_text_x - 15, num_health_text_y - 10,
                                                     190, num_health_text.get_height() + 25), border_radius=20)

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128), (health_text_x - 15, num_health_text_y - 10,
                                                  190, num_health_text.get_height() + 25), 1, 20)

    # здоровье костюма
    health_text = normal_font.render('костюм', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.suit_health), True, (244, 169, 0))

    health_text_x, health_text_y = 260, screen.get_height() - 55
    num_health_text_x, num_health_text_y = 362 if len(str(player.suit_health)) == 3 else 370, screen.get_height() - 82

    pygame.draw.rect(screen, (10, 10, 10, 128), (health_text_x - 15, num_health_text_y - 10,
                                                 210, num_health_text.get_height() + 25), border_radius=20)

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128), (health_text_x - 15, num_health_text_y - 10,
                                                  210, num_health_text.get_height() + 25), 1, 20)
