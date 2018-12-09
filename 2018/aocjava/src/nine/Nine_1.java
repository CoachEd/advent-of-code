
package nine;

public class Nine_1 {

	public static void main(String[] args) {
		int num_marbles = 71010;  //17 players with 1104 marbles doesn't match. I get Player 10 with 2720
		int num_players = 468;
		circle c = new circle(num_players);
		for (int i=0; i < num_marbles; i++) {
			node n = new node(i);
			c.insert(n);
			//c.printCircle();
		}
		
		System.out.println();
		long maxscore = -1;
		long maxindex = -1;
		for (int i=1; i < c.scores.length; i++) {
			System.out.println("Player " + i + ": " + c.scores[i]);
			if (c.scores[i] > maxscore) {
				maxscore = c.scores[i];
				maxindex = i;
			}
		}
		
		System.out.println("\nWINNER Player " + maxindex + " with " + maxscore);

	} //end MAIN

}





