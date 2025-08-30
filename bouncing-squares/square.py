import pygame
from typing import Tuple, List
import config


class Square:
    def __init__(self, x: int, y: int, size: int, color: Tuple[int, int, int], speedX: int, speedY: int, name: str) -> None:
        self.x: int = x
        self.y: int = y
        self.size: int = size
        self.maxSize: int = size
        self.color: Tuple[int, int, int] = color
        self.speedX: int = speedX
        self.speedY: int = speedY
        self.name: str = name
        self.health: int = config.STARTING_HEALTH

    def move(self, screenWidth: int, screenHeight: int) -> None:
        self.x += self.speedX
        self.y += self.speedY

        # bounce off walls
        if (self.x < 0) or (self.x + self.size > screenWidth):
            self.speedX = -self.speedX
            self.x = max(0, min(self.x, screenWidth - self.size))

        if (self.y < 0) or (self.y + self.size > screenHeight):
            self.speedY = -self.speedY
            self.y = max(0, min(self.y, screenHeight - self.size))

    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.getRect())

        if self.name == "Blue":
            borders: List[pygame.Rect] = self.getVerticalSides()
        elif self.name == "Green":
            borders: List[pygame.Rect] = self.getHorizontalSides()
        else:
            borders = []

        for border in borders:
            pygame.draw.rect(screen, config.RED, border)

    def getVerticalSides(self,) -> List[pygame.Rect]:
        return [
            pygame.Rect(self.x, self.y, config.BORDER_WIDTH,
                        self.size),  # left side
            pygame.Rect(self.x + self.size - config.BORDER_WIDTH, self.y,
                        config.BORDER_WIDTH, self.size)  # right side
        ]

    def getHorizontalSides(self,) -> List[pygame.Rect]:
        return [
            pygame.Rect(self.x, self.y, self.size,
                        config.BORDER_WIDTH),  # top side
            pygame.Rect(self.x, self.y + self.size - config.BORDER_WIDTH,
                        self.size, config.BORDER_WIDTH)  # bottom side
        ]

    def takeDamage(self) -> None:
        self.health -= 1
        self.size = int(self.maxSize * (self.health / config.STARTING_HEALTH))

    def isAlive(self) -> bool:
        return self.health > 0
