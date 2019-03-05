import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Jain {
  
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int testCases = Integer.parseInt(line);
    
    for (int t = 0; t < testCases; t++) {
      int[][] with = new int[6][32];
      line = in.readLine();
      int n = Integer.parseInt(line);
      
      for (int i = 0; i < n; i++) {
        line = in.readLine();
        
        int wordToInt = 0;
        if (line.indexOf("a") != -1) wordToInt = wordToInt |= 16;
        if (line.indexOf("e") != -1) wordToInt = wordToInt |= 8;
        if (line.indexOf("i") != -1) wordToInt = wordToInt |= 4;
        if (line.indexOf("o") != -1) wordToInt = wordToInt |= 2;
        if (line.indexOf("u") != -1) wordToInt = wordToInt |= 1;
        
        int len = Integer.bitCount(wordToInt);
        with[len][wordToInt]++;
      }

      long res = 0;
      for (int firstDishLen = 1; firstDishLen < 5; firstDishLen++) {
        for (int secondDishLen = firstDishLen; secondDishLen <= 5; secondDishLen++) {
          long ddd = 0;
          for (int j1 = 1; j1 < 32; j1++) {
            for (int j2 = 1; j2 < 32; j2++) {
              if ((j1 | j2) == 31) {
                  ddd += with[firstDishLen][j1] * with[secondDishLen][j2];
              }
            }
          }
            
          if (firstDishLen == secondDishLen) {
            res += ddd / 2;
          } else {
            res += ddd;
          }
        }
      }
      
      // concatenating words with all letters
      int allFive = with[5][31];
      res += (allFive * (allFive - 1)) / 2;
      
      System.out.println(res);
    }
    
    in.close();
    
  }


}
