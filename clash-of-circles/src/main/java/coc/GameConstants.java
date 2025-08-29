package coc;

import javafx.scene.paint.Color;

public final class GameConstants {

    // Arena
    public static final int ARENA_WIDTH = 800;
    public static final int ARENA_HEIGHT = 600;

    // Player mechanics
    public static final double PLAYER_SPEED = 3.0;

    // Visual
    public static final double PLAYER_RADIUS = 20.0;
    public static final Color BACKGROUND_COLOR = Color.BLACK;
    public static final Color BORDER_COLOR = Color.DARKGRAY;

    // misc
    public static final double MIN_PLAYER_X = Math.max(PLAYER_RADIUS, 0);
    public static final double MAX_PLAYER_X = ARENA_WIDTH - PLAYER_RADIUS;
    public static final double MIN_PLAYER_Y = Math.max(PLAYER_RADIUS, 0);
    public static final double MAX_PLAYER_Y = ARENA_HEIGHT - PLAYER_RADIUS;
    public static final long ATTACK_COOLDOWN = 5_000; // 5 seconds
    public static final double ATTACK_RADIUS = 100.0;
}