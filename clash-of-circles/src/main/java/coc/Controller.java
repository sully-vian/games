package coc;

import javafx.geometry.Point2D;
import javafx.scene.input.KeyCode;

public abstract class Controller {

    /**
     * Decides the next move for the player based on current game state
     *
     * @return Direction vector for movement
     */
    public abstract Point2D getNextMove();

    /**
     * Decides whether to attack or not
     *
     * @return true if the player should attack
     */
    public abstract boolean shouldAttack();

    /**
     * Updates the controller state (called every frame)
     * This can be used for AI decision making, input processing, etc.
     *
     * @param gameState        Current state of the game
     * @param controlledPlayer The player controlled by this controller
     * @param opponent         The opponent player
     */
    public void update(GameState gameState, Player controlledPlayer, Player opponent) {
        // Default implementation does nothing
        // Override in subclasses if needed
    }
}