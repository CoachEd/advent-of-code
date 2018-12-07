
package testproj;

import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;

public class Seven_1 {



	public static void main(String[] args) {
		Map<Character,Node> seenNodes = new TreeMap<Character,Node>();
		char[][] steps = {
				{'C','A'},
				{'C','F'},
				{'A','B'},
				{'A','D'},
				{'B','E'},
				{'D','E'},
				{'F','E'},
		};

		for (int i=0; i < steps.length; i++) {
			char[] step = steps[i];
			char cStart = step[0];
			char cEnd = step[1];
			Node nStart = null;
			Node nEnd = null;

			if (seenNodes.containsKey(cStart)) {
				nStart = seenNodes.get(cStart);
			} else {
				nStart = new Node(cStart);
				seenNodes.put(cStart, nStart);
			}

			if (seenNodes.containsKey(cEnd)) {
				nEnd = seenNodes.get(cEnd);
			} else {
				nEnd = new Node(cEnd);
				seenNodes.put(cEnd, nEnd);
			}

			nStart.children.put(cEnd, nEnd);
		}

		//Find root
		Node root = seenNodes.get('C');
		while (root.children.size() != 0) {
			System.out.print(root.c);
			Node new_root = root.children.firstEntry().getValue();
			root.children.remove(new_root.c);
			new_root.children.putAll(root.children);
			root = new_root;
		}

	} //end MAIN

	public void printTree(Node root) {
		System.out.print(root.c);

	}

}

class Node {
	char c;
	TreeMap<Character,Node> children = new TreeMap<Character,Node>();
	public Node(char c1) { c = c1; }
	void addChild(Node n) {
		children.put(n.c, n);
	}
}



