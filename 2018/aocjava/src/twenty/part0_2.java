package twenty;

import java.util.ArrayList;

public class part0_2 {

	public static int width = 11;
	public static int height = 11;
	public static int startx = 5;
	public static int starty = 5;
	public static char[][] themap = new char[height][width];
	public static char UNKNOWN = '?';
	public static char ROOM = '.';
	public static char WALL = '#';
	public static char HDOOR = '|';
	public static char VDOOR = '-';
	public static int currx, curry;

	public static void main(String[] args) {

		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				themap[row][col] = '?';
			}
		}


		//combinations generated by: python exrex.py 'ENWWW(NEEE|SSE(EE|N))' 
		ArrayList<String> al = new ArrayList<String>();
		al.add("ENNWSWWNEWSSSSEENWNSEEESWENNNN");
		al.add("ENNWSWWNEWSSSSEENWNSEEENNN");
		al.add("ENNWSWWNEWSSSSEENEESWENNNN");
		al.add("ENNWSWWNEWSSSSEENEENNN");
		al.add("ENNWSWWSSSEENWNSEEESWENNNN");
		al.add("ENNWSWWSSSEENWNSEEENNN");
		al.add("ENNWSWWSSSEENEESWENNNN");
		al.add("ENNWSWWSSSEENEENNN");
		for (String s : al) {
			//start position
			currx = startx;
			curry = starty;
			themap[curry][currx] = 'X';
			parseliteral(s,currx,curry);
		}

		printRoom();
	}

	public static void parseliteral(String s, int currx, int curry) {
		if (s == null || s.length() == 0)
			return;
		for (int i=0; i < s.length(); i++) {
			char c = s.charAt(i);
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
		}
		return;
	}

	public static void printRoom() {
		String s = "";
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				if (themap[row][col] == UNKNOWN)
					themap[row][col] = WALL;
				s += themap[row][col];
			}
			s+="\n";
		}
		System.out.println(s);
	}

}

