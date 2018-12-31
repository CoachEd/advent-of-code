package twentyfive;

public class Point1 {
	public int w,x,y,z;
	public Point1(int w1,int x1,int y1,int z1) {
		w=w1;
		x=x1;
		y=y1;
		z=z1;
	}
	public String toString() {
		return w+","+x+","+y+","+z;
	}
	public int mdist(Point1 n) {
		return(Math.abs(n.w-w) + Math.abs(n.x-x) + Math.abs(n.y-y) + Math.abs(n.z-z));
	}
}
