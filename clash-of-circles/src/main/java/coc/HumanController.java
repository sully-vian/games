package coc;

import javafx.geometry.Point2D;
import javafx.scene.Scene;
import javafx.scene.input.KeyCode;

public class HumanController extends Controller {

    private boolean upPressed;
    private boolean downPressed;
    private boolean leftPressed;
    private boolean rightPressed;
    private boolean attackPressed;

    private final Controls controls;

    public HumanController(Scene scene, Controls controls) {
        this.controls = controls;
    }

    @Override
    public Point2D getNextMove() {
        double dx = 0;
        double dy = 0;
        if (upPressed) {
            dy -= 1;
        }
        if (downPressed) {
            dy += 1;
        }
        if (leftPressed) {
            dx -= 1;
        }
        if (rightPressed) {
            dx += 1;
        }

        return new Point2D(dx, dy);
    }

    @Override
    public boolean shouldAttack() {
        boolean result = this.attackPressed;
        this.attackPressed = false; // Reset after checking
        return result;
    }

    public void updateKeyState(KeyCode code, boolean pressed) {
        if (code == controls.getUpKey()) {
            upPressed = pressed;
        } else if (code == controls.getDownKey()) {
            downPressed = pressed;
        } else if (code == controls.getLeftKey()) {
            leftPressed = pressed;
        } else if (code == controls.getRightKey()) {
            rightPressed = pressed;
        } else if (code == controls.getAttackKey()) {
            attackPressed = pressed;
        }
    }
}