import java.util.ArrayList;
import java.util.HashMap;

public class part2 {

  public static HashMap<String,Integer> hm = new HashMap<String,Integer>();
  public static void print_next_two(Clist l, HashMap<String,Integer> hm) {
    Node n = l.find(1);
    Node end = n;
    Node neighbor1 = n.next;
    Node neighbor2 = n.next.next;
    String s = neighbor1.data + " , " + neighbor2.data;
    if (!hm.containsKey(s)) {
      System.out.println(neighbor1.data + " , " + neighbor2.data);
      hm.put(s, 0);
    } else {
      int n1 = hm.get(s);
      hm.put(s, n1+1);   
    }
    
    //System.out.println(s);
  }
  
  public static void main(String[] args) {
    Clist l = new Clist();
    String s = "538914762";
    
    int maxr=1000000;
    //maxr = 1000000; //TEST
    
    System.out.println("Adding initial...");
    for (int i=0; i < s.length(); i++) {
      l.add(Integer.parseInt(s.charAt(i)+""));
    }
    
    System.out.println("Adding extra...");
    for (int r=10; r <= maxr; r++) {
      l.add(r);
    }    
    
    Node curr = l.head;
    
    int moves = 100;
    moves = maxr * 10;
    
    int move = 1;
    //print_next_two(l,hm);
    System.out.println("Entering loop...");
    for (int i=0; i < moves; i++) {
      if (move % 1000 == 0)
        System.out.println("-- move " + move + " --");
      //System.out.println("cups: " + l.toString());
      //pick up three
      ArrayList<Integer> three = new ArrayList<Integer>();
      Node new_curr = curr;
      //System.out.println("HERE 1");
      for (int j=0; j < 3; j++) {
        new_curr = new_curr.next;
        three.add(new_curr.data);
      }
      new_curr = new_curr.next;
      curr.next = new_curr;
      //System.out.println("pick up: " + three.toString());
      
      //loop through remaining cups and find min max
      ArrayList<Integer> cups = new ArrayList<Integer>();
      Node curr1 = curr;
      int max_cup = Integer.MIN_VALUE;
      int min_cup = Integer.MAX_VALUE;      
      //System.out.println("HERE 2");
      do {
        cups.add(curr1.data);
        if (curr1.data > max_cup)
          max_cup = curr1.data;
        if (curr1.data < min_cup)
          min_cup = curr1.data;
        curr1 = curr1.next;
      } while (curr1 != curr);

      // select dest cup       
      int dest_cup = curr.data - 1;
      if (dest_cup < min_cup)
        dest_cup = max_cup;
      //System.out.println("HERE 3");
      while (three.contains(dest_cup)) {
        dest_cup = dest_cup - 1;
        if (dest_cup < min_cup) {
          dest_cup = max_cup;
          break;
        }
      }
      //System.out.println("destination: " + dest_cup);
      
      //place cups
      Node dest = l.find(dest_cup);
      Node nextn = dest.next;
      Node n1 = new Node(three.get(0));
      Node n2 = new Node(three.get(1));
      Node n3 = new Node(three.get(2));
      n1.next = n2;
      n2.next = n3;
      dest.next = n1;
      n3.next = nextn;
      //System.out.println();
      curr = curr.next;
      l.head = curr;
      
      if (move == moves) {
        //System.out.println("-- final --");
        Node n = l.find(1);
        Node end = n;
        Node neighbor1 = n.next;
        Node neighbor2 = n.next.next;
        n = n.next;
        /*
        s = "";
        s = s + n.data + ' ';
        Node curr3 = n.next;
        while (curr3 != end) {
          s = s + curr3.data + ' ';
          curr3 = curr3.next;
        }
        System.out.println(s);
        */
        System.out.println("maxr: " + maxr+ "     " + neighbor1.data + " , " + neighbor2.data);
        System.out.print("Part 2: " + (neighbor1.data*neighbor2.data));
        break;
      }
      //print_next_two(l,hm);
      move++;
    }
  }

}
