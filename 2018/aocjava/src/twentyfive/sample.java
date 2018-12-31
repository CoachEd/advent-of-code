package twentyfive;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class sample {

	public static String fname = "files/25_0_a.txt";
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
		
		for (Point1 p : points) {
			System.out.println(p.toString());
		}


	}

}
