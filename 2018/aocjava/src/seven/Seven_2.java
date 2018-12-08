
package seven;

import java.util.Map;
import java.util.TreeMap;

public class Seven_2 {

	//try1: 224 (wrong)
	//try2: 223 (wrong)
	//try3: 225 (wrong)
	//try4: 1120 (correct!)
	
	public static void main(String[] args) {
		Map<Character,NodeAoc> seenNodes = new TreeMap<Character,NodeAoc>();
		Map<Character,NodeAoc> workers = new TreeMap<Character,NodeAoc>();
		char[][] steps = { //CHANGE!
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
		int MAX_WORKERS = 5; //CHANGE!!
		int[] worker_timers = new int[100];

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
		//done adding

		int second = 0;
		while (seenNodes.size() > 0 || workers.size() > 0) {
	
			//find candidates
			String sAvailable = "";
			for(Map.Entry<Character,NodeAoc> entry : seenNodes.entrySet()) {
				NodeAoc currentn = entry.getValue();
				if (currentn.parents.size() == 0) {
					//this node has no parents
					sAvailable += currentn.c;
				}
			}
			
			//try to add each available candidate to a worker
			int k=0;
			while (workers.size() < MAX_WORKERS && k < sAvailable.length()) {
				char c = sAvailable.charAt(k);
				NodeAoc thenode = seenNodes.get(c);
				workers.put(c, thenode);
				seenNodes.remove(c);
				worker_timers[c] = 0;
				k++;
			}
			
			//see if any workers done
			boolean changed = false;
			do {
				changed = false;
				for(Map.Entry<Character,NodeAoc> entry : workers.entrySet()) {
					NodeAoc currentn = entry.getValue();
					char c = currentn.c;
					if ((c-64+60) <= worker_timers[c]) { //OMG!  just had to add 60 here!!!
						//done
						//System.out.print(c); //GOOD!
						worker_timers[c] = 0;
						//loop through its children and remove itself as a parent
						for(Map.Entry<Character,NodeAoc> entry2 : currentn.children.entrySet()) {
							NodeAoc nc = entry2.getValue();
							nc.parents.remove(currentn.c);
						}

						workers.remove(c);
						changed = true;
						break;
					}
				}
			} while (changed);

			//workers available. try to assign some
			if (workers.size() < MAX_WORKERS) {
				sAvailable = "";
				for(Map.Entry<Character,NodeAoc> entry : seenNodes.entrySet()) {
					NodeAoc currentn = entry.getValue();
					if (currentn.parents.size() == 0) {
						//this node has no parents
						sAvailable += currentn.c;
					}
				}
				//try to add each available to a worker
				k=0;
				while (workers.size() < MAX_WORKERS && k < sAvailable.length()) {
					char c = sAvailable.charAt(k);
					NodeAoc thenode = seenNodes.get(c);
					workers.put(c, thenode);
					worker_timers[c] = 0;
					seenNodes.remove(c);
					k++;
				}
			} //HERE
		
			printWorkers(workers,worker_timers, second);

			for (int i=0; i < worker_timers.length; i++) {
				worker_timers[i] = worker_timers[i] + 1;
			}
			second++;
		}

		System.out.println();
		System.out.println((second-1) + " seconds");
	} //end MAIN

	public static void printWorkers(Map<Character,NodeAoc> w, int[]timers, int second) {
		//print workers
		System.out.print(second +": ");
		for(Map.Entry<Character,NodeAoc> entry : w.entrySet()) {
			NodeAoc currentn = entry.getValue();
			System.out.print(currentn.c+ "(" + timers[currentn.c] + ")  ");
		}
		System.out.println();
	}
	
}
