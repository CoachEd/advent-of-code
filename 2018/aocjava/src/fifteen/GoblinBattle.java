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
	static String fname = "files/goblin3.txt"; //working, need to make it more efficient; see where the slowdowns are
	//static String fname = "files/goblinfinal.txt"; //TOO SLOW
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
	static int alive_goblins = 0;
	static int alive_elves = 0;

	public String tick() {
		String sout = "";

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
			//System.out.println("moving " + players.get(i).c + ": " + players.get(i).row + "," + players.get(i).col);
			movePlayer(players.get(i));
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
					if (themap[row][col] == GOBLIN)
						alive_goblins++;
					else if (themap[row][col] == ELF)
						alive_elves++;
				}
			}

			//System.out.println("elves: " + alive_elves + "\ngoblins: " + alive_goblins);

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

			System.out.println("Players: " + players.size());
			System.out.println("Spaces: " + spaces.size());


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

	public static boolean validCoord(int row, int col) {
		//out of bounds?
		if (row < 0 || row >= maxrows || col < 0 || col >= maxcols)
			return false;
		return true;
	}

	public static boolean validSpace(int row, int col) {

		if (!validCoord(row,col))
			return false;

		//not a space
		if (themap[row][col] != SPACE)
			return false;
		return true;
	}

	public static boolean validNode(int row, int col, int targetrow, int targetcol) {
		//out of bounds?
		if (!validCoord(row,col))
			return false;

		//not a space
		if (themap[row][col] != SPACE && (row !=targetrow && col != targetcol))
			return false;
		return true;
	}	

	static ArrayList< ArrayList<Integer>> getPaths(int r1, int c1, int r2, int c2) 
	{

		ArrayList< ArrayList<Integer>> paths = new ArrayList< ArrayList<Integer>>();

		if (themap[r1][c1] == WALL || themap[r2][c2] == WALL)
			return paths;


		HashMap<String,Node> nodes = new HashMap<String,Node>();

		//add the src and dst nodes
		Node n0 =  new Node(0,r1,c1);
		nodes.put(r1+"|"+c1,n0);
		//System.out.println("Node added " + n0.id +": " + n0.row +"," + n0.col);
		Node n1 =  new Node(1,r2,c2);
		nodes.put(r2+"|"+c2,n1);
		//System.out.println("Node added " + n1.id +": " + n1.row +"," + n1.col);
		//add the space nodes
		int idcounter = 2;

		for (int r=0; r < maxrows; r++) {
			for (int c=0; c < maxcols; c++) {

				if (r == r1 && c == c1) {
					//System.out.println("Not adding: " + r + "," + c);
					continue;
				}
				if (r == r2 && c == c2) {
					//System.out.println("Not adding: " + r + "," + c);
					continue;			
				}

				if (themap[r][c] == SPACE) {
					Node n = new Node(idcounter,r,c);
					idcounter++;
					//System.out.println("Nodes added: " + r + "," + c);
					nodes.put(n.row+"|"+n.col,n);
					//System.out.println("Node added " + n.id +": " + n.row +"," + n.col + "   " + nodes.size());
				}
			}	
		}
		//System.out.println("*** nodes.size(): " + nodes.size());
		//for each node, add its surrounding edges
		TreeSet<Edge> edges = new TreeSet<Edge>();
		for(Map.Entry<String, Node> entry : nodes.entrySet()) {
			Node curr = entry.getValue();

			int upr = curr.row-1;
			int upc = curr.col;
			if (validNode(upr, upc, r2, c2)) {
				if (nodes.containsKey(upr+"|"+upc)) {
					Node tempnode = nodes.get(upr+"|"+upc);
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
				if (nodes.containsKey(downr+"|"+downc)) {
					Node tempnode = nodes.get(downr+"|"+downc);
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
				if (nodes.containsKey(leftr+"|"+leftc)) {
					Node tempnode = nodes.get(leftr+"|"+leftc);
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
				if (nodes.containsKey(rightr+"|"+rightc)) {
					Node tempnode = nodes.get(rightr+"|"+rightc);
					Edge e = new Edge(curr.id,tempnode.id);
					if (!edges.contains(e))
						edges.add(e);
					e = new Edge(tempnode.id,curr.id);
					if (!edges.contains(e))
						edges.add(e);
				}
			}

		}

		
		/*
		System.out.println("Nodes:");
		for(Map.Entry<String, Node> entry : nodes.entrySet()) {
			Node n = entry.getValue();
			System.out.println(n.id + ": " + n.row + "," + n.col);
		}
		System.out.println("*** nodes.size(): " + nodes.size());
		 */

		//create the graph to determine if there is a path
		Graph g = new Graph(nodes.size()+2); //nodes are the spaces + the src and dst
		//System.out.println("new graph size: " + nodes.size());
		//System.out.println(r1+"," + c1 + "  -> " + r2+"," + c2);

		//System.out.println("Edges: ");
		for (Edge e : edges) {
			//System.out.println(e.from + " -> " + e.to);
			g.addEdge(e.from, e.to);
		}

		int srcId = nodes.get(r1+"|"+c1).id;
		int dstId = nodes.get(r2+"|"+c2).id;
		//System.out.println("Finding path from " + srcId + " -> " + dstId);
		paths = g.printAllPaths(srcId,dstId);

		return paths;
	} 

	static int getSmallestPathSize(int r1, int c1, int r2, int c2) 
	{

		ArrayList< ArrayList<Integer>> paths = new ArrayList< ArrayList<Integer>>();

		if (themap[r1][c1] == WALL || themap[r2][c2] == WALL)
			return paths.size();


		HashMap<String,Node> nodes = new HashMap<String,Node>();

		//add the src and dst nodes

		nodes.put(r1+"|"+c1,new Node(0,r1,c1));
		//System.out.println("Node added: " + r1 +"," + c1);
		nodes.put(r2+"|"+c2,new Node(1,r2,c2));
		//System.out.println("Node added: " + r2 +"," + c2);

		//add the space nodes
		int idcounter = 2;
		for (int r=0; r < maxrows; r++) {
			for (int c=0; c < maxcols; c++) {

				if (r == r1 && c == c1)
					continue;
				if (r == r2 && c == c2)
					continue;

				if (themap[r][c] == SPACE) {
					Node n = new Node(idcounter, r,c);
					idcounter++;
					//System.out.println("Nodes added: " + r + "," + c);
					nodes.put(n.row+"|"+n.col,n);
				}


			}	
		}

		//for each node, add its surrounding edges
		TreeSet<Edge> edges = new TreeSet<Edge>();
		for(Map.Entry<String, Node> entry : nodes.entrySet()) {
			Node curr = entry.getValue();

			int upr = curr.row-1;
			int upc = curr.col;
			if (validNode(upr, upc, r2, c2)) {
				if (nodes.containsKey(upr+"|"+upc)) {
					Node tempnode = nodes.get(upr+"|"+upc);
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
				if (nodes.containsKey(downr+"|"+downc)) {
					Node tempnode = nodes.get(downr+"|"+downc);
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
				if (nodes.containsKey(leftr+"|"+leftc)) {
					Node tempnode = nodes.get(leftr+"|"+leftc);
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
				if (nodes.containsKey(rightr+"|"+rightc)) {
					Node tempnode = nodes.get(rightr+"|"+rightc);
					Edge e = new Edge(curr.id,tempnode.id);
					if (!edges.contains(e))
						edges.add(e);
					e = new Edge(tempnode.id,curr.id);
					if (!edges.contains(e))
						edges.add(e);
				}
			}

		}

		/*
		System.out.println("Nodes:");
		for(Map.Entry<String, Node> entry : nodes.entrySet()) {
			Node n = entry.getValue();
			System.out.println(n.id + ": " + n.row + "," + n.col);
		}
		 */

		//System.out.println("finding path from... " + r1+","+c1 + "  to  " + r2+","+c2);

		//create the graph to determine if there is a path
		Graph g = new Graph(nodes.size()); //nodes are the spaces + the src and dst
		//System.out.println("Edges: ");
		for (Edge e : edges) {
			//System.out.println(e.from + " -> " + e.to);
			g.addEdge(e.from, e.to);
		}

		int srcId = nodes.get(r1+"|"+c1).id;
		int dstId = nodes.get(r2+"|"+c2).id;
		int smallest_path = g.smallestPath(srcId,dstId);

		return smallest_path;
	}

	//returning a move of r,c [-1,-1] means don't/can't move (because we are blocked in or we should attack
	//the adjacent goblin
	public static int[] move(int r, int c) {
		int[] themove = new int[] {-1,-1};

		if (alive_goblins == 0 || alive_elves == 0) {
			//combat ends; no more targets
			System.err.println("no more targets");
			return themove;
		}

		//make sure the r,c is in bounds
		if (r < 0 || r >= maxrows || c < 0 || c >= maxcols) {
			System.err.println("r,c out of bounds");
			return themove;
		}

		//make sure the piece moving is an ELF or GOBLIN
		char theplayer = themap[r][c];
		if (theplayer != ELF && theplayer != GOBLIN) {
			System.err.println("invalid piece to move");
			return themove;
		}

		//theplayer will be 'E' or 'G' at this point
		//steps has at least one open coord (u,d,l,r)
		//players has both types of players GOBLIN and ELF
		char thetarget = ELF;
		if (theplayer == ELF)
			thetarget = GOBLIN;

		//get the valid steps on the board (may be occupied)
		ArrayList<Coord> steps = new ArrayList<Coord>();
		int upr = r-1;
		int upc = c;
		if (validSpace(upr,upc))
			steps.add(new Coord(upr,upc));
		int downr = r+1;
		int downc = c;
		if (validSpace(downr,downc))
			steps.add(new Coord(downr,downc));
		int rightr = r;
		int rightc = c+1;
		if (validSpace(rightr,rightc))
			steps.add(new Coord(rightr,rightc));
		int leftr = r;
		int leftc = c-1;
		if (validSpace(leftr,leftc))
			steps.add(new Coord(leftr,leftc));		

		//if already next to an enemy, move turn is over. now attack
		if ((validCoord(upr,upc) && themap[upr][upc] == thetarget) ||
				(validCoord(downr,downc) && themap[downr][downc] == thetarget) ||
				(validCoord(rightr,rightc) && themap[rightr][rightc] == thetarget) ||
				(validCoord(leftr,leftc) && themap[leftr][leftc] == thetarget) ) {
			return themove;
		}

		//count open spaces around player
		int open_spaces = 0;
		for (int i=0; i < steps.size(); i++) {
			Coord ctemp = steps.get(i);
			if (themap[ctemp.row][ctemp.col] == SPACE)
				open_spaces++;
		}

		//immediately return if we are already next to a goblin (time to attack!)
		//or if there are no open adjacent steps (u,d,l,r); we cannot move if we wanted to
		if (open_spaces == 0)
			return themove;

		//BEGIN move algorithm here; there are targets left


		//TODO: identify targets. if no targets remain, combat ends
		//loop through the players list and find the targets, then get their open steps
		ArrayList<Player> targets = new ArrayList<Player>();
		for (Player p : players) {
			if (p.c == thetarget) {
				targets.add(p);
			}
		}

		//any targets?
		if (targets.size() == 0) {
			System.err.println("no targets");
			return themove;
		}

		//get open steps around targets
		ArrayList<Coord> inRange = new ArrayList<Coord>();
		for (Player p : targets) {
			upr = p.row-1;
			upc = p.col;
			if (validCoord(upr,upc) && themap[upr][upc] == SPACE)
				inRange.add(new Coord(upr,upc));
			downr = p.row+1;
			downc = p.col;
			if (validCoord(downr,downc) && themap[downr][downc] == SPACE)
				inRange.add(new Coord(downr,downc));
			rightr = p.row;
			rightc = p.col+1;
			if (validCoord(rightr,rightc) && themap[rightr][rightc] == SPACE)
				inRange.add(new Coord(rightr,rightc));
			leftr = p.row;
			leftc = p.col-1;
			if (validCoord(leftr,leftc) && themap[leftr][leftc] == SPACE)
				inRange.add(new Coord(leftr,leftc));
		}

		if (inRange.size() == 0) {
			//no spaces in range of target, don't move
			return themove;
		}
		
		
		//of the inRange spaces, which are reachable?
		int smallest_path = 0x7fffffff;
		for (Coord c2 : inRange) {
			ArrayList< ArrayList<Integer>> paths = getPaths(r,c,c2.row,c2.col);
			if (paths.size() > 0) {
				//find the smallest path from the src node to the current inRange node
				for (ArrayList<Integer> l : paths) {
					if (l.size() <= smallest_path) {
						smallest_path = l.size();
					}
				}
			}
		}

		ArrayList<Coord> nearest = new ArrayList<Coord>();
		for (Coord c2 : inRange) {
			ArrayList< ArrayList<Integer>> paths = getPaths(r,c,c2.row,c2.col);
			if (paths.size() > 0) {
				int temp_path_size =  0x7fffffff;
				for (ArrayList<Integer> l : paths) {
					if (l.size() <= temp_path_size) {
						temp_path_size = l.size();
					}
				}
				if (temp_path_size <= smallest_path)
					nearest.add(c2);
			}
		}		

		//if more than one nearest, pick one that is first in reading order
		int row=maxrows-1; int col=maxcols-1;
		for (Coord c2 : nearest) {
			if (c2.row < row) {
				row = c2.row;
				col = c2.col;
			} else if (c2.row == row) {
				if (c2.col < col) {
					row = c2.row;
					col = c2.col;
				}
			}
		}



		//return row, col
		themove[0] = row;
		themove[1] = col;

		//TODO: if no reachable nodes, or  
		//TODO: To move...
		//TODO: which in nodes are in range (adjacent to) goblins?
		//TODO: of those nodes, which are reachable by the elf?
		//TODO: of those nodes, which are nearest to the elf?
		//      if there is a tie (distance-wise), pick the one that is first in reading oder
		//      this is the destination square
		//TODO: of the steps that the node can go to (UP,DOWN,LEFT,RIGHT), which one is closest to the
		//      destination square? if a tie, pick the one that is first in reading order
		//TODO: If the unit is not already in range of a target, and there are no open squares 
		//      which are in range of a target, the unit ends its move turn. attack is next		





		return themove;
	}


	public void movePlayer(Player p) {
		
		int startr = p.row;
		int startc = p.col;

		int[] next_move = move(startr,startc); //try to move E at this position
		//System.out.println("next move: " + next_move[0] + "," + next_move[1]);

		//MOVE: take a step that is closest to chosen target; shortest path from u,d,l,r to the target

		int targetr = next_move[0];
		int targetc = next_move[1];
		int r = startr; //player r 
		int c = startc; //player c

		if (targetr == -1 || targetc == -1) {
			//can't/shouldn't move
			return;
		}



		int upr = r-1;
		int upc = c;
		int smallest_distance =  0x7fffffff;
		ArrayList<Coord> steps_to_take = new ArrayList<Coord>();
		ArrayList<Integer> steps_to_take_distance = new ArrayList<Integer>();
		int[] steps = {-1,-1,-1,-1}; //up,down,right,left
		if (validSpace(upr,upc)) {
			steps_to_take.add(new Coord(upr,upc));
			//if next move is the target, then make the distance -99
			if (upr==targetr && upc==targetc) {
				steps[0] = -99;
			} else {
				steps[0] = getSmallestPathSize(upr,upc,targetr,targetc); 
			}
			if (steps[0] != 0 && steps[0] < smallest_distance) {
				smallest_distance = steps[0];
			}
			steps_to_take_distance.add(steps[0]);
		}

		int downr = r+1;
		int downc = c;
		if (validSpace(downr,downc)) {
			steps_to_take.add(new Coord(downr,downc));
			//if next move is the target, then make the distance -99
			if (downr==targetr && downc==targetc) {
				steps[1] = -99;
			} else {
				steps[1] = getSmallestPathSize(downr,downc,targetr,targetc); 
			}
			if (steps[1] != 0 && steps[1] < smallest_distance) {
				smallest_distance = steps[1];
			}
			steps_to_take_distance.add(steps[1]);
		}

		int rightr = r;
		int rightc = c+1;
		if (validSpace(rightr,rightc)) {
			steps_to_take.add(new Coord(rightr,rightc));
			//if next move is the target, then make the distance -99
			if (rightr==targetr && rightc==targetc) {
				steps[2] = -99;
			} else {
				steps[2] = getSmallestPathSize(rightr,rightc,targetr,targetc); 
			}
			if (steps[2] != 0 && steps[2] < smallest_distance) {
				smallest_distance = steps[2];
			}
			steps_to_take_distance.add(steps[2]);
		}

		int leftr = r;
		int leftc = c-1;
		if (validSpace(leftr,leftc)) {
			steps_to_take.add(new Coord(leftr,leftc));
			//if next move is the target, then make the distance -99
			if (leftr==targetr && leftc==targetc) {
				steps[3] = -99;
			} else {
				steps[3] = getSmallestPathSize(leftr,leftc,targetr,targetc); 
			}
			if (steps[3] != 0 && steps[3] < smallest_distance) {
				smallest_distance = steps[3];
			}
			steps_to_take_distance.add(steps[3]);
		}

		//System.out.println("up,down,right,left  " + steps[0] + " , " + steps[1] + " , " + steps[2] +  " , " + steps[3]);
		ArrayList<Coord> steps_to_keep = new ArrayList<Coord>();
		for (int i=0; i < steps_to_take.size(); i++) {
			Coord crd = steps_to_take.get(i);
			int dist = steps_to_take_distance.get(i);
			if (dist == smallest_distance) {
				//keep it
				steps_to_keep.add(crd);
			}
		}

		int finalrow = -1, finalcol = -1;
		if (steps_to_keep.size() == 1) {
			finalrow = steps_to_keep.get(0).row;
			finalcol = steps_to_keep.get(0).col;
		} else {
			//get reading order
			int row=maxrows-1; int col=maxcols-1;
			for (Coord c2 : steps_to_keep) {
				if (c2.row < row) {
					row = c2.row;
					col = c2.col;
				} else if (c2.row == row) {
					if (c2.col < col) {
						row = c2.row;
						col = c2.col;
					}
				}
			}
			finalrow = row;
			finalcol = col;
		}

		//THE MOVE
		//System.out.println("move to: " + finalrow +"," + finalcol);
		themap[startr][startc] = SPACE;  //make current spot space
		themap[finalrow][finalcol] = p.c; //move player
		//update player's location
		p.row = finalrow;
		p.col = finalcol;

	}

	public static void main(String[] args) {
		//TESTER
		GoblinBattle gb = new GoblinBattle();
		printMap(); //t0
		gb.tick(); printMap(); //t1
		gb.tick(); printMap(); //t2 - 2,4 Goblin should NOT move
		gb.tick(); printMap(); //t3



	} 


}
