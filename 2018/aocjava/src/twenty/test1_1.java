package twenty;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import utils.Dijkstra;
import utils.Edge1;
import utils.Vertex;
//LEFT OFF HERE - IF '|' multiply them out with REST
/*
|) YES
|| NO
|( NO

)) YES
)( YES
)| YES

(( NO
(| NO
() NO


( always followed by NSEW
 */
public class test1_1 {

	public static int width = 13;
	public static int height = 13;
	public static int startx = 7;
	public static int starty = 7;
	public static String smap = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$";
	/*
	public static int width = 13;
	public static int height = 29;
	public static int startx = 1;
	public static int starty = 27;
	public static String smap = "^NNNNN(EEEEE|NNN)NNNNN$";
	*/

	public static char[][] themap = new char[height][width];
	public static char UNKNOWN = '?';
	public static char ROOM = '.';
	public static char WALL = '#';
	public static char HDOOR = '|';
	public static char VDOOR = '-';
	public static int currx, curry;
	static String outfname = "files/rooms.txt";
	static BufferedWriter bw;

	public static ArrayList<Coord> parseIt(String s, Coord curr) {
		ArrayList<Coord> ret = new ArrayList<Coord>();
		if (s == null || s.length() == 0) return ret;

		String next = null;
		Coord temp = new Coord(curr.x,curr.y);
		char c = s.charAt(0);
		switch(c) {
		case 'N':case 'S':case 'E':case 'W':
			
			
			
			//check for top-level pipe (NEW)
			int pos2 = 0;
			int paren_count = 0;
			boolean found_toplevel_pipe = false;
			while (true) {
				if (s.charAt(pos2) == ')')
					paren_count--;
				else if (s.charAt(pos2) == '(')
					paren_count++;
				
				if (paren_count == 0 && s.charAt(pos2) == '|') {
					found_toplevel_pipe = true;
					break;
				}
				pos2++;
				if (pos2 >= s.length())
					break;
			}
			if (found_toplevel_pipe) {
				ArrayList<Coord> al3 = new ArrayList<Coord>();
				al3.addAll(parseIt(s.substring(0,pos2),curr));
				al3.addAll(parseIt(s.substring(pos2+1),curr));
				return al3;
			}
			
			
			
			
			String[] parts = s.split("\\(|\\)|\\|");
			System.out.println(temp.x+","+temp.y+ "  " + parts[0]); //TEST
			for (int i=0; i < parts[0].length(); i++) {
				char c2 = s.charAt(i);
				temp = move(c2,temp.x,temp.y);
			}
			printRoom();
			next = s.substring(parts[0].length());
			if (next.length() == 0) {
				ret.add(temp);
				return ret;
			} else {
				if (next.charAt(0) == '|') {
					ret.add(temp);
					ret.addAll(parseIt(next,curr));
					return ret;
				} else
					return parseIt(next,temp);
			}
		case '|':
			next = s.substring(1);
			return parseIt(next,curr);			
		case '(':
			//find the group, parse it, parse the rest (NEED WORK BELOW)
			int pos=0;
			int num_skips = 1;
			while (s.charAt(pos) != ')' || num_skips > 0) {
				pos++;
				if (s.charAt(pos) == '(')
					num_skips++;
				else if (s.charAt(pos) == ')')
					num_skips--;
			}
			String group = s.substring(1,pos);
			String rest = s.substring(pos+1);
			ArrayList<Coord> al = new ArrayList<Coord>();
			if (group.endsWith("|")) {
				//empty group case
				al.add(new Coord(curr.x,curr.y));
				group = group.substring(0,group.length()-1);
			}
			if (rest != null && rest.length() > 0) {
				char next_char = rest.charAt(0);
				al.addAll(parseIt(group,curr));
				if (next_char == '|') {
					al.addAll(parseIt(rest,curr));
					return al;
				}
				ArrayList<Coord> al2 =  new ArrayList<Coord>();
				for (Coord c3 : al) {
					al2.addAll( parseIt(rest,c3) );
				}
				return al2;
			} else {
				return parseIt(group,curr);
			}
		case ')':
			//NEEDED?
			break;
		default:
			break;
		}
		printRoom();


		return ret;
	}



	public static void main(String[] args) {

		smap = smap.substring(1,smap.length()-1);
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				themap[row][col] = '?';
			}
		}
		themap[starty][startx] = ROOM;

		//TESTING
		/*
		smap = "NNNNN"; 
		smap = "NNNNN|EE"; 
		smap = "NNNNN(EE)"; 
		smap = "NNEE(NN|SS)"; 
		smap = "NNEE(NN|SS)E";
		smap = "NNEE(NN|SS)(E|W)"; 
		smap = "NNEE(NN|SS(EE))"; 
		smap = "NNEE(NN|SS|)E"; 
		smap = "NNEE(E|N(E(WN|)S|E(N|E)))";
		*/
		//smap = "N(E(S|)N|W(S|E))"; //not working
		//smap = "E(S|)N|W(S|E)"; //not working
		//smap = "E(S|N)N|W(S|W)"; //not working (CASE: need to break this on '|' in two parts!!

		printRoom();
		parseIt(smap,new Coord(startx,starty));

		printRoom();
		findFurthest();
		writeRoomsToFile();
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

