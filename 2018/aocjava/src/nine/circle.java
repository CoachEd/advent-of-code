package nine;

public class circle {
	node currmarble;
	node nodezero;
	int length;
	int currplayer;
	long[] scores;
	int num_players;

	public circle(int numplayers) {
		currmarble = null;
		nodezero = null;
		length = 0;
		currplayer = -1;
		num_players = numplayers;
		scores = new long[num_players+1];
	}

	public void insert(node n) {
		currplayer++;
		if (currplayer > num_players)
			currplayer = 1;
		if (n == null) return;
		if (length == 0) {
			n.next = n;
			n.prev = n;
			nodezero = n;
		} else if (length == 1) {
			currmarble.prev = n;
			currmarble.next = n;
			n.prev = currmarble;
			n.next = currmarble;
		} else if (length == 2) {
			//insert before
			insertAfter(n,currmarble.prev);
		} else {
			//list is length three or more
			if (n.num % 23 == 0) {
				//find 7th marble ccw
				node ccw = currmarble;
				for (int i=0; i < 7; i++)
					ccw = ccw.prev;
				currmarble = ccw.next;
				int num = deleteNode(ccw);
				scores[currplayer] = scores[currplayer] + num + n.num;
				length--;
				return;
			} else {
				insertAfter(n,currmarble.next);
			}
		}

		currmarble = n;
		length++;
		return;
	}

	public void printCircle() {
		String player;
		if (length == 1)
			player = "-";
		else {
			player = currplayer + "";
		}
		node n = nodezero;
		System.out.print("[" + player + "] ");
		for (int i=0; i < length; i++) {
			if (n == currmarble)
				System.out.print("(" + n.num + ") ");
			else
				System.out.print(n.num + " ");
			n = n.next;
		}
		System.out.println();
	}

	public void insertAfter(node n1, node n2) {
		//insert n1 after n2
		if (n1 == null || n2 == null) return;
		node temp = n2.next;
		n2.next = n1;
		n1.next = temp;
		temp.prev = n1;
		n1.prev = n2;
	}

	public int deleteNode(node n) {
		if (n == null)
			return 0;
		node prev = n.prev;
		node next = n.next;
		prev.next = next;
		next.prev = prev;
		n.next = n;
		n.prev = n;
		return n.num;
	}
}
