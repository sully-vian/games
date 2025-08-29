package coc;

import javafx.animation.AnimationTimer;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.layout.Pane;
import javafx.scene.shape.ArcType;
import lombok.Setter;

public class GameView extends Pane {
    private Canvas canvas;
    private GraphicsContext gc;
    @Setter
    private GameState gameState;
    private AnimationTimer gameLoop;

    public GameView() {
        this.canvas = new Canvas(GameConstants.ARENA_WIDTH, GameConstants.ARENA_HEIGHT);
        this.gc = canvas.getGraphicsContext2D();
        this.getChildren().add(canvas);

        // Make sure this pane can receive focus for keyboard input
        this.setFocusTraversable(true);
    }

    public void startGameLoop() {
        this.gameLoop = new AnimationTimer() {
            @Override
            public void handle(long now) {
                if (gameState != null) {
                    gameState.update();
                    render();
                }
            }
        };
        this.gameLoop.start();
    }

    private void render() {
        // clear canvas
        gc.setFill(GameConstants.BACKGROUND_COLOR);
        gc.fillRect(0, 0, canvas.getWidth(), canvas.getHeight());

        // draw arena border
        gc.setStroke(GameConstants.BORDER_COLOR);
        gc.setLineWidth(5);
        gc.strokeRect(0, 0, canvas.getWidth(), canvas.getHeight());

        if (gameState != null) {
            // draw players
            drawPlayer(gameState.getPlayer1());
            drawPlayer(gameState.getPlayer2());

            drawAttackIndicator(gameState.getPlayer1());
            drawAttackIndicator(gameState.getPlayer2());
        }
    }

    private void drawPlayer(Player player) {
        if (!player.isAlive()) {
            gc.setFill(player.getColor().deriveColor(1, 1, 1, 0.3));
        } else {
            gc.setFill(player.getColor());
        }
        gc.fillOval(
                player.getPosition().getX() - GameConstants.PLAYER_RADIUS,
                player.getPosition().getY() - GameConstants.PLAYER_RADIUS,
                GameConstants.PLAYER_RADIUS * 2,
                GameConstants.PLAYER_RADIUS * 2);
    }

    private void drawAttackIndicator(Player player) {
        if (!player.isAlive()) {
            return;
        }

        if (player.canAttack()) {
            // draw attack range when ready
            gc.setStroke(player.getColor().deriveColor(1, 1, 1, 0.5));
            gc.setLineWidth(2);
            gc.strokeOval(
                    player.getPosition().getX() - GameConstants.ATTACK_RADIUS,
                    player.getPosition().getY() - GameConstants.ATTACK_RADIUS,
                    GameConstants.ATTACK_RADIUS * 2,
                    GameConstants.ATTACK_RADIUS * 2);
        } else {
            double progress = player.getAttackCooldownProgress();
            gc.setStroke(player.getColor().deriveColor(1, 1, 1, 0.3));
            gc.setLineWidth(3);
            double startAngle = -90; // top
            double arcExtent = 360 * progress;
            gc.strokeArc(
                    player.getPosition().getX() - GameConstants.ATTACK_RADIUS,
                    player.getPosition().getY() - GameConstants.ATTACK_RADIUS,
                    GameConstants.ATTACK_RADIUS * 2,
                    GameConstants.ATTACK_RADIUS * 2,
                    startAngle, arcExtent, ArcType.OPEN);
        }
    }
}