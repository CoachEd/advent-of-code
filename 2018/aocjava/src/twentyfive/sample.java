package twentyfive;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class sample {

	public static String fname = "files/25_1.txt";
	public static void main(String[] args) {

		ArrayList<String> al = new ArrayList<String>();
		try (BufferedReader br = new BufferedReader(new FileReader(fname))) {
			String line;
			while ((line = br.readLine()) != null) {
				al.add(line);
			}
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		ArrayList<Point1> points = new ArrayList<Point1>();
		for (String s : al) {
			String[] arr = s.split(",");
			int w = Integer.parseInt(arr[0].trim());
			int x = Integer.parseInt(arr[1].trim());
			int y = Integer.parseInt(arr[2].trim());
			int z = Integer.parseInt(arr[3].trim());
			points.add(new Point1(w,x,y,z));
		}

		ArrayList<ArrayList<Point1>> constellations = new ArrayList<ArrayList<Point1>>();
		for (int i=0; i < points.size(); i++) {
			if (constellations.size() == 0) {
				ArrayList<Point1> tempal = new ArrayList<Point1>();
				tempal.add(points.get(i));
				constellations.add(tempal);
			} else {
				Point1 p1 = points.get(i);
				boolean found = false;
				for (int j=0; j < constellations.size(); j++) {
					for (Point1 p2 : constellations.get(j)) {
						if (p1.mdist(p2) <= 3) {
							found = true;
							constellations.get(j).add(p1);
							break;
						}
					}
					if (found)
						break;
				}
				if (!found) {
					ArrayList<Point1> tempal = new ArrayList<Point1>();
					tempal.add(p1);
					constellations.add(tempal);
				}
			}
		}

		boolean changed = true;
		while (changed) {
			//check if constellations can touch each other
			changed = false;
			boolean constellations_touch = false;
			for (int k=0; k < constellations.size()-1; k++) {
				for (int l=k+1; l < constellations.size(); l++) {
					ArrayList<Point1> c1 = constellations.get(k);
					ArrayList<Point1> c2 = constellations.get(l);
					constellations_touch = false;
					for (Point1 p1 : c1) {
						for (Point1 p2 : c2) {
							if (p1.mdist(p2) <= 3) {
								constellations_touch = true;
								break;
							}
						}
						if (constellations_touch) break;
					}
					if (constellations_touch) {
						changed = true;
						ArrayList<Point1> altemp = new ArrayList<Point1>();
						altemp.addAll(c1);
						altemp.addAll(c2);
						constellations.remove(c1);
						constellations.remove(c2);
						constellations.add(altemp);
						break;
					}				
				}
				if (constellations_touch) break;
			}
		}

		//print out constellations
		String s = "";
		for (ArrayList<Point1> c : constellations) {
			for (Point1 p : c) {
				s += p.toString() + "  ";
			}
			s += "\n";
		}
		s += "Constellations: " + constellations.size();
		System.out.println(s);
		//GUESSES: 616 (too high), 612 (too high), 272 (too low), 350 (CORRECT!)

	}

}
