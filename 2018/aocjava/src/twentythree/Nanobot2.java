package twentythree;

public class Nanobot2 {
	public long x,y,z,r;
	public Nanobot2(long x1, long y1, long z1, long r1) {
		x = x1;
		y = y1;
		z = z1;
		r = r1;
	}

	public String toString() {
		return(x+","+y+","+z+" "+ r);
	}
	
	public long mdist(Nanobot2 n) {
		return(Math.abs(n.x-x) + Math.abs(n.y-y) + Math.abs(n.z-z));
	}
	
	public boolean overlaps(Nanobot2 n) {
		long x1 = x-r;
		long x2 = x+r;
		long y1 = y-r;
		long y2 = y+r;
		long z1 = z-r;
		long z2 = z+r;
		if ( (n.x >= x1 && n.x <= x2) || (n.y >= y1 && n.y <= y2) || (n.z >= z1 && n.z <= z2))
			return true;
		
		x1 = n.x-r;
		x2 = n.x+r;
		y1 = n.y-r;
		y2 = n.y+r;
		z1 = n.z-r;
		z2 = n.z+r;
		if ( (x >= x1 && x <= x2) || (y >= y1 && y <= y2) || (z >= z1 && z <= z2))
			return true;

		return false;
	}
}
