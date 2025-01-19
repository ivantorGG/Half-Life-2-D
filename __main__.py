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
pygame.mouse.set_visible(False)
screen.fill((255, 255, 255))


def pre_screen():
    running = True
    while running:
        stats.print_pre_screen(screen)
        running = controls.pre_screen_check_events()
        pygame.display.flip()
        cloak.tick(FPS)
        if running is None:
            running = True


def main_game():
    all_sprites = pygame.sprite.Group()

    HEV_charger = HEVCharger(k_size, 50, 300, all_sprites)
    health_charger = HealthCharger(k_size, 250, 300, all_sprites)

    player = Player(k_size, 150, 500, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    FoodBottery(k_size, 50 + 500, 600, player, all_sprites)
    FoodMedkitSmall(k_size, 100 + 500, 600, player, all_sprites)
    FoodMedkitBig(k_size, 150 + 500, 600, player, all_sprites)
    FoodGrenade(k_size, 200 + 500, 600, player, all_sprites)
    FoodBox(k_size, 300 + 500, 600, player, FoodGrenade, all_sprites)

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


main_game()
