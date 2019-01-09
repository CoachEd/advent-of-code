package twentythree;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class part2 {

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

		ArrayList<Nanobot2> nanobots = new ArrayList<Nanobot2>();
		for (String s : al) {
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
			nanobots.add(new Nanobot2(x,y,z,r));
		}

		Nanobot2 center = new Nanobot2(0,0,0,1);
		//long max_radius = 1000000000l;
		long max_radius = 291735893;
		long r = 291735892;
		long maxcounts = Integer.MIN_VALUE;
		long maxr = -1;
		while (r < max_radius) {
			center.r = r;
			int count = 0;
			for (Nanobot2 nb : nanobots) {
				long dist = nb.mdist(center);
				if (dist <= center.r) {
					count++;
				}
			}
			
			if (count > maxcounts) {
				maxcounts = count;
				maxr = r;
			}
			
			r+= 1;
		}

		System.out.println("radius is: " + maxr + "   counts: " + maxcounts);
//TOO HIGH: 291735892





	}

}
