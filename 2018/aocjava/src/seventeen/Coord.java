package seventeen;

public class Coord implements Comparable<Coord> {

	int y,x;

	public Coord(int x1, int y1) {
		x = x1;
		y = y1;
	}

	@Override
	public int compareTo(Coord c) {
		int xdiff = x-c.x;
		int ydiff = y-c.y;
		if (xdiff != 0)
			return xdiff;
		if (ydiff != 0)
			return ydiff;
		return 0;
	}
}


