package sixteen;
/*
//ORIGINAL
0:  banr*
1:  muli*
2:  bori*
3:  setr*
4:  addi*
5:  (eqir eqri eqrr gtir gtri gtrr)
6:  (               gtir gtri gtrr)
7:  (          eqrr gtir          )
8:  borr*
9:  (eqir eqri      gtir      gtrr) 
10: bani*
11: addr*
12: (eqir eqri eqrr           gtrr)
13: mulr*
14: seti*
15: (     eqri eqrr gtir      gtrr)

//looked at 5/12/15 WRONG
//          5/9/15 WRONG
//          5/9/12 ?
 */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

//WRONG: 188, 4116, 669 (too high)
//CORRECT: 493
public class DeviceProgram2 {

	static HashMap<String,Integer> hmCounts = new HashMap<String,Integer>();
	static Device d;
	static int count_samples = 0;

	public static void main(String[] args) {
		String fname = "files/input1.txt";
		/*
		FORMAT: registers before, instruction, registers after
		3 0 1 3
		15 2 1 3
		3 0 1 1

		1 3 2 0
		11 2 2 0
		4 3 2 0
		...
		 */

		d = new Device();

		try (BufferedReader br = new BufferedReader(new FileReader(fname))) {
			String line;
			int i=0;
			int n0=0, n1=0, n2=0, n3=0;
			int b0=0, b1=0, b2=0, b3=0; //before
			int i0=0, A=0, B=0, C=0; //instruction
			int a0=0, a1=0, a2=0, a3=0; //after
			while ((line = br.readLine()) != null) {
				String [] arr = null;
				if (line.trim().length() == 0)
					continue;

				if (i != 3) {
					arr = line.split("\\s+");
					n0 = Integer.parseInt(arr[0]);
					n1 = Integer.parseInt(arr[1]);
					n2 = Integer.parseInt(arr[2]);
					n3 = Integer.parseInt(arr[3]);
				}

				if (i == 0) {
					//before registers
					b0 = n0;
					b1 = n1;
					b2 = n2;
					b3 = n3;
					i++;
				} else if (i == 1) {
					//instruction
					i0 = n0;
					A = n1;
					B = n2;
					C = n3;
					i++;
				} else if (i == 2) {
					//after registers
					a0 = n0;
					a1 = n1;
					a2 = n2;
					a3 = n3;
					//blank line; execute instruction and compare
					runOperations(b0, b1, b2, b3,i0, A, B, C, a0, a1, a2, a3);


					i = 0;
				}
			}

			/*
			String s = "";
			for (Map.Entry<String, Integer> entry : hmCounts.entrySet()) {
				String opcode = entry.getKey();
				int count = entry.getValue();
				if (count <= 2)
					System.out.println(opcode + ": " + count);
					s = s + " " + opcode + " ";
			}
			System.out.println("count_samples: " + count_samples);
			System.out.println(s);
			*/

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void runOperations(int b0, int b1, int b2, int b3,int i0, int A, int B, int C, int a0, int a1, int a2, int a3) {

		String op = "|"+i0+"|"+A+"|"+B+"|"+C+"|";
		String sOp = "";
	
		int temp_count = 0;
		if (!hmCounts.containsKey(op))
			hmCounts.put(op, 0);

		d.set(b0,b1,b2,b3);
		d.addr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "addr"+ " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}

		d.set(b0,b1,b2,b3);
		d.addi(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "addi" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}

		d.set(b0,b1,b2,b3);
		d.mulr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "mulr" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}

		d.set(b0,b1,b2,b3);
		d.muli(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "muli" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}		

		d.set(b0,b1,b2,b3);
		d.banr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "banr" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}		

		d.set(b0,b1,b2,b3);
		d.bani(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "bani" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}		

		d.set(b0,b1,b2,b3);
		d.borr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "borr" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}		

		d.set(b0,b1,b2,b3);
		d.bori(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "bori" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}			

		d.set(b0,b1,b2,b3);
		d.setr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "setr" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}			

		d.set(b0,b1,b2,b3);
		d.seti(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "seti" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}				

		d.set(b0,b1,b2,b3);
		d.gtir(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "gtir" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}				

		d.set(b0,b1,b2,b3);
		d.gtri(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "gtri" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}				

		d.set(b0,b1,b2,b3);
		d.gtrr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "gtrr" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}				

		d.set(b0,b1,b2,b3);
		d.eqir(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "eqir" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}				

		d.set(b0,b1,b2,b3);
		d.eqri(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "eqri" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}				

		d.set(b0,b1,b2,b3);
		d.eqrr(A, B, C);
		if (d.equals(a0,a1,a2,a3)) { 
			sOp += "eqrr" + " ";
			hmCounts.put(op, hmCounts.get(op)+1); temp_count++;
		}

		if (op.startsWith("|15|")) {
		
			System.out.println(op + ":  " + sOp);
		}
	}

}
