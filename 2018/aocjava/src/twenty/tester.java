package twenty;

public class tester {

	public static void main(String[] args) {
		String smap = "AAAAA|SS";
		String[] parts = smap.split("\\(|\\)|\\|");
		System.out.println(parts.length);
		System.out.println(parts[0].length());
		

	}

}
