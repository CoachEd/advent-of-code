package sixteen;

public class Device {

	int[] register;
	
	public Device() {
		register = new int[]{0,0,0,0};
	}
	
	public void set(int n0, int n1, int n2, int n3) {
		register[0] = n0;
		register[1] = n1;
		register[2] = n2;
		register[3] = n3;
	}
	
	public void printRegisters() {
		System.out.println("[" + register[0] + " " + register[1] + " " + register[2] + " " + register[3] + "]");
	}
	
	public boolean equals(int n0, int n1, int n2, int n3) {
		return (register[0] == n0 && register[1] == n1 && register[2] == n2 && register[3] == n3);
	}
	
	public void addr(int A, int B, int C) {
		//addr (add register) stores into register C the result of adding register A and register B.
		register[C] = register[A] + register[B];
	}
	public void addi(int A, int B, int C) {
		//addi (add immediate) stores into register C the result of adding register A and value B.
		register[C] = register[A] + B;
	}

	public void mulr(int A, int B, int C) {
		//mulr (multiply register) stores into register C the result of multiplying register A and register B.
		register[C] = register[A] * register[B];
	}
	
	public void muli(int A, int B, int C) {
		//muli (multiply immediate) stores into register C the result of multiplying register A and value B.
		register[C] = register[A] * B;
	}

	public void banr(int A, int B, int C) {
		//banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
		register[C] = register[A] & register[B];
	}
	
	public void bani(int A, int B, int C) {
		//bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
		register[C] = register[A] & B;
	}

	public void borr(int A, int B, int C) {
		//borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
		register[C] = register[A] | register[B];
	}
	
	public void bori(int A, int B, int C) {
		//bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
		register[C] = register[A] | B;
	}

	public void setr(int A, int B, int C) {
		//setr (set register) copies the contents of register A into register C. (Input B is ignored.)
		register[C] = register[A];
	}
	
	public void seti(int A, int B, int C) {
		//seti (set immediate) stores value A into register C. (Input B is ignored.)
		register[C] = A;
	}	

	public void gtir(int A, int B, int C) {
		//gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
		register[C] = 0;
		if (A > register[B])
			register[C] = 1;
	}	
	
	public void gtri(int A, int B, int C) {
		//gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
		register[C] = 0;
		if (register[A] > B)
			register[C] = 1;
	}	
	
	public void gtrr(int A, int B, int C) {
		//gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
		register[C] = 0;
		if (register[A] > register[B])
			register[C] = 1;
	}	

	public void eqir(int A, int B, int C) {
		//eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
		register[C] = 0;
		if (A == register[B])
			register[C] = 1;
	}	
	
	public void eqri(int A, int B, int C) {
		//eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
		register[C] = 0;
		if (register[A] == B)
			register[C] = 1;
	}	
	
	public void eqrr(int A, int B, int C) {
		//eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
		register[C] = 0;
		if (register[A] == register[B])
			register[C] = 1;
	}
	
	
	public static void main(String[] args) {

		/*
		 * Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
		 */
		Device d = new Device();
		d.set(3, 2, 1, 1);
		d.printRegisters();
		d.seti(2,1,2);
		d.printRegisters();
		
		
		

	}

}
