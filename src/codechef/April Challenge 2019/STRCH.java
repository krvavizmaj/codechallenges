package april.challenge.y2019;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class STRCH {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int cases = Integer.parseInt(line);
    
    for (int t = 0; t < cases; t++) {
      line = in.readLine();
      int n = Integer.parseInt(line);
      line = in.readLine();
      String s = line.split(" ")[0];
      String c = line.split(" ")[1];
      
      long result = 0;
      int lastc = -1;
      for (int i = 0; i < n; i++) {
        if (s.substring(i, i+1).equals(c)) {
          lastc = i;
          result += i + 1;
        } else if (lastc >= 0) {
          result += lastc + 1;
        }
      }
      
      System.out.println(result);
      
    }
    in.close();

  }

}
