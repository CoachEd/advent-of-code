class Clist {
  Node head = null;
  Node tail = null;
  
  public Clist() {
    head = null;
  }
  
  //add to end of list
  public void add(int n) {
    Node node = new Node(n);
    if (head == null) {
      head = node;
      node.next = node;
      tail = node;
    } else {
      Node curr = tail.next;
      tail.next = node;
      node.next = curr;
      tail = node;
    }
  }  
  
  public Node find(int n) {
    Node curr = head;
    while (curr.data != n)
      curr = curr.next;
    return curr;
  }
  
  public String toString() {
    String s = "";
    Node curr = head;
    s = s + head.data + ' ';
    curr = curr.next;
    while (curr != head) {
      s = s + curr.data+ ' ';
      curr = curr.next;
    }
    return s;
  }
  
}