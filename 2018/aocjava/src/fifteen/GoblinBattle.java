package fifteen;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

public class GoblinBattle {

	static ArrayList<Player> players = new ArrayList<Player>();
	static ArrayList<Wall> walls = new ArrayList<Wall>();
	static ArrayList<Space> spaces = new ArrayList<Space>();
	static String fname = "C:\\Users\\edwin\\github\\advent-of-code\\2018\\aocjava\\src\\fifteen\\goblin1.txt";
	static int maxrows = 0;
	static int maxcols = 0;
	static char[][] themap;
	static int t = 0;
	static String playerchars = "GE";
	static final char GOBLIN = 'G';
	static final char ELF = 'E';
	static final char WALL = '#';
	static final char SPACE = '.';
	static final int UP = 0;
	static final int DOWN = 1;
	static final int LEFT = 2;
	static final int RIGHT = 3;

	public String tick() {
		String sout = "";

		//output map at the start of the tick (round)
		printMap();

		//sort the players list (order in which to process each player) in reading order
		for (int i=0; i < players.size(); i++) {
			for (int j=i+1; j < players.size(); j++) {
				Player playerj = players.get(j);
				Player playeri = players.get(i);
				if (playerj.row < playeri.row) {
					//swap
					playeri.swap(playerj);
				} else if (playerj.row == playeri.row) {
					if (playerj.col < playeri.col) {
						//swap
						playeri.swap(playerj);
					}
				}
			}
		}

		//now process all players
		for (int i=0; i < players.size(); i++) {

		} //end players for loop

		t++;
		return(sout);
	} //end tick

	public static void printMap() {
		String sout = "";
		for (int row = 0; row < themap.length; row++) {
			for (int col = 0; col < themap[row].length; col++) {
				sout += themap[row][col];
			}
			sout += "\n";
		}
		System.out.println("t="+ t + "\n" + sout);
	}

	public GoblinBattle() {
		ArrayList<String> al = new ArrayList<String>();
		try (BufferedReader br = new BufferedReader(new FileReader(fname))) {
			String line;
			while ((line = br.readLine()) != null) {
				maxrows++;
				maxcols = line.length();
				al.add(line);
			}

			//populate map
			themap = new char[maxrows][maxcols];
			for (int row = 0; row < al.size(); row++) {
				String l = al.get(row);
				for (int col = 0; col < l.length(); col++) {
					themap[row][col] = l.charAt(col);
				}
			}

			//create players, walls, and spaces
			for (int r = 0; r < themap.length; r++) {
				for (int c = 0; c < themap[r].length; c++) {
					if (playerchars.indexOf(themap[r][c] + "") != -1) {
						Player p = new Player(themap[r][c], r,c);
						players.add(p);
					} else if (themap[r][c] == WALL) {
						Wall w = new Wall(r,c);
						walls.add(w);
					} else if (themap[r][c] == SPACE) {
						Space s = new Space(r,c);
						spaces.add(s);
					}
				}
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	} //end constructor

	public static TreeSet<Coord> inRange(char targetchar) {
		TreeSet<Coord> ts = new TreeSet<Coord>();
		//return coordinates of spaces in range of type targetchar
		//loop through players
		for (int i=0; i < players.size(); i++) {
			Player p = players.get(i);
			if (p.c == targetchar) {
				getAdjacent(p,ts); //adds open spaces adjacent to p
			}
		}
		return ts;
	}

	//get adjacent open spaces to this character
	public static void getAdjacent(Player p, TreeSet<Coord> ts) {
		int upr = p.row-1;
		int upc = p.col;
		if (validSpace(upr,upc))
			ts.add(new Coord(upr,upc));

		int downr = p.row+1;
		int downc = p.col;
		if (validSpace(downr,downc))
			ts.add(new Coord(downr,downc));

		int leftr = p.row;
		int leftc = p.col-1;
		if (validSpace(leftr,leftc))
			ts.add(new Coord(leftr,leftc));

		int rightr = p.row;
		int rightc = p.col+1;
		if (validSpace(rightr,rightc))
			ts.add(new Coord(rightr,rightc));
	}

	public static boolean validSpace(int row, int col) {
		//out of bounds?
		if (row < 0 || row >= themap.length || col < 0 || col >= themap[0].length)
			return false;

		//not a space
		if (themap[row][col] != SPACE)
			return false;
		return true;
	}

	public static boolean validNode(int row, int col, int targetrow, int targetcol) {
		//out of bounds?
		if (row < 0 || row >= themap.length || col < 0 || col >= themap[0].length)
			return false;

		//not a space
		if (themap[row][col] != SPACE && (row !=targetrow && col != targetcol))
			return false;
		return true;
	}	

	static boolean isPath(int r1, int c1, int r2, int c2) 
	{ 
		
		if (themap[r1][c1] == WALL || themap[r2][c2] == WALL)
			return false;
		
		boolean b = false;

		HashMap<String,Coord> nodes = new HashMap<String,Coord>();

		//add the src and dst nodes
		Coord.idcounter = 0;
		
		nodes.put(r1+""+c1,new Coord(r1,c1));
		System.out.println("Node added: " + r1 +"," + c1);
		nodes.put(r2+""+c2,new Coord(r2,c2));
		System.out.println("Node added: " + r2 +"," + c2);

		//add the space nodes
		for (int r=0; r < maxrows; r++) {
			for (int c=0; c < maxcols; c++) {
				
				if (r == r1 && c == c1)
					continue;
				if (r == r2 && c == c2)
					continue;
				
				if (themap[r][c] == SPACE) {
					Coord crd = new Coord(r,c);
					System.out.println("Nodes added: " + r + "," + c);
					nodes.put(crd.row+""+crd.col,crd);
				}
				
				
			}	
		}

		//for each node, add its surrounding edges
		TreeSet<Edge> edges = new TreeSet<Edge>();
		for(Map.Entry<String, Coord> entry : nodes.entrySet()) {
			String rcStr = entry.getKey();
			Coord curr = entry.getValue();
			
			int upr = curr.row-1;
			int upc = curr.col;
			if (validNode(upr, upc, r2, c2)) {
				if (nodes.containsKey(upr+""+upc)) {
					Coord tempnode = nodes.get(upr+""+upc);
					Edge e = new Edge(curr.id,tempnode.id);
					if (!edges.contains(e))
						edges.add(e);
					e = new Edge(tempnode.id,curr.id);
					if (!edges.contains(e))
						edges.add(e);
				}
			}

			int downr = curr.row+1;
			int downc = curr.col;
			if (validNode(downr, downc, r2, c2)) {
				if (nodes.containsKey(downr+""+downc)) {
					Coord tempnode = nodes.get(downr+""+downc);
					Edge e = new Edge(curr.id,tempnode.id);
					if (!edges.contains(e))
						edges.add(e);
					e = new Edge(tempnode.id,curr.id);
					if (!edges.contains(e))
						edges.add(e);
				}
			}

			int leftr = curr.row;
			int leftc = curr.col-1;
			if (validNode(leftr, leftc, r2, c2)) {
				if (nodes.containsKey(leftr+""+leftc)) {
					Coord tempnode = nodes.get(leftr+""+leftc);
					Edge e = new Edge(curr.id,tempnode.id);
					if (!edges.contains(e))
						edges.add(e);
					e = new Edge(tempnode.id,curr.id);
					if (!edges.contains(e))
						edges.add(e);
				}
			}

			int rightr = curr.row;
			int rightc = curr.col+1;
			if (validNode(rightr, rightc, r2, c2)) {
				if (nodes.containsKey(rightr+""+rightc)) {
					Coord tempnode = nodes.get(rightr+""+rightc);
					Edge e = new Edge(curr.id,tempnode.id);
					if (!edges.contains(e))
						edges.add(e);
					e = new Edge(tempnode.id,curr.id);
					if (!edges.contains(e))
						edges.add(e);
				}
			}
			
		}

		System.out.println("Nodes:");
		for(Map.Entry<String, Coord> entry : nodes.entrySet()) {
			Coord n = entry.getValue();
			System.out.println(n.id + ": " + n.row + "," + n.col);
		}

		//create the graph to determine if there is a path
		Graph g = new Graph(nodes.size()); //nodes are the spaces + the src and dst
		System.out.println("nodes.size(): " + nodes.size());
		//System.out.println("Edges: ");
		for (Edge e : edges) {
			System.out.println(e.from + " -> " + e.to);
			g.addEdge(e.from, e.to);
		}

		int srcId = nodes.get(r1+""+c1).id;
		int dstId = nodes.get(r2+""+c2).id;
		System.out.println("Finding path from " + srcId + " -> " + dstId);
		int num_paths = g.printAllPaths(srcId,dstId);

		return num_paths > 0;
	} 

	public static void main(String[] args) {
		//TESTER
		GoblinBattle gb = new GoblinBattle();
		printMap();

		/*
		TreeSet<Coord> ts = inRange(GOBLIN);
		for (Coord c : ts) {
			themap[c.row][c.col]= '?'; 
		}
		System.out.println();
		printMap();
		 */

		System.out.println( isPath(1,1,3,1) ); //true elf to space
		System.out.println( isPath(1,1,1,5) ); //false elf to space (blocked by goblin)
		//System.out.println( isPath(1,1,1,2) ); //true
		//System.out.println( isPath(1,1,3,5) ); //false
		//System.out.println( isPath(4,0,5,0) ); //false - wall to wall
		//System.out.println( isPath(3,2,1,4) ); //true goblin to goblin
		//System.out.println( isPath(1,1,1,4) ); //true elf to goblin
		//System.out.println( isPath(1,1,3,2) ); //true elf to space
		//System.out.println( isPath(3,3,1,2) ); //true space to space
		//System.out.println( isPath(1,1,3,2) ); //true elf to elf (temp map)
		//System.out.println( isPath(1,1,3,4) ); //false elf to wall
		//System.out.println( isPath(3,4,1,1) ); //false wall to elf
		
		//gb.tick();
	} 


}
