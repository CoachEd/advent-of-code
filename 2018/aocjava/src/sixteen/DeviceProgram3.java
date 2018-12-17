package sixteen;
/*
//ORIGINAL
0:  banr*
1:  muli*
2:  bori*
3:  setr*
4:  addi*
5:  (eqri eqrr gtrr) 
6:  gtri*
7:  gtir*
8:  borr*
9:  eqir*
10: bani*
11: addr*
12: (eqri eqrr gtrr)
13: mulr*
14: seti*
15: (eqri eqrr gtrr)
 */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

//WRONG: 365, 390, 353 (too low), 362, 354, 372, 364, 355, 373
//CORRECT: 
public class DeviceProgram3 {

	static HashMap<String,Integer> hmCounts = new HashMap<String,Integer>();
	static Device d;
	static int count_samples = 0;

	public static void main(String[] args) {
		String fname = "/Users/ertorres/github/advent-of-code/2018/aocjava/src/sixteen/input3.txt";

		d = new Device();

		try (BufferedReader br = new BufferedReader(new FileReader(fname))) {
			String line;
			int i0=0, A=0, B=0, C=0; //instruction
			while ((line = br.readLine()) != null) {
				String [] arr = null;
				arr = line.split("\\s+");
				i0 = Integer.parseInt(arr[0]);
				A = Integer.parseInt(arr[1]);
				B = Integer.parseInt(arr[2]);
				C = Integer.parseInt(arr[3]);
				System.out.println("Running " + i0 + " " + A + " " + B + " " + C);
				runInstruction(i0,A,B,C);
			}
			d.printRegisters();

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void runInstruction(int i0, int A, int B, int C) {

		switch(i0) {
		case 0:
			d.banr(A, B, C);
			break;
		case 1:
			d.muli(A, B, C);
			break;
		case 2:
			d.bori(A, B, C);
			break;
		case 3:
			d.setr(A, B, C);
			break;
		case 4:
			d.addi(A, B, C);
			break;
			
			
		case 5:
			d.gtrr(A, B, C);
			break;		
		case 9:
			d.eqir(A, B, C);
			break;
		case 12:
			d.eqri(A, B, C);
			break;				
		case 7:
			d.gtir(A, B, C);
			break;
		case 15:
			d.eqrr(A, B, C);
			break;				
			
			
		case 6:
			d.gtri(A, B, C);
			break;
		case 8:
			d.borr(A, B, C);
			break;
		case 10:
			d.bani(A, B, C);
			break;
		case 11:
			d.addr(A, B, C);
			break;	
		case 13:
			d.mulr(A, B, C);
			break;
		case 14:
			d.seti(A, B, C);
			break;
		
		default:
			System.err.println("ERROR INSTRUCTION: " + i0);
		}




	}

}
