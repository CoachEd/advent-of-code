package fifteen;

public class Node implements Comparable<Coord> {

	int row;
	int col;
	int id;

	public Node(int id1,int row1, int col1) {
		id = id1;
		row = row1;
		col = col1;
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


