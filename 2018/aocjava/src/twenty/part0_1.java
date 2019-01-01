package twenty;

import java.util.ArrayList;
import java.util.Stack;

public class part0_1 {

	/*
###########
#.|.#.|.#.#
#-###-#-#-#
#.|.|.#.#.#
#-#####-#-#
#.#.#X|.#.#
#-#-#####-#
#.#.|.|.|.#
#-###-###-#
#.|.|.#.|.#
###########
	 */
	
	public static int width = 11;
	public static int height = 11;
	public static int startx = 5;
	public static int starty = 5;
	public static String smap = "ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN";
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

		// smap = ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN
		for (int i=0; i < smap.length(); i++) {
			char c = smap.charAt(i);
			switch(c) {
			case 'N':case'S':case'E':case'W':
				break;
			case '|':
				break;
			case '(':
				break;
			case ')':
				break;
			}
		}
		
		
		
		
		printRoom();		
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

