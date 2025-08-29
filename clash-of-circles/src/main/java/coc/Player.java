package coc;

import javafx.geometry.Point2D;
import javafx.scene.paint.Color;
import lombok.Getter;

public class Player {

    @Getter
    private Point2D position;

    @Getter
    private Color color;

    private long lastAttackTime;
    private boolean isAlive;

    public Player(Color color, Point2D initialPosition) {
        this.color = color;
        this.position = initialPosition;
        this.lastAttackTime = 0;
        this.isAlive = true;
    }

    public boolean isAlive() {
        return this.isAlive;
    }

    public void move(Point2D direction) {
        if (!isAlive || direction.magnitude() == 0) {
            return;
        }

        Point2D newPosition = position.add(direction.normalize().multiply(GameConstants.PLAYER_SPEED));

        // Keep in arena bounds
        double x = Math.max(GameConstants.MIN_PLAYER_X, Math.min(newPosition.getX(), GameConstants.MAX_PLAYER_X));
        double y = Math.max(GameConstants.MIN_PLAYER_Y, Math.min(newPosition.getY(), GameConstants.MAX_PLAYER_Y));
        this.position = new Point2D(x, y);
    }

    public boolean canAttack() {
        long currentTime = System.currentTimeMillis();
        long elapsed = currentTime - lastAttackTime;
        return elapsed >= GameConstants.ATTACK_COOLDOWN;
    }

    public boolean attack(Player opponent) {
        if (!isAlive || !opponent.isAlive || !canAttack()) {
            // no effect
            return false;
        }

        // attack used, lets see if it affects the other player
        lastAttackTime = System.currentTimeMillis(); // Reset attack cooldown

        double distance = position.distance(opponent.position);
        if (distance <= GameConstants.ATTACK_RADIUS) {
            opponent.isAlive = false; // Opponent is defeated
            return true; // Attack was successful
        }

        return false; // Attack was not successful
    }

    public double getAttackCooldownProgress() {
        if (canAttack()) {
            return 1.0;
        }
        long elapsed = System.currentTimeMillis() - lastAttackTime;
        return Math.min(1.0, (double) elapsed / GameConstants.ATTACK_COOLDOWN);
    }

}
