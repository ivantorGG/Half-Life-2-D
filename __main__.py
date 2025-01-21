from player import Player
from chargers import HEVCharger, HealthCharger
from food import FoodBox, FoodBottery, FoodGrenade, FoodMedkitBig, FoodMedkitSmall
import stats
import controls
from camera import Camera


from screeninfo import get_monitors
import pygame


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("HALF-LIFE: 2D")
size = width, height = get_monitors()[0].width, get_monitors()[0].height
k_size = width / 1600, height / 900

FPS = 60
cloak = pygame.time.Clock()
screen.fill((255, 255, 255))


def pre_screen():
    running = True
    first_motion = True
    last_place = None
    image, all_sprites, draw_btn = stats.print_pre_screen(screen, width, height)
    while running:
        image, first_motion, last_place, running = controls.pre_screen_check_events(image, first_motion, last_place, width, height)

        pygame.display.flip()
        cloak.tick(FPS)
        all_sprites.draw(screen)
        all_sprites.update()
        draw_btn()
        if running is None:
            running = True


def main_game():
    all_sprites = pygame.sprite.Group()

    HEV_charger = HEVCharger(k_size, 50, 600, all_sprites)
    health_charger = HealthCharger(k_size, 250, 600, all_sprites)

    player = Player(k_size, 150, 700, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    FoodBottery(k_size, 400, 600, player, all_sprites)
    FoodMedkitSmall(k_size, -200, 600, player, all_sprites)
    FoodMedkitBig(k_size, -350, 600, player, all_sprites)
    FoodGrenade(k_size, 700, 600, player, all_sprites)

    FoodBox(k_size, 800, 600, player, FoodGrenade, all_sprites)
    FoodBox(k_size, 900, 600, player, FoodBottery, all_sprites)
    FoodBox(k_size, 1000, 600, player, FoodMedkitBig, all_sprites)
    FoodBox(k_size, 1100, 600, player, FoodMedkitSmall, all_sprites)

    FoodBox(k_size, 800, 500, player, FoodGrenade, all_sprites)
    FoodBox(k_size, 900, 500, player, FoodBottery, all_sprites)
    FoodBox(k_size, 1000, 500, player, FoodBottery, all_sprites)
    FoodBox(k_size, 1100, 500, player, FoodBottery, all_sprites)

    while True:
        controls.main_game_check_events(player, all_sprites, HEV_charger, health_charger)

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        stats.print_stats(screen, k_size, player)
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        pygame.display.flip()
        cloak.tick(FPS)


pre_screen()
pygame.mouse.set_visible(False)
main_game()
