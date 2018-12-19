package seventeen;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class seventeen_1 {

	//static String fname = "files/17_1.txt";
	static String fname = "files/17_0.txt";
	static final char SAND = '.';
	static final char CLAY = '#';
	static final char SPRING = '+';
	static final char WATERS = '~'; //water settled
	static final char WATERM = '|'; //water movement
	static int SPRING_X = 500;
	static int SPRING_Y = 0;
	static int MAX_ROWS = 0;
	static int MAX_COLS = 0;
	static int CURRX = 0;
	static int CURRY = 0;
	static int DELAY_MS = 500;
	static int ystart = 0;
	static int xstart = 0;
	static int yend = 0; //bottom-right corner of ground (same as above)
	static int xend = 0;
	static char[][] ground;

	public static void main(String[] args) {

		//read the input file
		BufferedReader br = null;
		String line = "";
		ArrayList< ArrayList<Coord> > veins = new ArrayList< ArrayList<Coord>>();
		int maxX = -1;
		int maxY = -1;
		int minX = Integer.MAX_VALUE;
		int minY = Integer.MAX_VALUE;
		try {
			br = new BufferedReader(new FileReader(fname));
			while ((line = br.readLine()) != null) {
				ArrayList<Coord> vein = new ArrayList<Coord>();
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
					if (n3 > maxY)
						maxY = n3;
					if (n1 < minX)
						minX = n1;
					if (n3 < minY)
						minY = n3;
					for (int i=n2; i <= n3; i++) {
						vein.add(new Coord(n1,i)); //x,y
						//System.out.println("x: added " + n1+","+i);
					}
				} else {
					//first coord is y
					if (n1 > maxY)
						maxY = n1;
					if (n3 > maxX)
						maxX = n3;
					if (n1 < minY)
						minY = n1;
					if (n3 < minX)
						minX = n3;
					for (int i=n2; i <= n3; i++) {
						vein.add(new Coord(i,n1)); //x,y
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

		//TEST SPECIFIC
		//top-left part of map to show
		ystart = 0;
		xstart = minX-1;

		yend = maxY; //bottom-right corner of ground (same as above)
		xend = maxX+1;

		MAX_ROWS = yend+1;
		MAX_COLS = xend+1;

		//create ground and initialize to all sand
		ground = new char[MAX_ROWS][MAX_COLS];
		for (int y=0; y < ground.length; y++) {
			for (int x=0; x < ground[y].length; x++) {
				ground[y][x] = SAND;
			}
		}

		//add the veins
		for (ArrayList<Coord> al : veins) {
			for (Coord c : al) {
				//System.out.println("adding " + c.y + ","+ c.x);
				ground[c.y][c.x] = CLAY; 
			}
		}

		//add the spring
		ground[0][500] = SPRING;


		printGround(ystart,yend,xstart,xend);

		CURRX = SPRING_X;
		CURRY = SPRING_Y;
		boolean water_settled = false;
		while (true) {
			if (CURRY > maxY) {
				//water is past the lowest y, this drop is done
				continue;
			}

			//go down as far as you can
			boolean moved = true;
			while (moved) {
				int dx = CURRX;
				int dy = CURRY+1;
				moved = water(dx,dy); 
			}


			//left,right,up?	


			//set next currx, curry


			if (!water_settled) {
				//we are done
				break;
			}
		} //end WHILE

	}

	public static boolean water(int newx, int newy) {
		if (newx >=0 && newx < MAX_COLS && newy >=0 && newy <= MAX_ROWS) {

			try {
				Thread.sleep(DELAY_MS);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			//valid
			if (ground[newy][newx] == SAND) {
				if (ground[CURRY][CURRX] != SPRING)
					ground[CURRY][CURRX] = SAND;
				ground[newy][newx] = WATERM;
				CURRX = newx;
				CURRY = newy;
				printGround(ystart,yend,xstart,xend);
				return true;
			}
		} else {
			//invalid
			System.out.println("ERROR: invalid coords");
		}
		return false;
	}

	public static void printGround(int ystart, int yend, int xstart, int xend) { 
		String s = "";
		for (int y=ystart; y <= yend; y++) {
			for (int x=xstart; x <= xend; x++) {
				//System.out.println("x,y " + x+","+y);
				s = s + ground[y][x];
			}
			s += '\n';
		}
		System.out.println(s);
	}

}
