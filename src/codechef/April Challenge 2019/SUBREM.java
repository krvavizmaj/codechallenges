package april.challenge.y2019;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class SUBREM {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int cases = Integer.parseInt(line);
    
    for (int t = 0; t < cases; t++) {
      line = in.readLine();
      int n = Integer.parseInt(line.split(" ")[0]);
      long x = Integer.parseInt(line.split(" ")[1]);

      long[] a = new long[n];
      line = in.readLine();
      String[] aList = line.split(" ");
      for (int i = 0; i < n; i++) {
        a[i] = Integer.parseInt(aList[i]);
      }
      
      List<Integer>[] edges = new List[n];
      List<Integer>[] children = new List[n];
      for (int i = 0; i < n; i++) {
        edges[i] = new ArrayList<>();
        children[i] = new ArrayList<>();
      }
      for (int i = 0; i < n-1; i++) {
        line = in.readLine();
        int u = Integer.parseInt(line.split(" ")[0]) - 1;
        int v = Integer.parseInt(line.split(" ")[1]) - 1;
        edges[u].add(v);
        edges[v].add(u);
      }
      
      boolean[] visited = new boolean[n]; 
      Deque<Integer> q = new ArrayDeque<>();
      q.add(0);
      while (!q.isEmpty()) {
        int root = q.pop();
        visited[root] = true;
        for (int e : edges[root]) {
          if (!visited[e]) {
            children[root].add(e);
            q.add(e);
          }
        }
      }
      
      long[] subtreeSum = new long[n];
      boolean[] canBeRemoved = new boolean[n];
      long[] removedChildren = new long[n];
      long[] removedAmount = new long[n];
      collectRemoveCandidates(0, x, canBeRemoved, a, children, subtreeSum, removedChildren, removedAmount);
      
      long result = subtreeSum[0] - removedAmount[0] - x*removedChildren[0];

      System.out.println(result);
    }
    
    in.close();
  }
  
  static void collectRemoveCandidates(
      int root, 
      long x, 
      boolean[] canBeRemoved, 
      long[] a, 
      List<Integer>[] children, 
      long[] subtreeSum,
      long[] removedChildren,
      long[] removedAmount) {
    
    subtreeSum[root] = a[root];
    if (children[root].size() == 0) {
      if (a[root] < -x) {
        canBeRemoved[root] = true;
        removedChildren[root] = 1;
        removedAmount[root] = a[root];
      }
    } else {
      for (int child : children[root]) {
        collectRemoveCandidates(child, x, canBeRemoved, a, children, subtreeSum, removedChildren, removedAmount);
        
        subtreeSum[root] += subtreeSum[child];
        removedChildren[root] += removedChildren[child];
        removedAmount[root] += removedAmount[child];
      }
      
      if (subtreeSum[root] - removedAmount[root] - x*removedChildren[root] < -x) {
        canBeRemoved[root] = true;
        removedChildren[root] = 1;
        removedAmount[root] = subtreeSum[root];
      }
    }
  }
  
}
