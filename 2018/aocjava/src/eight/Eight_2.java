package eight;

import java.util.ArrayList;

public class Eight_2 {

	public static int total_metadata = 0;
	public static char[] letters = {'A','B','C','D','E'};
	public static int letter_index = 0;
	
	public static void main(String[] args) {
		String s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2";
		String[] arr = s.split(" ");
		ArrayList<Integer> al = new ArrayList<Integer>();
		for (int i=0; i < arr.length; i++) {
			int n = Integer.parseInt(arr[i]);
			al.add(n);
		}
		
		readNodes(al);
		System.out.println("Total metadata: " + total_metadata);
	}
	
	public static void readNodes(ArrayList<Integer> al) {
		if (al == null || al.size() == 0)
			return;
		
		int num_children = al.remove(0);
		int num_metadata = al.remove(0);
		char c = letters[letter_index++];
		
		if (num_children != 0) {
			for (int i=0; i < num_children; i++) {
				readNodes(al);
			}
		}
		
		//print metadata
		int node_meta_sum = 0;
		for (int j=0; j < num_metadata; j++) {
			int n = al.remove(0);
			total_metadata += n;
			node_meta_sum += n;
		}
		
		System.out.println(c + " total metadata: " + node_meta_sum);
		
	}

}
