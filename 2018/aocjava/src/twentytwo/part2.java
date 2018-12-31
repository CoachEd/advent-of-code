package twentytwo;

import java.util.HashMap;
import java.util.List;
import java.util.Random;

public class part2 {
	static int mouthx = 0;
	static int mouthy = 0;

	//final data
	static int targetx = 13;  //input
	static int targety = 743; //input
	static int depth = 8112;  //input
	//static int targetx = 10;  //input
	//static int targety = 10; //input
	//static int depth = 510;  //input


	static int width = targetx+13;
	static int height = targety+743;
	//static int width = targetx+1;
	//static int height = targety+1;	
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
		Vertex cnode;
		for (int y=0; y < cave.length; y++) {
			for (int x=0; x < cave[y].length; x++) {
				String sNode = y+"|"+x; //e.g., 0|0
				if (!vertices.containsKey(sNode)) {
					cnode = new Vertex(sNode,rtype[y][x],y,x);
					vertices.put(sNode,cnode);
				} else
					cnode = vertices.get(sNode);
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
				RTYPE nexttype; //type of next region
				Edge1 edge;
				Vertex tonode;
				int ty = upy;
				int tx = upx;
				if (validc(tx,ty)) {
					nexttype = rtype[ty][tx];
					sNode = ty+"|"+tx;
					if (!vertices.containsKey(sNode)) {
						tonode = new Vertex(sNode,nexttype,ty,tx);
						vertices.put(sNode,tonode);
					} else
						tonode = vertices.get(sNode);
					edge = new Edge1(tonode, 1);
					edges.put(cnode.name +"|" + tonode.name,edge);
					cnode.adjacencies.add(edge);
				}
				ty = downy;
				tx = downx;
				if (validc(tx,ty)) {
					nexttype = rtype[ty][tx];
					sNode = ty+"|"+tx;
					if (!vertices.containsKey(sNode)) {
						tonode = new Vertex(sNode,nexttype,ty,tx);
						vertices.put(sNode,tonode);
					} else
						tonode = vertices.get(sNode);
					edge = new Edge1(tonode, 1);
					edges.put(cnode.name +"|" + tonode.name,edge);
					cnode.adjacencies.add(edge);
				}
				ty = righty;
				tx = rightx;
				if (validc(tx,ty)) {
					nexttype = rtype[ty][tx];
					sNode = ty+"|"+tx;
					if (!vertices.containsKey(sNode)) {
						tonode = new Vertex(sNode,nexttype,ty,tx);
						vertices.put(sNode,tonode);
					} else
						tonode = vertices.get(sNode);
					edge = new Edge1(tonode, 1);
					edges.put(cnode.name +"|" + tonode.name,edge);
					cnode.adjacencies.add(edge);
				}
				ty = lefty;
				tx = leftx;
				if (validc(tx,ty)) {
					nexttype = rtype[ty][tx];
					sNode = ty+"|"+tx;
					if (!vertices.containsKey(sNode)) {
						tonode = new Vertex(sNode,nexttype,ty,tx);
						vertices.put(sNode,tonode);
					} else
						tonode = vertices.get(sNode);
					edge = new Edge1(tonode, 1);
					edges.put(cnode.name +"|" + tonode.name,edge);
					cnode.adjacencies.add(edge);
				}
			}
		}

		int smallest = Integer.MAX_VALUE;
		int mins = 0;
		//INCORRECT: 
		//lowest: 936 (too low)
		//
		int count = 0;
		for (int n=0; n < 100000; n++) {
			Random rand = new Random(System.currentTimeMillis());
			if (count == 10000) {
				System.out.println(n+"...");
				count = 0;
			}
			count++;
			Vertex mouth = vertices.get(mouthy+"|"+mouthx);
			Vertex target = vertices.get(targety+"|"+targetx);
			Dijkstra.computePaths(mouth,rand); // run Dijkstra
			List<Vertex> path = Dijkstra.getShortestPathTo(target); //no path is list of size 1 (itself)
			//System.out.println("Path: " + path + "   path.size(): " + path.size());
			mins = 0;
			for (int i=0; i < path.size()-1; i++) {
				Vertex fromv = path.get(i);
				Vertex tov = path.get(i+1);
				Edge1 e = edges.get(fromv.name+"|"+tov.name);
				mins += e.weight;
			}

			/*
			 * once you reach the target, you need the torch equipped before you can find him in the dark. 
			 * The target is always in a rocky region, so if you arrive there with climbing gear equipped, 
			 * you will need to spend seven minutes switching to your torch.
			 */
			Vertex t1 = path.get(path.size()-2);
			Vertex t2 = path.get(path.size()-1);
			Edge1 e1 = edges.get(t1.name + "|" + t2.name);
			if (e1.equipped != TOOLS.torch)
				mins += 7;

			if (mins < smallest) {
				smallest = mins;
			}
		}
		System.out.println();
		System.out.println(mins);
	}

	public static boolean validc(int x, int y) {
		if (x < 0 || y < 0 || x >= width || y >= height)
			return false;
		return true;
	}

}
