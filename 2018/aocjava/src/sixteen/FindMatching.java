package sixteen;

public class FindMatching {

	public static void main(String[] args) {
		String[] arr5 = {"gtir" , "gtri" , "gtrr" , "eqir" , "eqri" , "eqrr"};
		String[] arr6 = {"gtir", "gtri" ,"gtrr"}; 
		String[] arr7 = {"gtir" , "eqrr"};
		String[] arr9 = {"gtir" ,"eqir", "gtrr", "eqri"};
		String[] arr12 = {"gtrr", "eqir" ,"eqri" ,"eqrr"};
		String[] arr15 = {"gtir" ,"gtrr", "eqri", "eqrr"};

		for (int i=0; i < arr5.length; i++) {
			String s1 = arr5[i];
			for (int j=0; j < arr6.length; j++) {
				String s2 = arr6[j];
				if (s2.equals(s1)) continue;
				for (int k=0; k < arr7.length; k++) {
					String s3 = arr7[k];
					if (s3.equals(s2) || s3.equals(s1)) continue;
					for (int l=0; l < arr9.length; l++) {
						String s4 = arr9[l];
						if (s4.equals(s3) || s4.equals(s2) || s4.equals(s1)) continue;
						for (int m=0; m < arr12.length; m++) {
							String s5 = arr12[m];
							if (s5.equals(s4) || s5.equals(s3) || s5.equals(s2) || s5.equals(s1)) continue;
							for (int n=0; n < arr15.length; n++) {
								String s6 = arr15[n];
								if (s6.equals(s5) || s6.equals(s4) || s6.equals(s3) || s6.equals(s2) || s6.equals(s1)) continue;
								System.out.println("5,6,7,9,12,15: " + s1 + "," + s2 + "," + s3 + "," + s4 + "," + s5 + "," + s6);
							} 
						}  
					}  
				}  
			} 
		}

	}

}
