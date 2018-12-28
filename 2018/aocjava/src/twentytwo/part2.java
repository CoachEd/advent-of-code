package twentytwo;

import java.util.HashMap;

import utils.Edge1;
import utils.Vertex;

public class part2 {
	static int mouthx = 0;
	static int mouthy = 0;
	static int targetx = 13;  //input
	static int targety = 743; //input
	static int depth = 8112;  //input
	static int width = targetx+1;
	static int height = targety+1;	
	static char[][] cave;
	static int[][] geologic;
	static int[][] erosion;
	static RTYPE[][] rtype;
	static enum RTYPE { rocky , wet, narrow };
	static enum TOOLS { torch, climbing, neither };

	public static void main(String[] args) {
		int risk_level = 0;
		cave = new char[height][width];
		geologic = new int[height][width];
		erosion = new int[height][width];
		rtype = new RTYPE[height][width];
		for (int y=0; y < cave.length; y++) {
			for (int x=0; x < cave[y].length; x++) {
				if ( (x==mouthx && y==mouthy) || (x==targetx && y==targety)) {
					geologic[y][x] = 0;
					erosion[y][x] = (geologic[y][x] + depth) % 20183;
				} else if (y==0) {
					geologic[y][x] = x * 16807;
					erosion[y][x] = (geologic[y][x] + depth) % 20183;
				} else if (x==0) {
					geologic[y][x] = y * 48271;
					erosion[y][x] = (geologic[y][x] + depth) % 20183;
				} else {
					geologic[y][x] = erosion[y][x-1] * erosion[y-1][x];
					erosion[y][x] = (geologic[y][x] + depth) % 20183;
				}
				if (y==targety && x == targetx)
					System.out.println("");
				int result = erosion[y][x] % 3;
				risk_level += result;
				switch (result) {
				case 0:
					rtype[y][x] = RTYPE.rocky;
					cave[y][x] = '.';
					break;
				case 1:
					rtype[y][x] = RTYPE.wet;
					cave[y][x] = '=';
					break;
				case 2:
					rtype[y][x] = RTYPE.narrow;
					cave[y][x] = '|';
					break;
				default:
					System.err.println("ERROR. Should not happen");
				}
			}
		}

		String s = "";
		for (int y=0; y < cave.length; y++) {
			for (int x=0; x < cave[y].length; x++) {
				s += cave[y][x];
			}
			s += "\n";
		}
		System.out.println(s);
		System.out.println("risk_level: " + risk_level);

		//create the graph
		HashMap<String,Vertex> vertices = new HashMap<String,Vertex>();
		HashMap<String,Edge1> edges = new HashMap<String,Edge1>();
		TOOLS equipped;
		for (int y=0; y < cave.length; y++) {
			for (int x=0; x < cave[y].length; x++) {
				String sNode = y+"|"+x; //e.g., 0|0
				vertices.put(sNode,new Vertex(sNode));
				int upx = x;
				int upy = y-1;
				int downx = x;
				int downy = y+1;
				int rightx = x+1;
				int righty = y;
				int leftx = x-1;
				int lefty = y;
/*
In rocky regions, you can use the climbing gear or the torch. 
You cannot use neither (you'll likely slip and fall).

In wet regions, you can use the climbing gear or neither tool. 
You cannot use the torch (if it gets wet, you won't have a light source).

In narrow regions, you can use the torch or neither tool. 
You cannot use the climbing gear (it's too bulky to fit).
 */
				RTYPE curtype = rtype[y][x]; //type of current region
				equipped = TOOLS.torch;
				if (validc(upx,upy)) {

				}
				if (validc(downx,downy)) {

				} 
				if (validc(rightx,righty)) {

				}
				if (validc(leftx,lefty)) {

				}



			}
		}

	}

	public static boolean validc(int x, int y) {
		if (x < 0 || y < 0 || x >= width || y >= height)
			return false;
		return true;
	}

}
