package fifteen;

//for the Elf and Goblin players
public class Player {
	
	char c;
	int row;
	int col;
	int hp;
	
	public Player(char c1, int row1, int col1) {
		c = c1;
		row = row1;
		col = col1;
		hp = 200;
	}
	
	public void swap(Player p) {
		char tc = p.c;
		int trow = p.row;
		int tcol = p.col;
		int thp = p.hp;

		p.c = c;
		p.row = row;
		p.col = col;
		p.hp = hp;
		
		c = tc;
		row = trow;
		col = tcol;
		hp = thp;
	}

	
	
}
