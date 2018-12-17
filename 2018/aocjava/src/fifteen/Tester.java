package fifteen;

public class Tester {

	public static void main(String[] args) {

		Coord c2 = new Coord(0,1);
		int row=0;
        int col=2;
		if (c2.row < row) {
			row = c2.row;
			col = c2.col;
		} else if (c2.row == row) {
			if (c2.col < col) {
				row = c2.row;
				col = c2.col;
			}
		}
		
		System.out.println(row + "," + col);

	}

}
