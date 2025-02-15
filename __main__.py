# TODO: Create final stats
from player import Player
from chargers import HEVCharger, HealthCharger
from food import FoodBox, FoodBottery, FoodBullets, FoodMedkitBig, FoodMedkitSmall
from enemies import Crab, DirectCrab, TermenatorCrab, FlyingEnemy, DumbCrab, SummonerCrab
from connecting_objects import Level, InvisibleWall
from objects import Obstacle, GameLevel
import stats
import controls
from camera import Camera

from screeninfo import get_monitors
import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("HALF-LIFE: 2D")
size = width, height = get_monitors()[0].width * 1, get_monitors()[0].height * 1
k_size = width / 1600, height / 900

FPS = 60
cloak = pygame.time.Clock()
screen.fill((255, 255, 255))


def login():
    running = True


def pre_screen():
    running = True
    first_motion = True
    last_place = None
    image, all_sprites, draw_btn, draw_btn2, btn_x1, btn_y1, btn_x2, btn_y2, btn2_x1, btn2_y1, btn2_x2, btn2_y2 = stats.print_pre_screen(
        screen, width, height)
    while running:
        image, first_motion, last_place, running = controls.pre_screen_check_events(image, first_motion, last_place,
                                                                                    width, height, btn_x1, btn_y1,
                                                                                    btn_x2, btn_y2, btn2_x1, btn2_y1,
                                                                                    btn2_x2, btn2_y2)

        pygame.display.flip()
        cloak.tick(FPS)
        all_sprites.draw(screen)
        all_sprites.update()
        draw_btn()
        draw_btn2()
        if running is None:
            running = True


def first_level(player_health, player_suit_health, bullets):
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()

    walls_are_visible = False
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', (-300, -200, 'green'), (880, 0, 'purple'), [all_sprites],
                          level_sprites)

    InvisibleWall(k_size, -410, -180, -410, 200, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 950, -180, 950, 200, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, -450, 180, 210, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 220, 260, 350, 260, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 210, 200, 210, 240, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 350, 200, 350, 240, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 350, 180, 445, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 445, 200, 445, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 570, 200, 570, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 570, 180, 950, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', (-300, -200, 'green'), (880, 0, 'purple'), [all_sprites],
                          level_sprites)

    control_level = Level(k_size, None, 700, 148, all_sprites)
    player = Player(k_size, screen, -300, -200, player_health, player_suit_health, bullets, all_sprites)

    camera = Camera(width, height)
    camera.update(player)

    while True:
        do_break = controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                                     invisible_vertical_walls, level=control_level)

        if do_break:
            return True

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(invisible_horizontal_walls, invisible_vertical_walls)
        all_sprites.draw(screen)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if player.go_again:
            player_health, player_suit_health, bullets = first_level(player_health, player_suit_health, bullets)
            return player_health, player_suit_health, bullets
        camera.update(player)

        if level.completed:
            return player.health, player.suit_health, player.bullets

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)

        pygame.display.flip()
        cloak.tick(FPS)


def second_level(player_health, player_suit_health, bullets):
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()

    walls_are_visible = False
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/2.png', (-650, -500, 'purple'), (550, -250, 'purple'), [all_sprites],
                          level_sprites)

    InvisibleWall(k_size, -750, -97, -355, 240, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -235, -97, 258, 240, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 380, -97, 670, 240, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -730, -750, -730, -97, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 680, -750, 680, -97, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -354, -80, -354, -5, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, -232, -80, -232, -6, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 258, -96, 258, -5, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 380, -96, 380, -6, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/2.png', (-650, -500, 'purple'), (550, -250, 'purple'), [all_sprites],
                          level_sprites)

    player = Player(k_size, screen, -650, -300, player_health, player_suit_health, bullets, all_sprites)
    Crab(k_size, player, 100, -500, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    while True:
        do_break = controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                                     invisible_vertical_walls)

        if do_break:
            return True

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(invisible_horizontal_walls, invisible_vertical_walls)
        all_sprites.draw(screen)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if level.completed:
            return player.health, player.suit_health, player.bullets

        if player.go_again:
            player_health, player_suit_health = second_level(player_health, player_suit_health, bullets)
            return player_health, player_suit_health, bullets

        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)
        pygame.display.flip()
        cloak.tick(FPS)


def third_level(player_health, player_suit_health, bullets):
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()

    walls_are_visible = True
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/3.png', (-3050, -600, 'purple'), (4850, -330, 'purple'), [all_sprites],
                          level_sprites)

    InvisibleWall(k_size, -4200, -155, -2835, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2730, -155, -2640, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2540, -155, -2450, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2355, -155, -2258, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2228, -200, -2137, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1662, -400, -1380, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1990, -310, -1889, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2127, -250, -2030, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1825, -340, -1730, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1160, -400, -1075, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -980, -400, -788, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -510, -270, -320, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -60, -155, 400, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, 2490, -155, 2660, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, 4050, -150, 5180, -150, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, 5180, -560, 5180, -150, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    # вертикальные
    InvisibleWall(k_size, -3650, -777 + 20, -3650, -160 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -2835, -150 + 20, -2835, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2730, -150 + 20, -2730, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2640, -150 + 20, -2640, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2540, -150 + 20, -2540, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2450, -150 + 20, -2450, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2355, -150 + 20, -2355, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2258, -150 + 20, -2258, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1662, -400 + 20, -1662, -300 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1376, -400 + 20, -1376, -300 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1160, -400 + 20, -1160, -300 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1075, -400 + 20, -1075, -300 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -980, -400 + 20, -980, -300 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -788, -400 + 20, -788, -300 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -510, -260 + 20, -510, -150 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -320, -260 + 20, -320, -150 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -60, -150 + 20, -60, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 400, -150 + 20, 400, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 2490, -150 + 20, 2490, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 2660, -150 + 20, 2660, 0 + 20, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/3.png', (-3050, -600, 'purple'), (4850, -330, 'purple'), [all_sprites],
                          level_sprites)

    health_c = HealthCharger((k_size[0] * 0.8, k_size[1] * 0.8), -4170, -370, 30, all_sprites)
    hev_c = HEVCharger((k_size[0] * 0.8, k_size[1] * 0.8), -4370, -370, 20, all_sprites)
    player = Player(k_size, screen, -3050, -680, player_health, player_suit_health, bullets, all_sprites)

    DirectCrab(k_size, player, -1500, -340, -20, all_sprites)
    DirectCrab(k_size, player, -1600, -340, -20, all_sprites)
    DirectCrab(k_size, player, -1700, -340, -20, all_sprites)
    DirectCrab(k_size, player, -1800, -340, -20, all_sprites)
    DirectCrab(k_size, player, -1900, -340, -20, all_sprites)
    DirectCrab(k_size, player, -2000, -340, -20, all_sprites)

    FoodBox(k_size, -3200, -800, player, FoodBullets, invisible_horizontal_walls, all_sprites)
    FoodBox(k_size, -3200, -1100, player, FoodBullets, invisible_horizontal_walls, all_sprites)
    FoodBox(k_size, -3200, -1400, player, FoodBullets, invisible_horizontal_walls, all_sprites)

    camera = Camera(width, height)
    camera.update(player)

    create_obstacle1 = True
    spawn_termenator1 = True
    spawn_direct_crab1 = True
    spawn_direct_crab2 = True
    spawn_summoner_crab1 = True
    create_obstacle2 = True

    while True:
        do_break = controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                                     invisible_vertical_walls, HEV_charger=hev_c,
                                                     health_charger=health_c)

        if do_break:
            return True

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(invisible_horizontal_walls, invisible_vertical_walls)
        all_sprites.draw(screen)

        if player.x > -3050 and spawn_termenator1:
            TermenatorCrab(k_size, player, -500, 250, 6, all_sprites)
            for i in range(20):
                DirectCrab(k_size, player, -1500 - 200 * i, -150, 20, all_sprites)
                DirectCrab(k_size, player, 1200 + 200 * i, 750, -20, all_sprites)
            spawn_termenator1 = False

        if player.x > 0 and create_obstacle1:
            Obstacle(k_size, 1340, -10, 'images/objects/bridge1.png',
                     [invisible_horizontal_walls, invisible_vertical_walls, level_sprites], player, all_sprites)
            Obstacle(k_size, 1940, -300, 'images/objects/bridge1.png',
                     [invisible_horizontal_walls, invisible_vertical_walls, level_sprites], player, all_sprites)
            Obstacle(k_size, 2350, -600, 'images/objects/bridge1.png',
                     [invisible_horizontal_walls, invisible_vertical_walls, level_sprites], player, all_sprites)
            FoodBox(k_size, 3100, -800, player, FoodMedkitBig, invisible_horizontal_walls, all_sprites)
            FoodBox(k_size, 3100, -1200, player, FoodMedkitBig, invisible_horizontal_walls, all_sprites)
            create_obstacle1 = False

        if player.x > 2000 and create_obstacle2:
            Obstacle(k_size, 1570, -600, 'images/objects/bridge1.png',
                     [invisible_horizontal_walls, invisible_vertical_walls, level_sprites], player, all_sprites)
            Obstacle(k_size, 2120, -700, 'images/objects/bridge1.png',
                     [invisible_horizontal_walls, invisible_vertical_walls, level_sprites], player, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)
            DumbCrab(k_size, player, 1520, -650, all_sprites)

            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            DumbCrab(k_size, player, 2120, -800, all_sprites)
            create_obstacle2 = False

        if player.x > -800 and spawn_direct_crab1:
            spawn_direct_crab1 = False
            DirectCrab(k_size, player, 1500 + 400, 600, -20, all_sprites)
            DirectCrab(k_size, player, 1500 + 400, 400, -20, all_sprites)
            DirectCrab(k_size, player, 1500 + 400, 800, -20, all_sprites)
            DirectCrab(k_size, player, 1500 + 400, 1000, -20, all_sprites)
        if player.x > -1000 and spawn_direct_crab2:
            spawn_direct_crab2 = False
            DirectCrab(k_size, player, -1500, 500 - 115, 20, all_sprites)
            DirectCrab(k_size, player, -1500, 300 - 115, 20, all_sprites)
            DirectCrab(k_size, player, -1500, 700 - 115, 20, all_sprites)
            DirectCrab(k_size, player, -1500, 900 - 115, 20, all_sprites)
            DirectCrab(k_size, player, -1500, 1100 - 115, 20, all_sprites)

        if player.x > 1000 and spawn_summoner_crab1:
            spawn_summoner_crab1 = False
            SummonerCrab(k_size, player, 4500, -900, all_sprites)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if level.completed:
            return player.health, player.suit_health, player.bullets

        if player.go_again:
            player_health, player_suit_health, bullets = third_level(player_health, player_suit_health, bullets)
            return player_health, player_suit_health, bullets

        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)

        pygame.display.flip()
        cloak.tick(FPS)


def get_username():
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
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
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


def main():
    username = get_username()
    if username is None:
        return

    pygame.mouse.set_visible(True)
    pre_screen()
    pygame.mouse.set_visible(False)

    music = pygame.mixer.Sound('sounds/main_music1.mp3')
    music.play()

    player_health, player_suit_health, bullets = 30, 0, 0

    player_health, player_suit_health, bullets = first_level(player_health, player_suit_health, bullets)
    player_health, player_suit_health, bullets = second_level(player_health, player_suit_health, bullets)
    player_health, player_suit_health, bullets = third_level(player_health, player_suit_health, bullets)
    music.stop()


if __name__ == '__main__':
    while True:
        main()
