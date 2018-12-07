
package seven;

import java.util.Map;
import java.util.TreeMap;

public class Seven_1 {


	//sample: CABDFE
	//try1: ADEFKLBVHJQWRUNXCGOTMYIPSZ (wrong)
	//try2: AVHJQWRUNYIPSDLBXCGOTMZEFK (wrong)
	//try3: AJHDLBEGMFCIKNOPQRSTUVWXYZ (wrong)
	//try4: ADEFBJHCGKILMNOQPRTSUVWXYZ (wrong)
	//try5: ADEFKLBVJQWUXCNGORTMYSIHPZ (GOOD!)
	//sort steps in descending order by start letter
	public static void main(String[] args) {
		Map<Character,NodeAoc> seenNodes = new TreeMap<Character,NodeAoc>();
		char[][] steps = {
				{'Y','S'},
				{'Y','P'},
				{'Y','I'},
				{'X','Z'},
				{'X','S'},
				{'X','O'},
				{'X','G'},
				{'X','C'},
				{'W','Y'},
				{'W','U'},
				{'W','R'},
				{'W','I'},
				{'W','C'},
				{'V','W'},
				{'V','Q'},
				{'V','O'},
				{'V','J'},
				{'V','H'},
				{'U','R'},
				{'U','O'},
				{'U','N'},
				{'U','G'},
				{'T','Y'},
				{'T','P'},
				{'T','M'},
				{'T','H'},
				{'S','Z'},
				{'S','P'},
				{'S','I'},
				{'R','S'},
				{'R','I'},
				{'R','H'},
				{'Q','U'},
				{'Q','S'},
				{'Q','P'},
				{'Q','O'},
				{'Q','M'},
				{'P','Z'},
				{'O','Z'},
				{'O','T'},
				{'O','S'},
				{'O','R'},
				{'O','I'},
				{'N','Z'},
				{'N','T'},
				{'N','S'},
				{'N','I'},
				{'N','G'},
				{'M','Y'},
				{'M','S'},
				{'M','P'},
				{'L','T'},
				{'L','N'},
				{'L','B'},
				{'K','T'},
				{'K','R'},
				{'K','N'},
				{'K','B'},
				{'J','Z'},
				{'J','R'},
				{'J','N'},
				{'J','H'},
				{'I','Z'},
				{'I','P'},
				{'I','H'},
				{'H','Z'},
				{'H','P'},
				{'G','Y'},
				{'G','T'},
				{'G','I'},
				{'G','H'},
				{'F','Q'},
				{'F','O'},
				{'F','K'},
				{'F','I'},
				{'F','C'},
				{'E','U'},
				{'E','R'},
				{'E','P'},
				{'E','O'},
				{'E','N'},
				{'E','M'},
				{'E','G'},
				{'D','Z'},
				{'D','Y'},
				{'D','X'},
				{'D','L'},
				{'C','Y'},
				{'C','P'},
				{'C','N'},
				{'C','H'},
				{'B','W'},
				{'B','R'},
				{'A','Y'},
				{'A','W'},
				{'A','V'},
				{'A','P'},
				{'A','O'},
				{'A','K'},
				{'A','H'},
				{'A','G'}
		};

		for (int i=0; i < steps.length; i++) {
			char[] step = steps[i];
			char cStart = step[0];

			char cEnd = step[1];
			NodeAoc nStart = null;
			NodeAoc nEnd = null;

			if (seenNodes.containsKey(cStart)) {
				nStart = seenNodes.get(cStart);
			} else {
				nStart = new NodeAoc(cStart);
				seenNodes.put(cStart, nStart);
			}

			if (seenNodes.containsKey(cEnd)) {
				nEnd = seenNodes.get(cEnd);
			} else {
				nEnd = new NodeAoc(cEnd);
				seenNodes.put(cEnd, nEnd);
			}

			nStart.addChild(nEnd);
		}

		//find the highest priority node that is available (no parents)
		while (seenNodes.size() >0) {

			NodeAoc n = null;

			for(Map.Entry<Character,NodeAoc> entry : seenNodes.entrySet()) {
				NodeAoc currentn = entry.getValue();
				if (currentn.parents.size() == 0) {
					//this one is available
					if (n == null) {
						n = currentn;
					} else {
						if (currentn.c < n.c) {
							n = currentn;
						}
					}
				}
			}

			System.out.print(n.c);
			//loop through its children and remove itself as a parent
			for(Map.Entry<Character,NodeAoc> entry : n.children.entrySet()) {
				NodeAoc nc = entry.getValue();
				nc.parents.remove(n.c);

			}

			//remove node from seenNodes
			seenNodes.remove(n.c);
		}





	} //end MAIN

}





