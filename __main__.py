from player import Player
from chargers import HEVCharger, HealthCharger
from stats import print_stats
import controls
import pygame


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("HALF-LIFE: 2D")

FPS = 60
cloak = pygame.time.Clock()


def main_screen():
    ...


def main_game():

    all_sprites = pygame.sprite.Group()

    HEV_charger = HEVCharger(50, 300, all_sprites)
    health_charger = HealthCharger(250, 300, all_sprites)
    player = Player(150, 300, all_sprites)

    while True:
        controls.check_events(player, all_sprites, HEV_charger, health_charger)

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        print_stats(screen, player)

        pygame.display.flip()
        cloak.tick(FPS)


main_screen()
main_game()
