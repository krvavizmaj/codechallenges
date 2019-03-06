import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Subprnjl {
  
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int t = Integer.parseInt(line);
    
    for (int i = 0; i < t; i++) {
      line = in.readLine();
      String[] lineParts = line.split(" ");
      int n = Integer.parseInt(lineParts[0]);
      int k = Integer.parseInt(lineParts[1]);
      
      line = in.readLine();
      lineParts = line.split(" ");
      int[] a = new int[n];
      for (int ai = 0; ai < n; ai++) a[ai] = Integer.parseInt(lineParts[ai]);
      
      int res = 0;
      for (int start = 0; start < n; start++) {
        List<Integer> subArray = new ArrayList<>(n);
        int[] occurances = new int[2001];
        
        for (int end = start; end < n; end++) {
          insertElementInArray(subArray, a[end]);
          occurances[a[end]]++;
          
          int l = end - start + 1;
          int m = (int) Math.ceil((double)k / (double)l);
          int xi = (k - 1) / m;
          int x = subArray.get(xi);
          int f = occurances[x];
          if (f < 2001 && occurances[f] > 0) {
            res++;
          }
        }
      }
      System.out.println(res);
    }
    
    in.close();
  }
  
  static void insertElementInArray(List<Integer> array, int element) {
    int startIndex = 0;
    int endIndex = array.size() - 1;
    
    int middle = 0;
    while (endIndex - startIndex > 0) {
      middle = (startIndex + endIndex) / 2;
      if (array.get(middle) > element) {
        endIndex = middle;
      } else {
        startIndex = middle + 1;
      }
    }
    
    if (array.size() > startIndex && array.get(startIndex) < element) startIndex++;
    array.add(startIndex, element);
  }

}
