package coc;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.KeyCode;
import javafx.stage.Stage;

public class App extends Application {

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Clash of Circles");

        GameView gameView = new GameView();
        Scene scene = new Scene(gameView, GameConstants.ARENA_WIDTH, GameConstants.ARENA_HEIGHT);

        Controller redController = new HumanController(scene, Controls.leftHandControls());
        Controller blueController = new HumanController(scene, Controls.rightHandControls());

        scene.setOnKeyPressed(e -> {
            if (e.getCode() == KeyCode.ESCAPE) {
                primaryStage.close();
                return;
            }
            redController.updateKeyState(e.getCode(), true);
            blueController.updateKeyState(e.getCode(), true);
        });

        scene.setOnKeyReleased(e -> {
            redController.updateKeyState(e.getCode(), false);
            blueController.updateKeyState(e.getCode(), false);
        });

        GameState gameState = new GameState(redController, blueController);
        gameView.setGameState(gameState);

        primaryStage.setScene(scene);
        primaryStage.show();

        // Ensure the scene is focused to receive key events
        scene.getRoot().requestFocus();

        gameView.startGameLoop();
    }

    public static void main(String[] args) {
        launch(args);
    }

}
