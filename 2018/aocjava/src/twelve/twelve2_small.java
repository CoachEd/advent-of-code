package twelve;

import java.util.ArrayList;
import java.util.HashMap;

//INCORRECT: 1741
public class twelve2_small {

	public static void main(String[] args) {
		HashMap<String,Boolean> hm = new HashMap<String,Boolean>();
		hm.put("...##",true);
		hm.put("..#..",true);
		hm.put(".#...",true);
		hm.put(".#.#.",true);
		hm.put(".#.##",true);
		hm.put(".##..",true);
		hm.put(".####",true);
		hm.put("#.#.#",true);
		hm.put("#.###",true);
		hm.put("##.#.",true);
		hm.put("##.##",true);
		hm.put("###..",true);
		hm.put("###.#",true);
		hm.put("####.",true);
		
		String s = "#..#.#..##......###...###";

		ArrayList<pot> pots = new ArrayList<pot>();
		int MAXPOTS = 50;
		for (int i=-MAXPOTS; i < MAXPOTS; i++) {
			pot p = new pot(i,'.');
			pots.add(p);
		}

		//add plants
		int curr = MAXPOTS; //plant 0 index
		for (int i=0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == '#')
				pots.get(curr).c = c;
			curr++;
		}

		int sum = 0;
		for (long g=0; g < 21l; g++) {
			//print out current generation

			System.out.printf("%11d:  ",g);
			String s1 = "";
			sum = 0;
			for (pot p : pots) {
				s1 = s1 + p.c;
				if (p.c == '#')
					sum += p.num;
			}
			System.out.printf("%s  %d\n",s1,sum);

			//create next generation of pots
			ArrayList<pot> newpots = new ArrayList<pot>();
			for (int i=-MAXPOTS; i < MAXPOTS; i++) {
				pot p = new pot(i,'.');
				newpots.add(p);
			}

			//skip first 5 and last 5 pots, which we make empty anyway
			for (int p=5; p < pots.size()-5; p++) {

				String pattern = "";
				for (int i=p-2; i <= p+2; i++) {
					pattern = pattern + pots.get(i).c;
				}

				if (hm.containsKey(pattern)) {
					if (hm.get(pattern))
						newpots.get(p).c = '#';
					else
						newpots.get(p).c = '.';
				}
			}

			//set the next generation to the current one
			pots = newpots;
		}


		System.out.println(sum);

	}

}
