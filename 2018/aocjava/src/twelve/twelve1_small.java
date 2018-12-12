package twelve;

import java.util.ArrayList;
import java.util.HashMap;

public class twelve1_small {

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
		for (int g=0; g < 21; g++) {
			
			//print out current generation
			System.out.printf("%2d:  ",g);
			String s1 = "";
			sum = 0;
			for (pot p : pots) {
				if (p.num >= -3 && p.num <= 35) {
					s1 = s1 + p.c;
					if (p.c == '#')
						sum += p.num;
				}
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
					newpots.get(p).c = '#';
				}
			}
			
			//set the next generation to the current one
			pots = newpots;
		}


		System.out.println(sum);


	}

}
