package twenty;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import utils.Dijkstra;
import utils.Edge1;
import utils.Vertex;
/*
GOOD map (my output is missing the right fork):
#############
#.###########
#-###########
#.###########
#-###########
#.###########
#-###########
#.#########.#
#-#########-#
#.#########.#
#-#########-#
#.#########.#
#-#########-#
#.#########.#
#-#########-#
#.#########.#
#-#########-#
#.|.|.|.|.|.#
#-###########
#.###########
#-###########
#.###########
#-###########
#.###########
#-###########
#.###########
#-###########
#X###########
#############

This should be 15, your code returns 13. 
Oddly, this must be a corner-case because my input does not 
run into this problem.
 */
public class test3 {
	public static int width = 13;
	public static int height = 29;
	public static int startx = 1;
	public static int starty = 27;
	public static char[][] themap = new char[height][width];
	public static char UNKNOWN = '?';
	public static char ROOM = '.';
	public static char WALL = '#';
	public static char HDOOR = '|';
	public static char VDOOR = '-';
	public static int currx, curry;
	static String outfname = "files/rooms.txt";
	static BufferedWriter bw;

	public static String smap = "^NNNNN(EEEEE|NNN)NNNNN$";
	
	public static void parseIt(String s, int x, int y) {
		if (s == null || s.length() == 0) return;
		char c = s.charAt(0);
		Coord curr = new Coord(x,y);
		switch(c) {
		case 'N':case 'S':case 'E':case 'W':
			String[] parts = smap.split("\\(|\\)|\\|");
			for (char c1 : parts[0].toCharArray()) {
				curr = move(c1,curr.x,curr.y);
			}
			printRoom();

			break;
		case '(':

			break;
		case '|':
			break;
		case ')':
			break;
		default:
			break;
		}
		

		return;
	}
	
	public static void main(String[] args) {
		smap = smap.substring(1,smap.length()-1);
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				themap[row][col] = '?';
			}
		}
		themap[starty][startx] = ROOM;

		/* test*/
		parseIt(smap,startx,starty);
		//printRoom();
		//findFurthest();
		//writeRoomsToFile();
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
		int maxrow = Integer.MIN_VALUE;
		int maxcol = Integer.MIN_VALUE;
		String toid = "";
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				if (themap[row][col] != ROOM) continue;
				sid = col + "|" + row;

				if (row > maxrow) maxrow = row;
				if (col > maxcol) maxcol = col;

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
			//System.out.println("path.size(): " + path.size());
		}
		System.out.println("maxrow: " + maxrow + "   maxcol: " + maxcol);
		System.out.println("\nLargest number of doors required to pass through to reach a room?: " + (largest_path-1) + " doors  to reach " + " to reach " + largest_room.name);
	}

	public static void writeRoomsToFile() {
		File fout = new File(outfname);
		FileOutputStream fos;

		try {
			fos = new FileOutputStream(fout);
			bw = new BufferedWriter(new OutputStreamWriter(fos));
			for (int row=0; row < themap.length; row++) {
				for (int col=0; col < themap[row].length; col++) {
					if (themap[row][col] == UNKNOWN)
						themap[row][col] = WALL;
					if (row==starty && col==startx) {
						bw.write('X');
					} else
						bw.write(themap[row][col]);
				}
				bw.newLine();
			}			
			bw.close();
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}

