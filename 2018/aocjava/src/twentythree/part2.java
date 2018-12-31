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

		ArrayList<Nanobot> nanobots = new ArrayList<Nanobot>();
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
			nanobots.add(new Nanobot(x,y,z,r));
		}
		
		int max_intersecting = Integer.MIN_VALUE;
		int maxi_index = -1;
		for (int i=0; i < nanobots.size(); i++) {
			int count_intersecting = 0;
			for (int j=0; j < nanobots.size(); j++) {
				if (i == j) continue;
				Nanobot n1 = nanobots.get(i);
				Nanobot n2 = nanobots.get(j);
				if (n1.overlaps(n2))
					count_intersecting++;
			}
			System.out.println(count_intersecting);
			if (count_intersecting > max_intersecting) {
				max_intersecting = count_intersecting;
				maxi_index = i;
			}
		}
		System.out.println("maxi_index: " + maxi_index + "   max_intersecting: " + max_intersecting);
		System.out.println(nanobots.size());





	}

}
