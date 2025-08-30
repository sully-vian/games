import pygame


# ball config
BALL_RADIUS: int = 50
GRAVITY: float = 0.1
NUM_BALLS: int = 3
MIN_SPEED: int = 0
MAX_SPEED: int = 15
GROWTH_ON_BOUNCE: int = 10
BALL_BORDER: int = 2

# arena config
ARENA_RADIUS: int = 400
ARENA_BORDER: int = 5

# colors
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
BLUE: tuple[int, int, int] = (0, 100, 255)
GREEN: tuple[int, int, int] = (0, 255, 100)
RED: tuple[int, int, int] = (255, 0, 0)

# screen config
SCREEN_HEIGHT: int = 800
SCREEN_WIDTH: int = 800
CENTER_X: int = SCREEN_WIDTH // 2
CENTER_Y: int = SCREEN_HEIGHT // 2

FPS: int = 60

# controls
QUIT_KEYS: list[int] = [pygame.K_ESCAPE, pygame.K_q]

# Audio config
BIP_FREQUENCY: int = 800  # Hz
BIP_DURATION: float = 0.1  # seconds
SAMPLE_RATE: int = 44100  # Hz

NOTE_DURATION: float = 0.3  # seconds
MELODY_NOTES: list[int] = [60, 62, 64, 67, 69, 72, 74, 76]
