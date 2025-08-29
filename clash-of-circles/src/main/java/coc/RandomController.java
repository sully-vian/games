package coc;

import java.util.Random;

import javafx.geometry.Point2D;

public class RandomController extends Controller {

    private static final long MIN_DIRECTION_CHANGE_INTERVAL = 500;
    private static final long MAX_DIRECTION_CHANGE_INTERVAL = 2000;

    private static final double MOVE_PROBABILITY = 0.6;
    private static final double ATTACK_PROBABILITY = 0.02; // 2% chance per frame
    private static final long MIN_ATTACK_INTERVAL = 1000; // don"t spam attacks

    private final Random random = new Random();

    private Point2D currentDirection;
    private long lastAttackAttempt;
    private long nextDirectionChangeTime;

    public RandomController() {
        this.lastAttackAttempt = 0;
        generateNewDirection();
        scheduleNextDirectionChange();
    }

    @Override
    public Point2D getNextMove() {
        long currentTime = System.currentTimeMillis();

        if (currentTime >= nextDirectionChangeTime) {
            generateNewDirection();
            scheduleNextDirectionChange();
        }
        return this.currentDirection;
    }

    @Override
    public boolean shouldAttack() {
        long currenTime = System.currentTimeMillis();

        // don't attack to frequently
        long elapsed = currenTime - lastAttackAttempt;
        if (elapsed < MIN_ATTACK_INTERVAL) {
            // too early, don't attack
            return false;
        }

        if (random.nextDouble() < ATTACK_PROBABILITY) {
            // attack!
            lastAttackAttempt = currenTime;
            return true;
        }

        return false;
    }

    private void generateNewDirection() {
        // choose direction
        double angle = random.nextDouble() * 2 * Math.PI;

        // choose to move or not
        double magnitude = random.nextDouble() <= MOVE_PROBABILITY ? 1 : 0;

        if (magnitude > 0) {
            currentDirection = new Point2D(Math.cos(angle), Math.sin(angle));
        } else {
            currentDirection = new Point2D(0, 0); // stay still
        }
    }

    private void scheduleNextDirectionChange() {
        long interval = random.nextLong(MIN_DIRECTION_CHANGE_INTERVAL, MAX_DIRECTION_CHANGE_INTERVAL);
        long currentTime = System.currentTimeMillis();
        this.nextDirectionChangeTime = currentTime + interval;
    }
}