package nine;

public class node {
	int num;
	node next;
	node prev;
	
	public node(int n) {
		num = n;
		next = this;
		prev = this;
	}
}
