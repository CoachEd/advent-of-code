package twentytwo;

import java.util.PriorityQueue;
import java.util.Random;

import twentytwo.part2.RTYPE;
import twentytwo.part2.TOOLS;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Dijkstra
{
	public static TOOLS equipped = TOOLS.torch;
	public static void computePaths(Vertex source,Random r)
	{
		source.minDistance = 0.;
		PriorityQueue<Vertex> vertexQueue = new PriorityQueue<Vertex>();
		vertexQueue.add(source);
		equipped = TOOLS.torch;
		while (!vertexQueue.isEmpty()) {
			Vertex u = vertexQueue.poll();

			// Visit each edge exiting u
			for (Edge1 e : u.adjacencies)
			{
				//System.out.println("weight from " + u.name + " to " + e.target+" is " + e.weight);
				Vertex v = e.target;
				double weight = e.weight;
				
				//add cost to switch tools (if applicable) to weight
				RTYPE next_type = v.type;
				double added_weight = 0;
				switch(next_type) {
				case rocky:
					//In rocky regions, you can use the climbing gear or the torch. 
					//You cannot use neither (you'll likely slip and fall).
					if (equipped == TOOLS.neither) {
						//need to switch to climbing or torch
						//RANDOMLY choose? between the two?
						if ((int)(r.nextFloat() * 2) == 1)
							equipped = TOOLS.climbing;
						else
							equipped = TOOLS.torch;
						added_weight = 7;
					}
					break;
				case wet:
					//In wet regions, you can use the climbing gear or neither tool. 
					//You cannot use the torch (if it gets wet, you won't have a light source).
					if (equipped == TOOLS.torch) {
						//need to switch to climbing or torch
						//RANDOMLY choose? between the two?
						if ((int)(r.nextFloat() * 2) == 1)
							equipped = TOOLS.climbing;
						else
							equipped = TOOLS.neither;
						added_weight = 7;
					}					
					break;
				case narrow:
					//In narrow regions, you can use the torch or neither tool. 
					//You cannot use the climbing gear (it's too bulky to fit).
					if (equipped == TOOLS.climbing) {
						//need to switch to climbing or torch
						//RANDOMLY choose? between the two?
						if ((int)(r.nextFloat() * 2) == 1)
							equipped = TOOLS.torch;
						else
							equipped = TOOLS.neither;
						added_weight = 7;
					}					
					break;
				}
				e.equipped = equipped;
				double distanceThroughU = u.minDistance + weight + added_weight;
				
				if (distanceThroughU < v.minDistance) {
					vertexQueue.remove(v);

					v.minDistance = distanceThroughU ;
					v.previous = u;
					vertexQueue.add(v);
				}
			}
		}
	}

	public static List<Vertex> getShortestPathTo(Vertex target)
	{
		List<Vertex> path = new ArrayList<Vertex>();
		for (Vertex vertex = target; vertex != null; vertex = vertex.previous)
			path.add(vertex);

		Collections.reverse(path);
		return path;
	}

	public static void main(String[] args)
	{
		
		// mark all the vertices 
		Vertex A0 = new Vertex(0+"");
		Vertex A1 = new Vertex(1+"");
		Vertex A2 = new Vertex(2+"");
		Vertex A3 = new Vertex(3+"");
		Vertex A4 = new Vertex(4+"");
		Vertex A5 = new Vertex(5+"");
		Vertex A6 = new Vertex(6+"");
		Vertex A7 = new Vertex(7+"");
		Vertex A8 = new Vertex(8+"");
		Vertex A9 = new Vertex(9+"");
		Vertex A10 = new Vertex(10+"");


		// set the edges and weight
		A0.adjacencies.add(new Edge1(A2, 99));
		A0.adjacencies.add(new Edge1(A5, 1));
		A1.adjacencies.add(new Edge1(A8, 1));
		A2.adjacencies.add(new Edge1(A0, 1));
		A2.adjacencies.add(new Edge1(A3, 1));
		A2.adjacencies.add(new Edge1(A6, 1));
		A3.adjacencies.add(new Edge1(A2, 1));
		A3.adjacencies.add(new Edge1(A7, 1));
		A4.adjacencies.add(new Edge1(A8, 1));
		A5.adjacencies.add(new Edge1(A0, 1));
		A5.adjacencies.add(new Edge1(A6, 1));
		A5.adjacencies.add(new Edge1(A9, 1));
		A6.adjacencies.add(new Edge1(A2, 1));
		A6.adjacencies.add(new Edge1(A5, 1));
		A6.adjacencies.add(new Edge1(A7, 1));
		A7.adjacencies.add(new Edge1(A3, 1));
		A7.adjacencies.add(new Edge1(A6, 1));
		A7.adjacencies.add(new Edge1(A10, 1));
		A8.adjacencies.add(new Edge1(A1, 1));
		A8.adjacencies.add(new Edge1(A4, 1));
		A9.adjacencies.add(new Edge1(A5, 1));
		A10.adjacencies.add(new Edge1(A7, 1));


		computePaths(A0,new Random()); // run Dijkstra
		List<Vertex> path = getShortestPathTo(A10); //no path is list of size 1 (itself)
		System.out.println("Path: " + path + "   path.size(): " + path.size());
		
		
	}
}