package test;

import java.util.Arrays;

public class ArrayTriplets {

  public static void main(String[] args) {
    ArrayTriplets a = new ArrayTriplets();
    
    int[] arr = new int[] {88, 13, 9, 6, 88, 27, 21, 25, 75, 43, 65, 94, 27, 99, 63, 100, 73, 8};
    System.out.println(a.arrayTriplets(arr));
  }

  int arrayTriplets(int[] arr) {

    int res = 0;
    Arrays.sort(arr);
    int n = arr.length;

    for (int i = 0; i < n - 2; i++) {
      for (int j = i + 1; j < n - 1; j++) {
        int indexBigger = findIndexOfValue(arr, n, arr[i] + arr[j], j);
        res += indexBigger - j - 1;
      }
    }

    return res;
  }
  
  int findIndexOfValue(int[] arr, int size, int biggerThan, int afterIndex) {
    int start = afterIndex + 1;
    int end = size - 1;    

    while (end - start > 1) {
      int t = (start + end) / 2;
      if (arr[t] >= biggerThan)
        end = t;
      else
        start = t;
    }

    if (arr[end] < biggerThan)
      return end + 1;
    else 
      return arr[start] >= biggerThan ? start : end;
  }
  
}
