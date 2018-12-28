package twenty;
//NEEDS WORK. THIS IS HARD.
public class part0 {

	public static void main(String[] args) {
		String s = "^ENWWW(NEEE|SSE(EE|N))$";
		s = s.substring(1,s.length()-1);
		parseit(s);
	}


	public static void parseit(String s) {
		if (s == null || s.length() == 0 || s.charAt(0) == ')')
			return;
		int startparen = s.indexOf('(');
		int pipe = s.indexOf('|');
		int pos = -1;
		if (pipe == -1 && startparen == -1) {
			System.out.print(s);
			return;
		} else if (pipe == -1) {
			pos = startparen;
		} else if (startparen == -1) {
			pos = pipe;
		} else if (pipe < startparen) {
			pos = pipe;
		} else {
			pos = startparen;
		}
		System.out.print(s.substring(0, pos));
		parseit(s.substring(pos+1));
	}

}

