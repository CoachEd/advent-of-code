package fifteen;

public class Node implements Comparable<Coord> {

	int row;
	int col;
	int id;
	static int idcounter = 0;

	public Node(int row1, int col1) {
		id = idcounter;
		row = row1;
		col = col1;
		idcounter++;
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


