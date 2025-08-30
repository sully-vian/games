import pygame
import sys
from game import Game
import config


def main():
    pygame.init()
    game = Game()
    print(
        f"To quit the game, press one of the following keys: {[pygame.key.name(key) for key in config.QUIT_KEYS]}")
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
