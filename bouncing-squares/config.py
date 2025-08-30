import pygame

"""Game configuration constants."""

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
FPS: int = 60

# colors
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
BLUE: tuple[int, int, int] = (0, 100, 255)
GREEN: tuple[int, int, int] = (0, 255, 100)
RED: tuple[int, int, int] = (255, 0, 0)

# Game settings
SQUARE_SIZE: int = 150
MIN_SPEED: int = 10
MAX_SPEED: int = 15
STARTING_HEALTH: int = 10

# Audio settings
BIP_FREQUENCY: int = 800  # Hz
BIP_DURATION: float = 0.1  # seconds
SAMPLE_RATE: int = 44100  # Hz

# UI settings
FONT_SIZE: int = 36
BORDER_WIDTH: int = 5

# controls
QUIT_KEYS: list[int] = [pygame.K_ESCAPE, pygame.K_q]
