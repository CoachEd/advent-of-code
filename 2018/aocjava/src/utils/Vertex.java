package utils;

import java.util.ArrayList;

public class Vertex implements Comparable<Vertex>
{
	public final String name;
	public ArrayList<Edge1> adjacencies = new ArrayList<Edge1>();
	public double minDistance = Double.POSITIVE_INFINITY;
	public Vertex previous;
	public Vertex(String argName) { name = argName; }
	public String toString() { return name+""; }
	
	//meta data
	public int row;
	public int col;

	public Vertex(String s, int r, int c) {
		name = s;
		row = r;
		col = c;
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


