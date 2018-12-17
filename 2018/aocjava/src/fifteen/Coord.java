package fifteen;

import java.util.TreeSet;

//for the walls
public class Coord implements Comparable<Coord> {

	int row;
	int col;

	public Coord(int row1, int col1) {
		row = row1;
		col = col1;
	}

	public static void main(String[] args) {
		//tester
		TreeSet<Coord> t = new TreeSet<Coord>();
		t.add(new Coord(0,1));
	
		
	}

	@Override
	public int compareTo(Coord c) {
		int rowdiff = row-c.row;
		int coldiff = col-c.col;
		if (rowdiff != 0)
			return rowdiff;
		if (coldiff != 0)
			return coldiff;
		return 0;
	}
}


