package twentytwo;

import java.util.ArrayList;

public class Vertex implements Comparable<Vertex>
{
	public final String name;
	public part2.RTYPE type;
	public ArrayList<Edge1> adjacencies = new ArrayList<Edge1>();
	public double minDistance = Double.POSITIVE_INFINITY;
	public Vertex previous;
	public String toString() { return name+""; }
	
	//meta data
	public int row;
	public int col;

	public Vertex(String argName) { 
		name = argName;
	}
	
	public Vertex(String s, part2.RTYPE t, int r, int c) {
		name = s;
		row = r;
		col = c;
		type = t;
	}
	
	public Vertex() {
		name = "";
		row = -1;
		col = -1;
	}
	
	public int compareTo(Vertex other)
	{
		return Double.compare(minDistance, other.minDistance);
	}

}


