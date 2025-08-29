package coc;

import javafx.geometry.Point2D;
import javafx.scene.paint.Color;
import lombok.Getter;

public class GameState {

    @Getter
    private Player player1;

    @Getter
    private Player player2;

    private Controller controller1;
    private Controller controller2;

    private boolean gameOver;

    public GameState(Controller controller1, Controller controller2) {
        this.controller1 = controller1;
        this.controller2 = controller2;
        this.player1 = new Player(Color.RED, new Point2D(100, GameConstants.ARENA_HEIGHT / 2));
        this.player2 = new Player(Color.BLUE,
                new Point2D(GameConstants.ARENA_WIDTH - 100, GameConstants.ARENA_HEIGHT / 2));
    }

    public void update() {

        if (gameOver) {
            return;
        }

        Point2D move1 = controller1.getNextMove();
        Point2D move2 = controller2.getNextMove();

        player1.move(move1);
        player2.move(move2);

        if (controller1.shouldAttack() && player1.canAttack()) {
            if (player1.attack(player2)) {
                System.out.println("Player 1 attacked Player 2!");
                gameOver = true;
            } else {
                System.out.println("Player 1's attack missed!");
            }
        }

        if (controller2.shouldAttack() && player2.canAttack()) {
            if (player2.attack(player1)) {
                System.out.println("Player 2 attacked Player 1!");
                gameOver = true;
            } else {
                System.out.println("Player 2's attack missed!");
            }
        }
    }
}