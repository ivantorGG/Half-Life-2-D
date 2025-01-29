from player import Player
from chargers import HEVCharger, HealthCharger
from food import FoodBox, FoodBottery, FoodGrenade, FoodMedkitBig, FoodMedkitSmall
from connecting_objects import Level, InvisibleWall
from objects import CrushedCarChained, GameLevel
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


def first_level():
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()

    walls_are_visible = True
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', (0, 0), (0, 0), level_sprites)
    InvisibleWall(-500, -1000, -500, 1000, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(1100, -1000, 1100, 1000, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(-500, 150, 310, 150, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    InvisibleWall(310, 240, 510, 240, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(310, 180, 310, 250, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(510, 180, 510, 250, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(510, 150, 640, 150, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(790, 180, 790, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(640, 180, 640, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(790, 150, 1100, 150, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', level_sprites)

    health_charger = HealthCharger(k_size, 900, 0, 30, all_sprites)

    player = Player(k_size, screen, 0, 0, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    FoodBottery(k_size, 700, 0, player, all_sprites)
    FoodMedkitSmall(k_size, 420, 210, player, all_sprites)

    while True:
        controls.first_level_check_events(player, all_sprites, invisible_horizontal_walls, invisible_vertical_walls,
                                          None,
                                          health_charger)

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(None, invisible_horizontal_walls, invisible_vertical_walls)
        all_sprites.draw(screen)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if player.go_again:
            first_level()
        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)

        pygame.display.flip()
        cloak.tick(FPS)


def main():
    pre_screen()
    pygame.mouse.set_visible(False)
    first_level()


main()
