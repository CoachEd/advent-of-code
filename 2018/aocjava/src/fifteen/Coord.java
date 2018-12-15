package fifteen;

import java.util.TreeSet;

//for the walls
public class Coord implements Comparable<Coord> {

	int row;
	int col;
	int id;
	public static int idcounter = 0;

	public Coord(int row1, int col1) {
		row = row1;
		col = col1;
		id = idcounter;
		idcounter++;
	}

	public static void main(String[] args) {
		//tester
		TreeSet<Coord> t = new TreeSet<Coord>();
		t.add(new Coord(0,1));
		Coord temp0 = new Coord(1,1);
		t.add(temp0);
		System.out.println(temp0.id);
		t.add(new Coord(1,1));

		Coord temp = new Coord(1,1);
		System.out.println(t.contains(temp));
		System.out.println(temp.id);
		
		
		
		


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


