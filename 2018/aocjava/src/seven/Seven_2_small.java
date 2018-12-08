
package seven;

import java.util.Map;
import java.util.TreeMap;
/*
Correct Output:
0: C(0)  
1: C(1)  
2: C(2)  
3: A(0)  F(0)  
4: B(0)  F(1)  
5: B(1)  F(2)  
6: D(0)  F(3)  
7: D(1)  F(4)  
8: D(2)  F(5)  
9: D(3)  
10: E(0)  
11: E(1)  
12: E(2)  
13: E(3)  
14: E(4)  
15: 

 */
public class Seven_2_small {

	public static void main(String[] args) {
		Map<Character,NodeAoc> seenNodes = new TreeMap<Character,NodeAoc>();
		Map<Character,NodeAoc> workers = new TreeMap<Character,NodeAoc>();
		char[][] steps = { //CHANGE!
				{'F','E'},
				{'D','E'},
				{'C','A'},
				{'C','F'},
				{'B','E'},
				{'A','B'},
				{'A','D'}
		};
		int MAX_WORKERS = 2; //CHANGE!!
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
		while (seenNodes.size() > 0 || workers.size() != 0) {
	
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
					if ((c-64+60) <= worker_timers[c]) { //MUST ADD 60 seconds!
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
			}

		
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
