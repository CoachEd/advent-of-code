package eight;

import java.util.ArrayList;
import java.util.TreeMap;


public class node {
	char c;
	
	//header
	int num_children;
	int num_metadata;
	
	TreeMap<Character,node> children = new TreeMap<Character,node>();
	ArrayList<Integer> metadata = new ArrayList<Integer>();
	public node(char c1) { c = c1; }
	void addChild(node nChild) {
		children.put(nChild.c, nChild);
	}
}
