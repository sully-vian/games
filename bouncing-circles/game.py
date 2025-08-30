from ball import Ball
import config
import pygame
from typing import List
import numpy as np
from audio import AudioManager


class Game:
    def __init__(self, melodyFile: str) -> None:
        # random speeds
        speeds: np.ndarray = np.random.randint(
            config.MIN_SPEED, config.MAX_SPEED, size=(config.NUM_BALLS, 2)) * np.random.choice([-1, 1], size=(config.NUM_BALLS, 2))

        self.balls: List[Ball] = [Ball(
            config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2, velX, velY, config.BALL_RADIUS)
            for velX, velY in speeds]

        self.setupDisplay()
        self.audioManager: AudioManager = AudioManager(melodyFile)

    def setupDisplay(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Bouncing Circles")
        self.clock: pygame.time.Clock = pygame.time.Clock()

    def handleEvents(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in config.QUIT_KEYS:
                    return False
        return True

    def updateGameState(self) -> None:
        for ball in self.balls:
            ball.move(self.audioManager.getNextSound)

    def drawArena(self) -> None:
        arenaCenter: tuple[int, int] = (
            config.CENTER_X, config.CENTER_Y)
        pygame.draw.circle(self.screen, config.WHITE, arenaCenter,
                           config.ARENA_RADIUS, config.ARENA_BORDER)

    def render(self) -> None:
        self.screen.fill(config.BLACK)

        self.drawArena()
        for ball in self.balls:
            ball.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:
        running: bool = True
        while running:
            running = self.handleEvents()
            self.updateGameState()
            self.render()
            self.clock.tick(config.FPS)
