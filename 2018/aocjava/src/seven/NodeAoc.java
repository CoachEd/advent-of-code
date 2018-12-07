package seven;

import java.util.TreeMap;


public class NodeAoc {
	char c;
	TreeMap<Character,NodeAoc> children = new TreeMap<Character,NodeAoc>();
	TreeMap<Character,NodeAoc> parents = new TreeMap<Character,NodeAoc>();
	public NodeAoc(char c1) { c = c1; }
	void addChild(NodeAoc nChild) {
		children.put(nChild.c, nChild);
		nChild.parents.put(c, this);
	}
}
