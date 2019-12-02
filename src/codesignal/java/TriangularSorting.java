package test;

public class TriangularSorting {

  public static void main(String[] args) {
    TriangularSorting t = new TriangularSorting();
    
    ListNode<Integer> list = t.createDummyList();
    ListNode<Integer> result = t.triangularSorting(list);
    while (result != null) {
      System.out.print(result.value + " ");
      result = result.next;
    }
  }
  
  class ListNode<T> {
    ListNode(T x) {
      value = x;
    }
    T value;
    ListNode<T> next;
    
    @Override
    public String toString() {
      return "ListNode [value=" + value + "]";
    }
  }

  ListNode<Integer> triangularSorting(ListNode<Integer> list) {

    int n = 0;
    int k = 0;
    
    ListNode<Integer> h = list;
    while (h != null) {
      n++;
      h = h.next;
    }
    
    k = (int) (Math.sqrt(4*n + 1) - 1) / 2;
    
    h = list;
    ListNode<Integer> resultStart = list;
    ListNode<Integer> resultEnd = null;
    ListNode<Integer> remainingListStart = null;
    for (int i = k; i >= 1; i--) {
      for (int j = 0; j < i-1; j++)
        h = h.next;
      
      ListNode<Integer> t = h.next;
      remainingListStart = t;
      for (int j = 0; j < i*(i-1) - 1; j++)
        t = t.next;
      
      h.next = t.next;
      t.next = null;
      
      while (h.next != null)
        h = h.next;
      
      resultEnd = h;
      h.next = remainingListStart;
      h = h.next;
    }
    
    return resultStart;
  }

  ListNode<Integer> createDummyList() {
    int[] x = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30};
    
    ListNode<Integer> h = new ListNode<Integer>(x[0]);
    ListNode<Integer> c = h;
    for (int i = 1; i < x.length; i++) {
      ListNode<Integer> t = new ListNode<Integer>(x[i]);
      c.next = t;
      c = c.next;
    }
    
    return h;
  }
  
}
 