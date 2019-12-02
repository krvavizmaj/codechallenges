package april.challenge.y2019;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FENCE {

  class Point implements Comparable<Point> {
    int row, col;
    Point(int row, int col) {
      this.row = row;
      this.col = col;
    }
    
    @Override
    public int compareTo(Point o) {
      if (this.row == o.row) {
        return this.col - o.col;
      } else {
        return this.row - o.row;
      }
    }
    
    @Override
    public String toString() {
      return "[" + row + ", " + col + "]";
    }

  }
  
  public static void main(String[] args) throws IOException {
    FENCE fence = new FENCE();
    
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line = in.readLine();
    int cases = Integer.parseInt(line);
    
    for (int t = 0; t < cases; t++) {
      line = in.readLine();
      int rows = Integer.parseInt(line.split(" ")[0]);
      int cols = Integer.parseInt(line.split(" ")[1]);
      int k = Integer.parseInt(line.split(" ")[2]);

      List<Point> plants = new ArrayList<>();
      for (int i = 0; i < k; i++) {
        line = in.readLine();
        int r = Integer.parseInt(line.split(" ")[0]);
        int c = Integer.parseInt(line.split(" ")[1]);
        plants.add(fence.new Point(r, c));
      }
      
      Collections.sort(plants);
      
      long result = 4 * k;
      for (Point p : plants) {
        if (p.row > 1 && plantExists(plants, fence.new Point(p.row - 1, p.col))) {
          result--;
        }
        if (p.row < rows && plantExists(plants, fence.new Point(p.row + 1, p.col))) {
          result--;
        }
        if (p.col > 1 && plantExists(plants, fence.new Point(p.row, p.col - 1))) {
          result--;
        }
        if (p.col < cols && plantExists(plants, fence.new Point(p.row, p.col + 1))) {
          result--;
        }
      }
      
      System.out.println(result);
    }

  }
  
  private static boolean plantExists(List<Point> plants, Point p) {
    int start = 0;
    int end = plants.size() - 1;
    
    while (end - start > 1) {
      int m = (start + end) / 2;
      if (plants.get(m).compareTo(p) == 0) {
        return true;
      } else {
        if (p.compareTo(plants.get(m)) < 0) {
          end = m;
        } else {
          start = m;
        }
      }
    }
    
    return p.compareTo(plants.get(start)) == 0 || p.compareTo(plants.get(end)) == 0;
  }

}
