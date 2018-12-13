package twelve;

import java.util.ArrayList;
import java.util.HashMap;

public class twelve1a_small {

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
		for (int i=0; i < s.length(); i++) {
			pot p = new pot(i,'.');
			pots.add(p);
		}

		//add plants
		for (int i=0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == '#')
				pots.get(i).c = c;
		}

		int sum = 0;
		for (int g=0; g < 21; g++) {

			//print out current generation
			System.out.printf("%2d:  ",g);
			String s1 = "";
			sum = 0;
			for (pot p : pots) {
				s1 = s1 + p.c;
				if (p.c == '#')
					sum += p.num;
			}
			System.out.printf("%s  %d\n",s1,sum);

			int findex = pots.get(0).num;
			int lindex = pots.get(pots.size()-1).num;
			if (!s1.startsWith(".....")) {
				//add two
				pots.add(0, new pot(findex-1,'.'));
				pots.add(0, new pot(findex-2,'.'));
				pots.add(0, new pot(findex-3,'.'));
				pots.add(0, new pot(findex-4,'.'));
				pots.add(0, new pot(findex-5,'.'));
			}

			if (!s1.endsWith(".....")) {
				//add two
				pots.add(new pot(lindex+1,'.'));
				pots.add(new pot(lindex+2,'.'));
				pots.add(new pot(lindex+3,'.'));
				pots.add(new pot(lindex+4,'.'));
				pots.add(new pot(lindex+5,'.'));
			} 

			//create next generation of pots
			ArrayList<pot> newpots = new ArrayList<pot>();
			for (int i=0; i < pots.size(); i++) {
				pot p = new pot(pots.get(i).num,'.');
				newpots.add(p);
			}

			//skip first 2 and last 2 pots, which we make empty anyway
			for (int p=2; p < pots.size()-2; p++) {

				String pattern = "";
				for (int i=p-2; i <= p+2; i++) {
					pattern = pattern + pots.get(i).c;
				}

				if (hm.containsKey(pattern)) {
					newpots.get(p).c = '#';
				}
			}

			//set the next generation to the current one
			pots = newpots;
		}


		System.out.println(sum);


	}

}
