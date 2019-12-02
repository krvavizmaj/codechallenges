import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Chnum {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int t = Integer.parseInt(line);
    
    for (int i = 0; i < t; i++) {
      line = in.readLine();
      int n = Integer.parseInt(line);
      line = in.readLine();
      String[] aList = line.split(" ");
      
      int positive = 0;
      int negative = 0;
      for (String a : aList) {
        int ai = Integer.parseInt(a);
        if (ai > 0) {
          positive++;
        } else {
          negative++;
        }
      }
      
      int min = 0;
      int max = 0;
      if (Math.min(positive, negative) != 0) {
        min = Math.min(positive, negative);
      } else {
        min = Math.max(positive, negative);
      }
      max = Math.max(positive, negative);
      
      System.out.println(max + " " + min);
    }
    
   
    in.close();
  }

}
