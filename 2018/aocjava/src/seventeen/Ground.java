package seventeen;

public class Ground implements Comparable<Ground> {

	char c;
	int y,x;

	public void swap(Ground g) {
		char tc = c;
		int tx = x;
		int ty = y;
		c = g.c;
		x = g.x;
		y = g.y;
		g.c = tc;
		g.x = tx;
		g.y = ty;
	}
	
	public Ground(int x1, int y1, char c1) {
		x = x1;
		y = y1;
		c = c1;
	}
	
	public Ground(Ground g) {
		c = g.c;
		y = g.y;
		x = g.x;
	}

	@Override
	public int compareTo(Ground g) {
		int xdiff = x-g.x;
		int ydiff = y-g.y;
		if (xdiff != 0)
			return xdiff;
		if (ydiff != 0)
			return ydiff;
		return 0;
	}
}
