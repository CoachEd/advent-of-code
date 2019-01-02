package twenty;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import utils.Dijkstra;
import utils.Edge1;
import utils.Vertex;

public class part0_2 {

	/*
#############
#.|.|.|.|.|.#
#-#####-###-#
#.#.|.#.#.#.#
#-#-###-#-#-#
#.#.#.|.#.|.#
#-#-#-#####-#
#.#.#.#X|.#.#
#-#-#-###-#-#
#.|.#.|.#.#.#
###-#-###-#-#
#.|.#.|.|.#.#
#############
	 */

	public static int width = 13;
	public static int height = 13;
	public static int startx = 7;
	public static int starty = 7;
	public static String smap = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$";
	public static char[][] themap = new char[height][width];
	public static char UNKNOWN = '?';
	public static char ROOM = '.';
	public static char WALL = '#';
	public static char HDOOR = '|';
	public static char VDOOR = '-';
	public static int currx, curry;

	public static void main(String[] args) {
		smap = smap.substring(1,smap.length()-1);
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				themap[row][col] = '?';
			}
		}

		themap[starty][startx] = ROOM;
		printRoom();

		currx = startx;
		curry = starty;
		Stack<Coord> stack = new Stack<Coord>();
		Stack<Integer> poss = new Stack<Integer>();
		poss.push(0);
		stack.push(new Coord(currx,curry));
		int pos = 0;

		while (stack.size() > 0 && pos < smap.length() ) {
			Coord curr = stack.peek();
			char c = smap.charAt(pos);
			switch(c) {
			case 'N':case'S':case'E':case'W':
				stack.pop();
				curr = move(c,curr.x,curr.y);
				stack.push(curr);
				printRoom();
				break;
			case '|':
				stack.pop();
				break;
			case '(':
				stack.push(curr);
				break;
			case ')':
				break;
			}
			pos++;
		} 

		printRoom();
		findFurthest();

	}

	public static Coord move(char c,int currx, int curry) {
		switch(c) {
		case 'N':
			curry--;
			themap[curry][currx] = VDOOR;
			themap[curry][currx-1] = WALL;
			themap[curry][currx+1] = WALL;
			curry--;
			themap[curry][currx] = ROOM;
			themap[curry-1][currx-1] = WALL;
			themap[curry-1][currx+1] = WALL;				
			break;
		case 'S':
			curry++;
			themap[curry][currx] = VDOOR;
			themap[curry][currx-1] = WALL;
			themap[curry][currx+1] = WALL;
			curry++;
			themap[curry][currx] = ROOM;
			themap[curry+1][currx-1] = WALL;
			themap[curry+1][currx+1] = WALL;	
			break;
		case 'E':
			currx++;
			themap[curry][currx] = HDOOR;
			themap[curry-1][currx] = WALL;
			themap[curry+1][currx] = WALL;
			currx++;
			themap[curry][currx] = ROOM;
			themap[curry-1][currx+1] = WALL;
			themap[curry+1][currx+1] = WALL;
			break;
		case 'W':
			currx--;
			themap[curry][currx] = HDOOR;
			themap[curry-1][currx] = WALL;
			themap[curry+1][currx] = WALL;
			currx--;
			themap[curry][currx] = ROOM;
			themap[curry-1][currx-1] = WALL;
			themap[curry+1][currx-1] = WALL;	
			break;
		default:
			System.out.println("SHOULD NOT HAPPEN: " + c);
			break;
		}
		return new Coord(currx,curry);
	}


	public static void printRoom() {
		String s = "";
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				if (themap[row][col] == UNKNOWN)
					themap[row][col] = WALL;
				if (row==starty && col==startx) {
					s += 'X';
				} else
					s += themap[row][col];
			}
			s+="\n";
		}
		System.out.println(s);
	}

	public static void findFurthest() {
		System.out.println("Building graph...");
		//create the graph
		HashMap<String,Vertex> vertices = new HashMap<String,Vertex>();
		String sid;
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				sid = col + "|" + row;
				if (themap[row][col] == ROOM) {
					if (!vertices.containsKey(sid)) {
						vertices.put(sid, new Vertex(sid));
					}
				}
			}
		}

		//for each node, add its edges
		HashMap<String,Edge1> edges = new HashMap<String,Edge1>();
		String toid = "";
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				if (themap[row][col] != ROOM) continue;
				sid = col + "|" + row;

				Vertex v = vertices.get(sid);
				Vertex v2;
				String edgeid = "";
				Edge1 edge;
				//up node?
				if (themap[row-1][col] == VDOOR) {
					toid = col + "|" + (row-2);
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

				//down node?
				if (themap[row+1][col] == VDOOR) {
					toid = col + "|" + (row+2);
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

				//right node?
				if (themap[row][col+1] == HDOOR) {
					toid = (col+2) + "|" + row;
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

				//left node?
				if (themap[row][col-1] == HDOOR) {
					toid = (col-2) + "|" + row;
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

			}
		}

		System.out.println("Calculating shortest path through most doors...");
		sid = startx +"|" + starty;
		Vertex vstart = vertices.get(sid); //start vertex
		Dijkstra.computePaths(vstart); // run Dijkstra

		int largest_path = Integer.MIN_VALUE;
		Vertex largest_room = null;
		for (Map.Entry<String, Vertex> entry : vertices.entrySet()) {
			Vertex v = entry.getValue();
			List<Vertex> path = Dijkstra.getShortestPathTo(v); //no path is list of size 1 (itself)
			//System.out.println("Path from,to  " + vstart.name + "," + v.name +"  " + path + "   path.size(): " + path.size());
			if (path.size() > largest_path) {
				largest_path = path.size();
				largest_room = v;
			}
			System.out.println("path.size(): " + path.size());
		}
		System.out.println("\nLargest number of doors required to pass through to reach a room?: " + (largest_path-1) + " doors  to reach " + " to reach " + largest_room.name);
	}

}

