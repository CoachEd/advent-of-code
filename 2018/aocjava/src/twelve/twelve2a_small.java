package twelve;

import java.util.ArrayList;
import java.util.HashMap;

public class twelve2a_small {

	/* OMG OMG OMG!!! THIS IS CORRECT NOW!
	...
	12500  449458
	13000  467458
	13500  485458
	14000  503458
	14500  521458
	15000  539458
	15500  557458
	16000  575458
	16500  593458
	17000  611458
	...
	At 20000, count is 719458.
	Then, it always adds 18000 for each 500, so...
	50 000 000 000 - 20000 = 49999980000

	49999980000 / 500 = 99999960

	99999960 * 18000 = 1799999280000

	1799999280000 + the previous amount (719458)
	= 1799999999458 
	*/
	
	public static void main(String[] args) {
		HashMap<String,Boolean> hm = new HashMap<String,Boolean>();
		
		
		//hm.put("##...",false);
		//hm.put("##.##",false);
		hm.put(".#.#.",true);
		//hm.put("#..#.",false);
		hm.put("#.###",true);
		//hm.put(".###.",false);
		//hm.put("#.#..",false);
		//hm.put("##..#",false);
		//hm.put(".....",false);
		//hm.put("...#.",false);
		//hm.put(".#..#",false);
		hm.put("####.",true);
		hm.put("...##",true);
		hm.put("..###",true);
		hm.put("#.#.#",true);
		hm.put("###.#",true);
		hm.put("#...#",true);
		//hm.put("..#.#",false);
		hm.put(".##..",true);
		hm.put(".#...",true);
		hm.put(".##.#",true);
		//hm.put(".####",false);
		//hm.put(".#.##",false);
		//hm.put("..##.",false);
		//hm.put("##.#.",false);
		//hm.put("#.##.",false);
		//hm.put("#..##",false);
		//hm.put("###..",false);
		//hm.put("....#",false);
		hm.put("#####",true);
		//hm.put("#....",false);
		hm.put("..#..",true);
		String s = "#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............";
		long generations = 50000000000l;
		
		/*
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
		long generations = 20l + 1;
		*/
		
		
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
		for (long g=0; g < generations; g++) {

			//print out current generation
			//System.out.printf("%2d:  ",g);
			String s1 = "";
			sum = 0;
			for (pot p : pots) {
				s1 = s1 + p.c;
				if (p.c == '#')
					sum += p.num;
			}
			
			if (g % 500 == 0) {
				//System.out.printf("%s  %d\n",s1,sum);
				System.out.printf("%d  %d\n",g,sum);
			}

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
