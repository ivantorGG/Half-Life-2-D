from player import Player
from chargers import HEVCharger, HealthCharger
from food import FoodBox, FoodBottery, FoodGrenade, FoodMedkitBig, FoodMedkitSmall
import stats
import controls
import pygame


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("HALF-LIFE: 2D")

FPS = 60
cloak = pygame.time.Clock()
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

    HEV_charger = HEVCharger(50, 300, all_sprites)
    health_charger = HealthCharger(250, 300, all_sprites)

    player = Player(150, 500, all_sprites)

    FoodBottery(50, 200, player, all_sprites)
    FoodMedkitSmall(100, 200, player, all_sprites)
    FoodMedkitBig(150, 200, player, all_sprites)
    FoodGrenade(200, 200, player, all_sprites)

    while True:
        controls.main_game_check_events(player, all_sprites, HEV_charger, health_charger)

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        stats.print_stats(screen, player)

        pygame.display.flip()
        cloak.tick(FPS)


main_game()
