package nineteen;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Part2 {

	//static String fname = "files/19_0.txt"; //sample data
	static String fname = "files/19_2.txt"; //part 2 data
	static enum FUNCS {banr,muli,bori,setr,addi,eqrr,gtri,gtir,borr,eqri,bani,addr,eqir,mulr,seti,gtrr};
	static Device d = new Device();

	public static void main(String[] args) {	
		
		//Part 2 - register 0 started with value 1
		d.register[0] = 1;
		
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

		//get IP
		String s1 = al.get(0);
		String[] arr = s1.split("\\s+");
		int num = Integer.parseInt(arr[1]);
		d.ipbind = num;
		al.remove(0);

		boolean done = false;
		while (!done) {
			String s = al.get(d.ip);
			arr = s.split("\\s+");
			String cmd = arr[0].trim();
			int n1 = Integer.parseInt(arr[1].trim());
			int n2 = Integer.parseInt(arr[2].trim());
			int n3 = Integer.parseInt(arr[3].trim());
			FUNCS f = FUNCS.valueOf(cmd);
			int idx = f.ordinal(); //index into runInstruction

			//update IP register to IP value
			d.register[d.ipbind] = d.ip;
			//System.out.println("ip=" + d.ip + " " + d.register[0]);
			d.printRegisters();
			//System.out.println(cmd +" " + n1 + " " + n2 + " " + n3);
			runInstruction(idx,n1,n2,n3);
			d.ip = d.register[d.ipbind];
			d.ip = d.ip + 1;
			//d.printRegisters();
			//System.out.println();
			if (d.ip >= al.size()) done = true;
		}
		
		System.out.println("register[0] is " + d.register[0]);



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
			d.eqrr(A, B, C);
			break;		
		case 6:
			d.gtri(A, B, C);
			break;
		case 7:
			d.gtir(A, B, C);
			break;
		case 8:
			d.borr(A, B, C);
			break;
		case 9:
			d.eqri(A, B, C);
			break;
		case 10:
			d.bani(A, B, C);
			break;
		case 11:
			d.addr(A, B, C);
			break;	
		case 12:
			d.eqir(A, B, C);
			break;				
		case 13:
			d.mulr(A, B, C);
			break;
		case 14:
			d.seti(A, B, C);
			break;
		case 15:
			d.gtrr(A, B, C);
			break;	
		default:
			System.err.println("ERROR INSTRUCTION: " + i0);
		}
	}

}
