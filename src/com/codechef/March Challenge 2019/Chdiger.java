import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Chdiger {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int t = Integer.parseInt(line);
    
    for (int i = 0; i < t; i++) {
      line = in.readLine();
      String[] lineParts = line.split(" ");
      long n = Long.parseLong(lineParts[0]);
      int d = Integer.parseInt(lineParts[1]);
      
      long min = n;
      List<Character> digits = new ArrayList<>();
      for (char c : String.valueOf(n).toCharArray()) digits.add(c);
      
      for (int j = 0; j <= digits.size(); j++) {
        int k = 0;
        while (k < digits.size() - 1 - j && digits.get(k+1) >= digits.get(k)) {
          k++;
        }
        digits.remove(k);
        digits.add((char) (d + 48));
        
        String newNString = "";
        for (char c : digits) newNString += c;
        long newN = Long.parseLong(newNString);
        if (newN < min) {
          min = newN;
        }
      }
      
      System.out.println(min);
    }
    in.close();
  }

}
