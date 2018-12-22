package eighteen;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
/*
 * This program gave me the repeating order. Just project it out to 1000000000...
t=10000    combo: 614|359
t=20000    combo: 561|372
t=30000    combo: 536|329
t=40000    combo: 546|314*
t=50000    combo: 572|316
t=60000    combo: 597|333
t=70000    combo: 607|352

t=80000    combo: 614|359
t=90000    combo: 561|372
t=100000    combo: 536|329
t=110000    combo: 546|314*
t=120000    combo: 572|316
t=130000    combo: 597|333
t=140000    combo: 607|352

t=150000    combo: 614|359
t=160000    combo: 561|372
t=170000    combo: 536|329
t=180000    combo: 546|314*
t=190000    combo: 572|316
t=200000    combo: 597|333
t=210000    combo: 607|352


0: 999960000
1: 999970000
2: 999980000
3: 999990000
4: 1000000000
answer: 180752 (546*314)

 */
public class Part_1_18 {

	//static String fname = "files/18_0.txt"; //sample data
	static String fname = "files/18_1.txt"; //Part 1 & 2 data
	//static int minutes = 10; //Part 1 duration
	static int minutes = 1000000000; //Part 2 duration

	static boolean bShowForest = false; //Part 2

	static final char OPEN = '.';
	static final char TREES = '|';
	static final char LUMBER = '#';
	static int DELAY_MS = 0;

	public static void main(String[] args) {
		HashSet<String> hmSeen = new HashSet<String>();
		long startms = System.currentTimeMillis();
		ArrayList<String> al = new ArrayList<String>();
		try (BufferedReader br = new BufferedReader(new FileReader(fname))) {
			String line;
			int cols = 0;
			while ((line = br.readLine()) != null) {
				al.add(line);
				cols = line.length();
			}
			br.close();

			//populate map
			char[][] forest = new char[al.size()][cols];
			for (int row=0; row < al.size(); row++) {
				String s = al.get(row);
				for (int col=0; col < s.length(); col++)
					forest[row][col] = s.charAt(col);
			}

			int t=0; //initial state

			if (bShowForest) {
				System.out.println("t="+t);
				printForest(forest);
			}

			for (t=1; t <= minutes; t++) {
				//make a copy of the forest
				char[][] f1 = new char[al.size()][cols];
				for (int r1=0; r1 < forest.length; r1++) {
					for (int c1=0; c1 < forest[r1].length; c1++) {
						f1[r1][c1] = forest[r1][c1];
					}
				}

				//transform each acre
				for (int r1=0; r1 < forest.length; r1++) {
					for (int c1=0; c1 < forest[r1].length; c1++) {
						switch(forest[r1][c1]) {
						case OPEN:
							//An open acre will become filled with trees 
							//if three or more adjacent acres contained trees. Otherwise, nothing happens.
							if (countNeighbors(r1,c1,TREES,f1) >= 3)
								forest[r1][c1] = TREES;
							break;
						case TREES:
							//An acre filled with trees will become a lumberyard if three or more adjacent 
							//acres were lumberyards. Otherwise, nothing happens.
							if (countNeighbors(r1,c1,LUMBER,f1) >= 3)
								forest[r1][c1] = LUMBER;
							break;
						case LUMBER:
							//An acre containing a lumberyard will remain a lumberyard if it was adjacent to at 
							//least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
							if (countNeighbors(r1,c1,LUMBER,f1) >= 1 && countNeighbors(r1,c1,TREES,f1) >= 1)
								forest[r1][c1] = LUMBER;
							else
								forest[r1][c1] = OPEN;
							break;
						default:
							break;
						}
					}
				}

				try {
					Thread.sleep(DELAY_MS);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}

				if (bShowForest) {
					System.out.println("t="+t);
					printForest(forest);
				}




				int num_open = 0;
				int num_trees = 0;
				int num_lumber = 0;
				for (int r1=0; r1 < forest.length; r1++) {
					for (int c1=0; c1 < forest[r1].length; c1++) {
						if (forest[r1][c1] == OPEN)
							num_open++;
						else if (forest[r1][c1] == TREES)
							num_trees++;
						else if (forest[r1][c1] == LUMBER)
							num_lumber++;
					}
				}
				String combo = num_trees+"|"+num_lumber;
				if (!hmSeen.contains(combo)) {
					hmSeen.add(combo);
				} else {
					if (t > 10000 && t % 7 == 0)
						System.out.println("t=" + t + "    combo: " + combo);
				}
			}

			int num_open = 0;
			int num_trees = 0;
			int num_lumber = 0;
			for (int r1=0; r1 < forest.length; r1++) {
				for (int c1=0; c1 < forest[r1].length; c1++) {
					if (forest[r1][c1] == OPEN)
						num_open++;
					else if (forest[r1][c1] == TREES)
						num_trees++;
					else if (forest[r1][c1] == LUMBER)
						num_lumber++;
				}
			}
			System.out.println("open: " + num_open);
			System.out.println("trees: " + num_trees);
			System.out.println("lumber: " + num_lumber);
			System.out.println("TOTAL: " + (num_open+num_trees+num_lumber));
			System.out.println();
			System.out.println("Total Resource Value: " + (num_lumber*num_trees));


		} catch (IOException e) {
			e.printStackTrace();
		}

		long endms = System.currentTimeMillis();
		long elapsedms = endms - startms;
		System.out.println("It took " + (elapsedms / 1000.0) + " seconds.");
	}

	public static void printForest(char[][] f) {
		if (f == null) return;
		for (int r=0; r < f.length; r++) {
			for (int c=0; c < f[r].length; c++)
				System.out.print(f[r][c] + " ");
			System.out.println();
		}
		System.out.println();
	}

	public static int countNeighbors(int row, int col, char c, char[][] f) {
		if (c <= 0 || f == null || row < 0 || col < 0) return 0;
		if (f.length == 0) return 0;
		if (row >= f.length) return 0;
		if (col >= f[0].length) return 0;

		int[] counts = new int[125]; //largest ascii val is TREES: 124
		int tlr = row-1;
		int tlc = col-1;
		int tr = row-1;
		int tc = col;
		int trr = row-1;
		int trc = col+1;
		int lr = row;
		int lc = col-1;
		int rr = row;
		int rc = col+1;
		int blr = row+1;
		int blc = col-1;
		int br = row+1;
		int bc = col;
		int brr = row+1;
		int brc = col+1;

		if (v(tlr,tlc,f))
			counts[(int)f[tlr][tlc]] = counts[(int)f[tlr][tlc]] + 1;
		if (v(tr,tc,f))
			counts[(int)f[tr][tc]] = counts[(int)f[tr][tc]] + 1;
		if (v(trr,trc,f))
			counts[(int)f[trr][trc]] = counts[(int)f[trr][trc]] + 1;
		if (v(lr,lc,f))
			counts[(int)f[lr][lc]] = counts[(int)f[lr][lc]] + 1;
		if (v(rr,rc,f))
			counts[(int)f[rr][rc]] = counts[(int)f[rr][rc]] + 1;
		if (v(blr,blc,f))
			counts[(int)f[blr][blc]] = counts[(int)f[blr][blc]] + 1;
		if (v(br,bc,f))
			counts[(int)f[br][bc]] = counts[(int)f[br][bc]] + 1;
		if (v(brr,brc,f))
			counts[(int)f[brr][brc]] = counts[(int)f[brr][brc]] + 1;

		return counts[(int)c];
	}

	public static boolean v(int r, int c, char[][] f) {
		if (f == null || f.length == 0)
			return false;
		if (r < 0 || c < 0 || r >= f.length || c >= f[0].length)
			return false;
		return true;
	}

}
