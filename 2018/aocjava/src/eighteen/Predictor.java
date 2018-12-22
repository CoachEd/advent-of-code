package eighteen;

public class Predictor {
	//1000000000
	/*Here is the sequence, it repeats...
0 t=10000    combo: 614|359
1 t=20000    combo: 561|372
2 t=30000    combo: 536|329
3 t=40000    combo: 546|314
4 t=50000    combo: 572|316***
5 t=60000    combo: 597|333
6 t=70000    combo: 607|352
	 */
	public static void main(String[] args) {
		int[] arr = {0,1,2,3,4,5,6};
		int cnt = 0;
		for (int i=10000; i <= 1000000000; i+= 10000) {

			if (i > 900000000)
				System.out.println(cnt + ": " + i);
			cnt++;
			if (cnt >6)
				cnt = 0;
		}

		
		int ans = 572 * 316;
		System.out.println("answer: " + ans);
		
	}

}
