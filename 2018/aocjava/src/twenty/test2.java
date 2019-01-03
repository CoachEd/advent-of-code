package twenty;

public class test2 {

	public static void main(String[] args) {
		String s = "NNN(S)EEE|WWW";
		String[] parts = s.split("\\(|\\)|\\|");
		System.out.println(parts[0]);
		System.out.println(parts[1]);
		System.out.println(parts[2]);
		System.out.println(parts[3]);
		
	}

}

