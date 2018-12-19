package fifteen;

import java.io.*;
import java.util.ArrayList;

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
	private static int WIDTH=435;
	private static int HEIGHT=825;
	private static int REFRESH_MS = 100; //ms
	static String fname = "files/recording.txt"; //created by GoblinBattleOutput.java
	private static BufferedReader br;
	private static ArrayList<String> board;
	private static int tick = 0;

	@Override
	public void start(Stage primaryStage) throws Exception {
		System.out.println("MatrixClient running");

		board = new ArrayList<String>();
		br = new BufferedReader(new FileReader(fname));
		String line = "";
		String oneBoard = "";
		while ((line = br.readLine()) != null) {
			if (line.trim().length() == 0) {
				board.add(oneBoard);
				oneBoard = "";
			}
			oneBoard = oneBoard + line + "\n";
		}

		BorderPane bpane = new BorderPane();
		l = new Label();
		l.setFont(Font.font ("Courier New", FontWeight.BOLD, 20));

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

							if (tick < board.size())
								l.setText( board.get(tick++) );
							else
								System.out.println("game over.");

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
		primaryStage.setTitle("Elves vs. Goblins");
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


