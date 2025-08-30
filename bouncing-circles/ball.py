import config
import pygame
import math
from typing import Callable


class Ball:
    def __init__(self, posX: int, posY: int, velX: int, velY: int, size: int) -> None:
        self.posX: float = posX
        self.posY: float = posY
        self.velX: float = velX
        self.velY: float = velY
        self.size: int = size

    def draw(self, surface: pygame.Surface) -> None:
        posXInt: int = int(self.posX)
        posYInt: int = int(self.posY)
        pygame.draw.circle(surface, config.RED,
                           (posXInt, posYInt), self.size, config.BALL_BORDER)

    def move(self, getNextSound: Callable[[], pygame.mixer.Sound]) -> None:
        if self.size >= config.ARENA_RADIUS:
            self.posX = config.CENTER_X
            self.posY = config.CENTER_Y
            return

        self.posX += self.velX
        self.posY += self.velY

        self.velY += config.GRAVITY

        arenaCenterX: int = config.CENTER_X
        arenaCenterY: int = config.CENTER_Y

        dx: float = self.posX - arenaCenterX
        dy: float = self.posY - arenaCenterY
        norm: float = math.sqrt(dx * dx + dy * dy)

        if norm + self.size >= config.ARENA_RADIUS:
            self.size += config.GROWTH_ON_BOUNCE

            # normalize
            dx /= norm
            dy /= norm

            dotProd: float = self.velX * dx + self.velY * dy
            self.velX -= 2 * dotProd * dx
            self.velY -= 2 * dotProd * dy

            # move ball back inside the arena
            self.posX = arenaCenterX + dx * (config.ARENA_RADIUS - self.size)
            self.posY = arenaCenterY + dy * (config.ARENA_RADIUS - self.size)

            getNextSound().play()
