package seventeen;

//WRONG: 468 (too low), 653 (too low), 27752 (too high), 27742(wrong), 27732 (wrong), 27720, 27744
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class seventeen_1a {

	static String fname = "files/17_1.txt";
	//static String fname = "files/17_0.txt";
	static final char SAND = '.';
	static final char CLAY = '#';
	static final char SPRING = '+';
	static final char WATERS = '~'; //water settled
	static final char WATERF = '|'; //water flowing
	static int SPRING_X = 500;
	static int SPRING_Y = 0;
	static int MAX_ROWS = 0;
	static int MAX_COLS = 0;
	static int CURRX = 0;
	static int CURRY = 0;
	static int DELAY_MS = 0;
	static int ystart = 0;
	static int xstart = 0;
	static int yend = 0; //bottom-right corner of ground (same as above)
	static int xend = 0;
	static int maxX = -1;
	static int maxY = -1;
	static int minX = Integer.MAX_VALUE;
	static int minY = Integer.MAX_VALUE;
	static char[][] ground;
	static ArrayList<Ground> groundelems = new ArrayList<Ground>();
	static ArrayList<Ground> newelems = new ArrayList<Ground>();
	static String outfname = "files/waterout.txt";
	static BufferedWriter bw;
	static int count2 = 0; //audit for water

	public static void main(String[] args) {

		//read the input file
		BufferedReader br = null;
		String line = "";
		ArrayList< ArrayList<Ground> > veins = new ArrayList< ArrayList<Ground>>();
		try {
			br = new BufferedReader(new FileReader(fname));
			while ((line = br.readLine()) != null) {
				ArrayList<Ground> vein = new ArrayList<Ground>();
				String[] arr = line.split("\\s+");
				String s1 = arr[0];
				String s2 = arr[1];
				if (s2.indexOf("..") == -1) {
					System.out.println("ERROR: part 2 of coordinate is missing '..'");
					System.exit(-1);
				}
				int cindex = s1.indexOf(',');
				int eindex = s2.indexOf("..");
				int n1 = Integer.parseInt(s1.substring(2,cindex));
				int n2 = Integer.parseInt(s2.substring(2,eindex));
				int n3 = Integer.parseInt(s2.substring(eindex+2));

				//System.out.println(n1 + "    " + n2 + " " + n3);
				if (s1.startsWith("x=")) {
					//first coord is x
					if (n1 > maxX)
						maxX = n1;
					if (n2 > maxY)
						maxY = n2;
					if (n3 > maxY)
						maxY = n3;
					if (n1 < minX)
						minX = n1;
					if (n2 < minY)
						minY = n2;
					if (n3 < minY)
						minY = n3;
					for (int i=n2; i <= n3; i++) {
						vein.add(new Ground(n1,i,CLAY)); //x,y
						//System.out.println("x: added " + n1+","+i);
					}
				} else {
					//first coord is y
					if (n1 > maxY)
						maxY = n1;
					if (n2 > maxX)
						maxX = n2;
					if (n3 > maxX)
						maxX = n3;
					if (n1 < minY)
						minY = n1;
					if (n2 < minX)
						minX = n2;
					if (n3 < minX)
						minX = n3;
					for (int i=n2; i <= n3; i++) {
						vein.add(new Ground(i,n1,CLAY)); //x,y
						//System.out.println("y: added " +i+","+n1);
					}
				}
				veins.add(vein);
			}
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		System.out.println("maxX: " +  maxX + "   maxY: " + maxY);
		System.out.println("minX: " +  minX + "   minY: " + minY);

		//displayable part of the map; must be within MAX_ROWS , MAX_COLS
		ystart = 0; //top-left part of map to show
		xstart = minX-1;
		yend = maxY+2; //bottom-right corner of ground (same as above)
		xend = maxX+1;	

		//size of ground
		MAX_ROWS = yend+1000;
		MAX_COLS = xend+1000;

		//create ground and initialize to all sand
		ground = new char[MAX_ROWS][MAX_COLS];
		for (int y=0; y < ground.length; y++) {
			for (int x=0; x < ground[y].length; x++) {
				ground[y][x] = SAND;
			}
		}

		//add the veins
		for (ArrayList<Ground> al : veins) {
			for (Ground g : al) {
				ground[g.y][g.x] = CLAY; 
			}
		}

		//add the spring
		int y = SPRING_Y;
		int x = SPRING_X;
		ground[y][x] = SPRING;
		groundelems.add(new Ground(x,y,SPRING));


		CURRX = SPRING_X;
		CURRY = SPRING_Y;
		boolean done = false;
		int iter = 0;
		while (!done) {
			newelems = new ArrayList<Ground>(); //any added ground elements during this iteration
			//printGround(ystart,yend,xstart,xend);

			try {
				Thread.sleep(DELAY_MS);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			//process all items in groundelems
			for (Ground g : groundelems) {
				switch(g.c) {
				case SPRING: //spring source
					if (down(g) == SAND) {
						addDown(g,WATERF);
					}
					break;
				case WATERF: //flowing water '|'
					if (down(g) == SAND) {
						addDown(g,WATERF);
					} else if (down(g) == CLAY) {
						if (left(g) == SAND)
							addLeft(g,WATERF);
						if (right(g) == SAND)
							addRight(g,WATERF);
						if (isBordered(g)) {
							g.c = WATERS;
							ground[g.y][g.x]= WATERS; 
						}						
					} else if (down(g) == WATERS) {
						if (right(g) == SAND)
							addRight(g,WATERF);
						if (left(g) == SAND)
							addLeft(g,WATERF);
						if (down(g) == WATERS && isBordered(g)) {
							g.c = WATERS;
							ground[g.y][g.x]= WATERS; 
						}

						if (left(g) == CLAY && right(g) == CLAY) {
							g.c = WATERS;
							ground[g.y][g.x]= WATERS; 
						}

					}

					if (right(g) == WATERS || left(g) == WATERS) {
						g.c = WATERS;
						ground[g.y][g.x]= WATERS;
					}

					break;
					/*
				case WATERS: //standing water '~'
					if (right(g) == WATERF) {
						ground[g.y][g.x+1] = WATERS;
					}
					if (left(g) == WATERF) {
						ground[g.y][g.x-1] = WATERS;
					}
					if (right(g) == SAND)
						addRight(g,WATERS);
					if (left(g) == SAND)
						addLeft(g,WATERS);
					break;
					 */
				default:
					break;
				}



			}

			//TODO: add newelems to groundelems
			groundelems.addAll(newelems);
			iter++;

			//arbitrary end condition
			if (iter > 9093)
				done = true;

		} //end WHILE

		System.out.println("maxX: " +  maxX + "   maxY: " + maxY);
		System.out.println("minX: " +  minX + "   minY: " + minY);
		
		int count = 0;
		int minx = Integer.MAX_VALUE;
		int maxx = -1;
		int miny = Integer.MAX_VALUE;
		int maxy = -1;
		for (int r=0; r < ground.length; r++) {
			for (int c=0; c < ground[r].length; c++) {
				if (ground[r][c] == WATERF || ground[r][c] == WATERS) {
					
					//To prevent counting forever, ignore tiles with a y coordinate smaller than 
					//the smallest y coordinate in your scan data or larger than the largest one
					if (r <= maxY && r >= minY)
						count++;

					if (r < miny)
						miny = r;
					if (r > maxy)
						maxy = r;
					if (c < minx)
						minx = c;
					if (c > maxx)
						maxx = c;
				}
			}
		}
		System.out.println("count: " + count);
		System.out.println("Printing...");


		System.out.println((miny-1) + "," + (maxy+1) + "," + (minx-1) + "," + (maxx+1));
		printGroundToFile(miny-1,maxy+1,minx-1,maxx+1);


		//printGround(miny-1+1600,maxy+1,minx-1,maxx+1); //last section
		System.out.println("\niterations: " + iter);
		System.out.println("water: " + minx+","+miny + "     " + maxx+","+maxy);
		System.out.println("tiles: " + count);
		System.out.println("DONE.");
	}

	public static boolean isBordered(Ground g) {
		//is it bordered on left and right sides by clay
		Ground t = new Ground(g); //temp
		while (down(t) != SAND && rightDown(t) != SAND) {
			t.c = ground[g.y][t.x+1];
			t.x = t.x + 1;
			if (ground[t.y][t.x]== CLAY)
				break;
		}
		boolean right_border = t.c == CLAY; 
		t = new Ground(g); //temp
		while (down(t) != SAND && leftDown(t) != SAND) {
			t.c = ground[g.y][t.x-1];
			t.x = t.x - 1;
			if (ground[t.y][t.x]== CLAY)
				break;			
		}
		boolean left_border = t.c == CLAY; 
		return right_border && left_border;
	}

	public static void addDown(Ground g, char c) {
		if (g == null) return;

		//add element c down one space from elem g
		int x = g.x;
		int y = g.y+1;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS) {
			Ground gnew = new Ground(x,y,c);
			ground[y][x] = gnew.c;
			newelems.add(gnew);
			if (y <= maxY) count2++;
		}
	}

	public static void addUp(Ground g, char c) {
		if (g == null) return;
		int x = g.x;
		int y = g.y-1;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS) {
			Ground gnew = new Ground(x,y,c);
			ground[y][x] = gnew.c;
			newelems.add(gnew);
			if (y <= maxY) count2++;
		}
	}

	public static void addRight(Ground g, char c) {
		if (g == null) return;
		int x = g.x+1;
		int y = g.y;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS) {
			Ground gnew = new Ground(x,y,c);
			ground[y][x] = gnew.c;
			newelems.add(gnew);
			if (y <= maxY) count2++;
		}
	}

	public static void addLeft(Ground g, char c) {
		if (g == null) return;
		int x = g.x-1;
		int y = g.y;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS) {
			Ground gnew = new Ground(x,y,c);
			ground[y][x] = gnew.c;
			newelems.add(gnew);
			if (y <= maxY) count2++;
		}
	}

	public static char up(Ground g) {
		char c = '\0';
		if (g == null)
			return c;
		int x = g.x;
		int y = g.y-1;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS)
			return ground[y][x];
		return c;
	}

	public static char down(Ground g) {
		char c = '\0';
		if (g == null)
			return c;
		int x = g.x;
		int y = g.y+1;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS)
			return ground[y][x];
		return c;
	}

	public static char left(Ground g) {
		char c = '\0';
		if (g == null)
			return c;
		int x = g.x-1;
		int y = g.y;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS)
			return ground[y][x];
		return c;
	}

	public static char leftDown(Ground g) {
		char c = '\0';
		if (g == null)
			return c;
		int x = g.x-1;
		int y = g.y+1;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS)
			return ground[y][x];
		return c;
	}

	public static char rightDown(Ground g) {
		char c = '\0';
		if (g == null)
			return c;
		int x = g.x+1;
		int y = g.y+1;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS)
			return ground[y][x];
		return c;
	}

	public static char right(Ground g) {
		char c = '\0';
		if (g == null)
			return c;
		int x = g.x+1;
		int y = g.y;
		if (x >=0 && x < MAX_COLS && y >= 0 && y < MAX_ROWS)
			return ground[y][x];
		return c;
	}

	public static void printGround(int ystart, int yend, int xstart, int xend) { 


		String s = "\n";
		String.format("%s = %d", "joe", 35);
		for (int y=ystart; y <= yend; y++) {
			for (int x=xstart; x <= xend; x++) {
				//System.out.println("x,y " + x+","+y);
				if (y <= maxY)
					s = s + ground[y][x];
				else
					s = s + SAND;
			}
			s += '\n';

		}
		System.out.print(s);

	}
	public static void printGroundToFile(int ystart, int yend, int xstart, int xend) { 


		String s = "\n";
		String.format("%s = %d", "joe", 35);
		for (int y=ystart; y <= yend; y++) {
			for (int x=xstart; x <= xend; x++) {
				//System.out.println("x,y " + x+","+y);
				if (y <= maxY)
					s = s + ground[y][x];
				else
					s = s + SAND;
			}
			s += '\n';

		}
		//System.out.print(s);

		File fout = new File(outfname);
		FileOutputStream fos;
		try {
			fos = new FileOutputStream(fout);
			bw = new BufferedWriter(new OutputStreamWriter(fos));
			bw.write(s);
			bw.newLine();
			bw.close();
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
