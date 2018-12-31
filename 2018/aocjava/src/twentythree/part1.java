package twentythree;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class part1 {

	public static String fname = "files/23_1.txt";
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

		ArrayList<Nanobot> nanobots = new ArrayList<Nanobot>();
		int max_radius = Integer.MIN_VALUE;
		int max_idx = 0;
		int idx = -1;
		for (String s : al) {
			idx++;
			String[] arr = s.split("\\s+");
			String pos = arr[0];
			int id1 = pos.indexOf('<');
			int id2 = pos.indexOf('>');
			pos = pos.substring(id1+1,id2);
			String[] arr2 = pos.split(",");
			int x = Integer.parseInt(arr2[0]);
			int y = Integer.parseInt(arr2[1]);
			int z = Integer.parseInt(arr2[2]);
			String sRadius = arr[1];
			int id3 = sRadius.indexOf('=');
			sRadius = sRadius.trim().substring(id3+1);
			int r = Integer.parseInt(sRadius);
			if (r > max_radius) {
				max_radius = r;
				max_idx = idx;
			}
			nanobots.add(new Nanobot(x,y,z,r));
		}
		
		Nanobot maxnanobot = nanobots.get(max_idx);
		System.out.println("Max nanobot: " + maxnanobot.toString());
		
		int numbots = 0;
		for (Nanobot nb : nanobots) {
			int dist = nb.mdist(maxnanobot);
			if (dist <= maxnanobot.r) {
				//System.out.println(nb.toString());
				numbots++;
			}
		}
		System.out.println(numbots);





	}

}
