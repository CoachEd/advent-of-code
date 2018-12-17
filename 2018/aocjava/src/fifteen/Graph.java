package fifteen;

//JAVA program to print all  
//paths from a source to 
//destination. 
//https://www.geeksforgeeks.org/find-paths-given-source-destination/
import java.util.ArrayList; 

//A directed graph using 
//adjacency list representation 
public class Graph { 

	public static int numPaths = 0;
	public static ArrayList< ArrayList<Integer> > globalPathList = null;

	// No. of vertices in graph 
	private int v;  

	// adjacency list  
	private ArrayList<Integer>[] adjList;  

	//Constructor 
	public Graph(int vertices){ 
		//System.out.println("vertices: " + vertices);
		//initialise vertex count 
		this.v = vertices; 

		// initialise adjacency list 
		initAdjList();  
	} 

	// utility method to initialise 
	// adjacency list 
	@SuppressWarnings("unchecked") 
	private void initAdjList() 
	{ 
		adjList = new ArrayList[v]; 

		for(int i = 0; i < v; i++) 
		{ 
			adjList[i] = new ArrayList<>(); 
		} 
	} 

	// add edge from u to v 
	public void addEdge(int u, int v) 
	{ 
		// Add v to u's list. 
		//System.out.println(adjList.length);
		//System.out.println(adjList.length);
		adjList[u].add(v);  
	} 

	// Prints all paths from 
	// 's' to 'd' 
	@SuppressWarnings("unchecked")
	public ArrayList< ArrayList<Integer>> printAllPaths(int s, int d)  
	{ 
		//reset counter
		numPaths = 0;
		globalPathList = new ArrayList< ArrayList<Integer> >();

		boolean[] isVisited = new boolean[v]; 
		ArrayList<Integer> pathList = new ArrayList<>(); 

		//add source to path[] 
		pathList.add(s); 

		//Call recursive utility 
		printAllPathsUtil(s, d, isVisited, pathList); 
		//System.out.println("numPaths: " + numPaths);
		//System.out.println("globalPathList size: " + globalPathList.size());

		/*
		for (ArrayList<Integer> l : globalPathList) {
			for (Integer i : l) {
				System.out.print(i + " ");
			}
			System.out.println();
		}
		 */

		return (ArrayList<ArrayList<Integer>>) (globalPathList.clone());
	} 

	public int smallestPath(int s, int d)  
	{ 
		//reset counter
		numPaths = 0;
		globalPathList = new ArrayList< ArrayList<Integer> >();

		boolean[] isVisited = new boolean[v]; 
		ArrayList<Integer> pathList = new ArrayList<>(); 

		//add source to path[] 
		pathList.add(s); 

		//Call recursive utility 
		printAllPathsUtil(s, d, isVisited, pathList); 
		//System.out.println("numPaths: " + numPaths);
		//System.out.println("globalPathList size: " + globalPathList.size());

		int smallest_path = 0x7fffffff;
		for (ArrayList<Integer> l : globalPathList) {
			if (l.size() < smallest_path)
				smallest_path = l.size();
		}


		return smallest_path;
	} 	


	// A recursive function to print 
	// all paths from 'u' to 'd'. 
	// isVisited[] keeps track of 
	// vertices in current path. 
	// localPathList<> stores actual 
	// vertices in the current path 
	@SuppressWarnings("unchecked")
	private void printAllPathsUtil(Integer u, Integer d, 
			boolean[] isVisited, 
			ArrayList<Integer> localPathList) { 

		// Mark the current node 
		isVisited[u] = true; 

		if (u.equals(d))  
		{ 
			numPaths++;

			//uncomment to see paths
			//System.out.println(localPathList);
			globalPathList.add((ArrayList<Integer>)localPathList.clone());

			// if match found then no need to traverse more till depth 
			isVisited[u]= false; 
			return ; 
		} 

		// Recur for all the vertices 
		// adjacent to current vertex 
		for (Integer i : adjList[u])  
		{ 
			if (!isVisited[i]) 
			{ 
				// store current node  
				// in path[] 
				localPathList.add(i); 
				printAllPathsUtil(i, d, isVisited, localPathList); 

				// remove current node 
				// in path[] 
				localPathList.remove(i); 
			} 
		} 

		// Mark the current node 
		isVisited[u] = false; 
	} 

	// Driver program 
	public static void main(String[] args)  
	{ 

		// Create a sample graph 
		Graph g = new Graph(11); 
		g.addEdge(0,2); 
		g.addEdge(0,5); 
		g.addEdge(1,8); 
		g.addEdge(2,0); 
		g.addEdge(2,3); 
		g.addEdge(2,6);
		g.addEdge(3,2);
		g.addEdge(3,7);
		g.addEdge(4,8);
		g.addEdge(5,0);
		g.addEdge(5,6);
		g.addEdge(5,9);
		g.addEdge(6,2);
		g.addEdge(6,5);
		g.addEdge(6,7);
		g.addEdge(7,3);
		g.addEdge(7,6);
		g.addEdge(7,10);
		g.addEdge(8,1);
		g.addEdge(8,4);
		g.addEdge(9,5);
		g.addEdge(10,7);


		// arbitrary source 
		int s = 0; 

		// arbitrary destination 
		int d = 10; 
		d = 4;

		System.out.println("Following are all different paths from "+s+" to "+d); 
		g.printAllPaths(s, d); 







	} 
} 

//This code is contributed by Himanshu Shekhar. 
