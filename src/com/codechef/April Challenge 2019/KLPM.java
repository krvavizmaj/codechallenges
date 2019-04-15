package april.challenge.y2019;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class KLPM {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String s = in.readLine();
    s = s.toLowerCase();
    s = s.replace(" ", "");
    int n = s.length();

    String reversed = "";
    for (char c : s.toCharArray()) { 
      reversed = c + reversed;
    }
    
    long[][] result = new long[n][n];
    long[][] palindromesStartingAt = new long[n][n];
    long[][] palindromesEndingAt = new long[n][n];
    
    // palindromesStartingAt - number of palindromes starting exactly on position i and ending anywhere before position j
    // palindromesEndingAt - number of palindromes starting anywhere after position i and ending exactly at position j
    for (int i = n-1; i >= 0; i--) {
      for (int j = i; j < n; j++) {
        if (i == j) {
          palindromesStartingAt[i][j] = 1;
          palindromesEndingAt[i][j] = 1;
        } else {
          if (s.substring(i, j+1).equals(reversed.substring(n-j-1, n-i))) {
            palindromesStartingAt[i][j] = palindromesStartingAt[i][j - 1] + 1;
            palindromesEndingAt[i][j] = palindromesEndingAt[i+1][j] + 1;
          } else {
            palindromesStartingAt[i][j] = palindromesStartingAt[i][j - 1];
            palindromesEndingAt[i][j] = palindromesEndingAt[i+1][j];
          }
        }
      }
    }
    
    for (int i = n-1; i >= 0; i--) {
      for (int j = i+1; j < n; j++) {
        if (s.charAt(i) == s.charAt(j)) {
          result[i][j] = 1 + result[i+1][j-1] + palindromesStartingAt[i+1][j-1] + palindromesEndingAt[i+1][j-1];
        }
      }
    }
    
    long sum = 0;
    for(int i = 0; i < n; i++) {
      for(int j = i+1; j < n; j++) {
        sum += result[i][j];
      }
    }
    
    System.out.println(sum);
//    System.out.println(bruteforce(s));
    
    in.close();
  }
  
  public static int bruteforce(String s) {
    int n = s.length();
    int r = 0;
    
    for (int s1 = 0; s1 < n - 1; s1++) {
      for (int e1 = s1; e1 < n - 1; e1++) {
        for (int s2 = e1+1; s2 < n; s2++) {
          for (int e2 = s2; e2 < n; e2++) {
            String t = s.substring(s1, e1+1) + s.substring(s2, e2+1);
            int i = 0;
            while (i < t.length() / 2 && t.charAt(i) == t.charAt(t.length() - i - 1)) {
              i++;
            }
            if (i >= t.length() / 2) {
//              System.out.println(s.substring(s1, e1+1) + " " + s.substring(s2, e2+1));
              r++;
            }
          }
        }
      }
    }
    
    return r;
  }
  
}
