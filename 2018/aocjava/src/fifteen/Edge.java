package fifteen;

public class Edge implements Comparable<Edge> {

	int from; //from node id
	int to; //to node id

	public Edge(int from1, int to1) {
		from = from1;
		to = to1;
	}

	@Override
	public int compareTo(Edge e) {
		int fromdiff = from-e.from;
		int todiff = to-e.to;
		if (fromdiff != 0)
			return fromdiff;
		if (todiff != 0)
			return todiff;
		return 0;
	}

}


