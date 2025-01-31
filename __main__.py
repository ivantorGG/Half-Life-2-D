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
        level = GameLevel(k_size, 'images/levels/1.png', (-300, -200, 'green'), (880, 0, 'green'), [all_sprites], level_sprites)

    InvisibleWall(-410, -300, -410, 200, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(950, -300, 950, 200, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(-450, 180, 220, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    InvisibleWall(220, 240, 350, 240, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(220, 200, 220, 240, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(350, 200, 350, 240, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(350, 180, 445, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(445, 200, 445, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(570, 200, 570, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(570, 180, 950, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', (-300, -200, 'green'), (880, 0, 'green'), all_sprites, level_sprites)

    control_level = Level(k_size, None, 700, 148, all_sprites)

    player = Player(k_size, screen, -300, -200, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    while True:
        controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                          invisible_vertical_walls, level=control_level)

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

        if level.completed:
            print(1)

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
