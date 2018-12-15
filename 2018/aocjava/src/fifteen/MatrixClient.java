package fifteen;

import java.io.*;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

public class MatrixClient extends Application {
	public static void main(String[] args) throws IOException {
		launch(args);
	}

	private Thread gameThread;
	private Label l;
	private static int WIDTH=875;
	private static int HEIGHT=500;
	private static int REFRESH_MS = 1000; //ms

	//class that has the logic
	private GoblinBattle gb = new GoblinBattle(); //TODO change; CUSTOM Class here

	@Override
	public void start(Stage primaryStage) throws Exception {
		System.out.println("MatrixClient running");
		BorderPane bpane = new BorderPane();
		l = new Label();
		l.setFont(Font.font ("Courier New", FontWeight.BOLD, 24));
		
		// set to white on black
		bpane.setStyle("-fx-background-color:black;");
		l.setTextFill(Color.web("white"));
		
		bpane.setCenter(l);

		//run the game
		gameThread = new Thread(new Runnable() {
			@Override public void run() {
				while (true) {
					Platform.runLater(new Runnable() {
						@Override public void run() {
							
							l.setText( gb.tick() ); //CUSTOM Class here; return the output after one tick
							
						}
					});
					try {
						Thread.sleep(REFRESH_MS);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}});
		gameThread.start();

		Scene scene = new Scene(bpane,WIDTH,HEIGHT);
		primaryStage.setTitle("");
		primaryStage.setScene(scene);
		primaryStage.show();
		primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
			public void handle(WindowEvent we) {
				Platform.exit();
				System.exit(0);
				System.out.println("Bye.");
			}
		});

	}
}


