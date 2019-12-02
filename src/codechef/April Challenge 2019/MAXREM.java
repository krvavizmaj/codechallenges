package april.challenge.y2019;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MAXREM {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int n = Integer.parseInt(line);
    
    line = in.readLine();
    String[] lineParts = line.split(" ");
    
    int max1 = 0;
    int max2 = 0;
    for (int i = 0; i < n; i++) {
      int t = Integer.parseInt(lineParts[i]);
      if (t > max1) {
        if (t != max1) {
          max2 = max1;
        }
        max1 = t;
      } else if (t > max2 && t != max1) {
        max2 = t;
      }
    }

    System.out.println(max2);
    in.close();
  }

}
