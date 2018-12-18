package utils;

import java.util.ArrayList;

public class Vertex implements Comparable<Vertex>
{
	public final int name;
	public ArrayList<Edge1> adjacencies = new ArrayList<Edge1>();
	public double minDistance = Double.POSITIVE_INFINITY;
	public Vertex previous;
	public Vertex(int argName) { name = argName; }
	public String toString() { return name+""; }
	public int compareTo(Vertex other)
	{
		return Double.compare(minDistance, other.minDistance);
	}

}


