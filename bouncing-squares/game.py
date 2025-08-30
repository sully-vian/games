import pygame
from square import Square
from typing import Optional
import numpy as np
import config


class Game:
    def __init__(self) -> None:
        self.setupDisplay()
        self.setupSquares()
        self.setupAudio()

        self.gameOver: bool = False
        self.winner: Optional[str] = None
        self.font: pygame.font.Font = pygame.font.Font(None, 36)

    def setupDisplay(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode(
            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Bouncing Squares")
        self.clock: pygame.time.Clock = pygame.time.Clock()

    def setupSquares(self) -> None:
        speeds: np.ndarray = np.random.randint(
            config.MIN_SPEED, config.MAX_SPEED, size=4) * np.random.choice([-1, 1], size=4)
        self.blueSquare: Square = Square(100, 100, config.SQUARE_SIZE,
                                         config.BLUE, speeds[0], speeds[1], "Blue")
        self.greenSquare: Square = Square(600, 600, config.SQUARE_SIZE,
                                          config.GREEN, speeds[2], speeds[3], "Green")

    def setupAudio(self) -> None:
        t: np.ndarray = np.linspace(
            0, config.BIP_DURATION, int(config.SAMPLE_RATE * config.BIP_DURATION), False)
        wave: np.ndarray = (np.sin(2 * np.pi * config.BIP_FREQUENCY * t)
                            * 32767).astype(np.int16)
        stereoWave: np.ndarray = np.column_stack((wave, wave))
        self.bipSound: pygame.mixer.Sound = pygame.sndarray.make_sound(
            stereoWave)

    def checkCollision(self):
        blueRect: pygame.Rect = self.blueSquare.getRect()
        greenRect: pygame.Rect = self.greenSquare.getRect()

        if blueRect.colliderect(greenRect):
            overlapX: int = min(blueRect.right, greenRect.right) - \
                max(blueRect.left, greenRect.left)
            overlapY: int = min(blueRect.bottom, greenRect.bottom) - \
                max(blueRect.top, greenRect.top)

            if overlapX > overlapY:
                # vertical collision
                self.blueSquare.takeDamage()
                self.bipSound.play()
                if (not self.blueSquare.isAlive()):
                    self.gameOver = True
                    self.winner = "Green"
            else:
                # horizontal collision
                self.greenSquare.takeDamage()
                self.bipSound.play()
                if (not self.greenSquare.isAlive()):
                    self.gameOver = True
                    self.winner = "Blue"

            self.separateSquares()

    def separateSquares(self):
        if self.blueSquare.x < self.greenSquare.x:
            self.blueSquare.speedX = abs(self.blueSquare.speedX) * -1
            self.greenSquare.speedX = abs(self.greenSquare.speedX)
        else:
            self.blueSquare.speedX = abs(self.blueSquare.speedX)
            self.greenSquare.speedX = abs(self.greenSquare.speedX) * -1

        if self.blueSquare.y < self.greenSquare.y:
            self.blueSquare.speedY = abs(self.blueSquare.speedY) * -1
            self.greenSquare.speedY = abs(self.greenSquare.speedY)
        else:
            self.blueSquare.speedY = abs(self.blueSquare.speedY)
            self.greenSquare.speedY = abs(self.greenSquare.speedY) * -1

    def drawUI(self):
        if self.gameOver:
            line1: pygame.Surface = self.font.render(
                "Game Over!", True, config.WHITE)
            line2: pygame.Surface = self.font.render(
                f"{self.winner} Wins!", True, config.WHITE)
            line1Rect: pygame.Rect = line1.get_rect(
                center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 20))
            line2Rect: pygame.Rect = line2.get_rect(
                center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 20))
            self.screen.blit(line1, line1Rect)
            self.screen.blit(line2, line2Rect)

    def handleEvents(self) -> bool:
        """Handle pygame events. returns False if the game should quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in config.QUIT_KEYS:
                    return False
        return True

    def updateGameState(self) -> None:
        if not self.gameOver:
            self.blueSquare.move(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
            self.greenSquare.move(
                config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

            self.checkCollision()

    def render(self) -> None:
        self.screen.fill(config.BLACK)
        self.blueSquare.draw(self.screen)
        self.greenSquare.draw(self.screen)
        self.drawUI()
        pygame.display.flip()

    def run(self):
        running: bool = True
        while running:
            running = self.handleEvents()
            self.updateGameState()
            self.render()
            self.clock.tick(config.FPS)
