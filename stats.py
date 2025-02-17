import random
import pygame


def print_pre_screen(screen, width, height):
    def draw_btn1():
        screen.blit(text, (round(40 * (width / 1600)), round(400 * (width / 1600))))
        x1, y1, width1, height1 = round(20 * (width / 1600)), round(395 * (height / 900)), round(
            505 * (width / 1600)), round(60 * (height / 900))
        pygame.draw.rect(screen, (205, 205, 200), (x1, y1, width1, height1), round(3 * (width / 1600)))
        return x1, y1, x1 + width1, y1 + height1

    def draw_btn2():
        screen.blit(text2, (round(40 * (width / 1600)), round(500 * (width / 1600))))
        x1, y1, width1, height1 = round(20 * (width / 1600)), round(495 * (height / 900)), round(
            180 * (width / 1600)), round(60 * (height / 900))
        pygame.draw.rect(screen, (205, 205, 200), (x1, y1, width1, height1), round(3 * (width / 1600)))
        return x1, y1, x1 + width1, y1 + height1

    class PreImage(pygame.sprite.Sprite):
        def __init__(self, *groups):
            super().__init__(*groups)
            img = pygame.image.load(random.choice(
                ['images/pre_screen/on_minimum.png',
                 'images/pre_screen/wake_up.png', 'images/pre_screen/no_chess.jpg',
                 "images/pre_screen/maxresdefault.jpg", "images/pre_screen/abeba.jpg"]))
            self.image = img
            self.image = pygame.transform.scale(self.image, (width * 1.2, height * 1.2))
            self.rect = self.image.get_rect()
            self.rect.x = -(width * 1.2 - width) // 2
            self.rect.y = -(height * 1.2 - height) // 2

    all_sprites = pygame.sprite.Group()
    pre_image = PreImage(all_sprites)
    all_sprites.draw(screen)
    all_sprites.update()

    hl2_font = pygame.font.Font('fonts/halflife2.ttf', round(40 * (width / 1600)))
    normal_font = pygame.font.Font('fonts/Roboto-Regular.ttf', round(40 * (width / 1600)))

    text = hl2_font.render("HALF - LIFE'", True, (205, 205, 200))
    text2 = normal_font.render("ВЫХОД", True, (205, 205, 200))

    btn_x1, btn_y1, btn_x2, btn_y2 = draw_btn1()
    btn2_x1, btn2_y1, btn2_x2, btn2_y2 = draw_btn2()

    return pre_image, all_sprites, draw_btn1, draw_btn2, btn_x1, btn_y1, btn_x2, btn_y2, btn2_x1, btn2_y1, btn2_x2, btn2_y2


def print_stats(screen, k_size, player):
    hl2_font = pygame.font.Font('fonts/halflife2.ttf', round(50 * k_size[0]))
    normal_font = pygame.font.Font('fonts/Roboto-Regular.ttf', round(25 * k_size[0]))

    # здоровье
    health_text = normal_font.render('жизнь', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.health), True, (244, 169, 0))

    health_text_x, health_text_y = round(30 * k_size[0]), round((screen.get_height() - 55 * k_size[0]))
    num_health_text_x, num_health_text_y = round(105 * k_size[0]) if len(str(player.health)) == 3 else round(
        115 * k_size[0]), screen.get_height() - round(80 * k_size[0])
    # прямоугольник
    rect = pygame.Surface((round(200 * k_size[0]), round(num_health_text.get_height() + 25 * k_size[0])),
                          pygame.SRCALPHA)
    pygame.draw.rect(rect, (10, 10, 10, 198), (0, 0,
            round(200 * k_size[0]), round(num_health_text.get_height() + 25 * k_size[0])), border_radius=20)
    screen.blit(rect, (round(health_text_x - 15 * k_size[0]), round(num_health_text_y - 10 * k_size[0])))

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128),
                     (round(health_text_x - 15 * k_size[0]), round(num_health_text_y - 10 * k_size[0]),
                      round(round(200 * k_size[0])), round(num_health_text.get_height() + 25 * k_size[0])), 2,
                     20)

    # здоровье костюма
    health_text = normal_font.render('костюм', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.suit_health), True, (244, 169, 0))

    health_text_x, health_text_y = round(250 * k_size[0]), screen.get_height() - round(55 * k_size[0])
    num_health_text_x, num_health_text_y = round(350 * k_size[0]) if len(str(player.suit_health)) == 3 else round(
        370 * k_size[0]), round(screen.get_height() - (80 * k_size[0]))

    # прямоугольник
    rect = pygame.Surface((round(220 * k_size[0]), round(num_health_text.get_height() + 25 * k_size[0])),
                          pygame.SRCALPHA)
    pygame.draw.rect(rect, (10, 10, 10, 198), (0, 0,
                                               round(220 * k_size[0]),
                                               round(num_health_text.get_height() + 25 * k_size[0])), border_radius=20)
    screen.blit(rect, (round(health_text_x - 15 * k_size[0]), round(num_health_text_y - 10 * k_size[0])))

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    pygame.draw.rect(screen, (244, 169, 0, 128),
                     (round(health_text_x - 15 * k_size[0]), round(num_health_text_y - 10 * k_size[0]),
                      round(220 * k_size[0]), round(num_health_text.get_height() + 25 * k_size[0])), 2,
                     20)

    # патроны
    health_text = normal_font.render('патроны', True, (244, 169, 0))
    num_health_text = hl2_font.render(str(player.bullets), True, (244, 169, 0))
    bullets_icon = hl2_font.render('p', True, (244, 169, 0))

    health_text_x, health_text_y = screen.get_width() - round(230 * k_size[0]), screen.get_height() - round(
        45 * k_size[0])
    num_health_text_x, num_health_text_y = screen.get_width() - round(130 * k_size[0]) if len(
        str(player.bullets)) == 3 else screen.get_width() - round(
        115 * k_size[0]), round(screen.get_height() - (80 * k_size[0]))
    # прямоугольник
    rect = pygame.Surface((round(220 * k_size[0]), round(num_health_text.get_height() + 25 * k_size[0])),
                          pygame.SRCALPHA)
    pygame.draw.rect(rect, (10, 10, 10, 198), (0, 0,
                                               round(220 * k_size[0]),
                                               round(num_health_text.get_height() + 25 * k_size[0])), border_radius=20)
    screen.blit(rect, (round(health_text_x - 15 * k_size[0]), round(num_health_text_y - 10 * k_size[0])))

    screen.blit(health_text, (health_text_x, health_text_y))
    screen.blit(num_health_text, (num_health_text_x, num_health_text_y))

    bullets_count = 6 if player.bullets // 5 > 6 else player.bullets // 5
    if 5 > player.bullets > 0:
        bullets_count = 1
    if bullets_count > 0:
        bullets_icon_x, bullets_icon_y = screen.get_width() - round(230 * k_size[0]), screen.get_height() - round(
            80 * k_size[0])
        screen.blit(bullets_icon, (bullets_icon_x, bullets_icon_y))
    if bullets_count > 1:
        bullets_icon_x, bullets_icon_y = screen.get_width() - round(230 * k_size[0]), screen.get_height() - round(
            100 * k_size[0])
        screen.blit(bullets_icon, (bullets_icon_x, bullets_icon_y))
    if bullets_count > 2:
        bullets_icon_x, bullets_icon_y = screen.get_width() - round(195 * k_size[0]), screen.get_height() - round(
            100 * k_size[0])
        screen.blit(bullets_icon, (bullets_icon_x, bullets_icon_y))
    if bullets_count > 3:
        bullets_icon_x, bullets_icon_y = screen.get_width() - round(195 * k_size[0]), screen.get_height() - round(
            80 * k_size[0])
        screen.blit(bullets_icon, (bullets_icon_x, bullets_icon_y))
    if bullets_count > 4:
        bullets_icon_x, bullets_icon_y = screen.get_width() - round(160 * k_size[0]), screen.get_height() - round(
            100 * k_size[0])
        screen.blit(bullets_icon, (bullets_icon_x, bullets_icon_y))
    if bullets_count > 5:
        bullets_icon_x, bullets_icon_y = screen.get_width() - round(160 * k_size[0]), screen.get_height() - round(
            80 * k_size[0])
        screen.blit(bullets_icon, (bullets_icon_x, bullets_icon_y))

    pygame.draw.rect(screen, (244, 169, 0, 128),
                     (round(health_text_x - 15 * k_size[0]), round(num_health_text_y - 10 * k_size[0]),
                      round(220 * k_size[0]), round(num_health_text.get_height() + 25 * k_size[0])), 2,
                     20)


def print_death_screen(screen, i, play_sound):
    if play_sound:
        death_sound = pygame.mixer.Sound('sounds/player_died-long.mp3')
        death_sound.play()
    screen.fill((i, 0, 0))


def get_username(screen):
    pygame.display.set_caption("Введите ник")
    font = pygame.font.Font('fonts/Roboto-Regular.ttf', 36)
    clock = pygame.time.Clock()

    user_text = ""
    inputting = True

    while inputting:
        screen.fill((30, 30, 30))
        text_surface = font.render("Введите имя своего героя и нажмите Enter:", True, (255, 255, 255))
        screen.blit(text_surface, (50, 100))

        user_surface = font.render(user_text, True, (255, 255, 255))
        screen.blit(user_surface, (50, 150))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inputting = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        clock.tick(30)

    with open("username.txt", "w", encoding="utf-8") as file:
        file.write(user_text)

    return user_text


def sum_player_stats(*stats):
    result = {}
    for key in stats[0]:
        result[key] = stats[0][key]
        for stat in stats[1:]:
            result[key] += stat[key]

    record = 100
    record += result['crabs killed'] * 10
    record -= result['bullets shot']
    record -= result['damage took']
    record -= result['boxes crushed']
    record -= result['batteries ate']
    record -= result['medkits ate']
    record -= result['bullets ate']
    record -= result['HEVCharger used']
    record -= result['HealthCharger used']

    return result, record
