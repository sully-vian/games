package coc;

import javafx.scene.input.KeyCode;
import lombok.Getter;

@Getter
public class Controls {

    private final KeyCode upKey;
    private final KeyCode downKey;
    private final KeyCode leftKey;
    private final KeyCode rightKey;
    private final KeyCode attackKey;

    public Controls(KeyCode upKey, KeyCode downKey, KeyCode leftKey, KeyCode rightKey, KeyCode attackKey) {
        this.upKey = upKey;
        this.downKey = downKey;
        this.leftKey = leftKey;
        this.rightKey = rightKey;
        this.attackKey = attackKey;
    }

    public static Controls leftHandControls() {
        return new Controls(KeyCode.Z, KeyCode.S, KeyCode.Q, KeyCode.D, KeyCode.A);
    }

    public static Controls rightHandControls() {
        return new Controls(KeyCode.UP, KeyCode.DOWN, KeyCode.LEFT, KeyCode.RIGHT, KeyCode.M);
    }
}