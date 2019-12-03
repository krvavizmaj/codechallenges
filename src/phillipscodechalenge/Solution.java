/*
 * Copyright 2019, collaboration Factory AG. All rights reserved.
 */

import java.io.*;
import java.math.*;
import java.util.*;

class Result {
    static double pi = 3.14159265359;
    static double[][] result;
    static List<Integer> r;
    static int executions = 0;

// Solution 1 (brute force) ============================================================================================
    public static String largestSegmentBruteForce(List<Integer> radius, int segments) {
        int n = radius.size();
        Collections.sort(radius);
        Collections.reverse(radius);

        List<Double> max = new ArrayList<>();
        max.add(0.0);
        int[] dist = new int[radius.size()];
        Result.largestSegmentBF(radius, max, dist, 0, segments);

        BigDecimal r = new BigDecimal(Double.toString(max.get(0)));
        r = r.setScale(4, RoundingMode.HALF_EVEN);
        String s = r.toString();
        return s;
    }

    public static void largestSegmentBF(List<Integer> radius, List<Double> max, int[] dist, int index, int segments) {
        if (index >= dist.length) {
            if (segments == 0) {
                double m = (double)radius.get(0) * (double)radius.get(0) * pi;
                for (int i = 0; i < dist.length; i++) {
                    if (dist[i] > 0) {
                        m = Math.min(m, (double)radius.get(i) * (double)radius.get(i) * pi / (double)dist[i]);
                    }
                }
                max.set(0, Math.max(m, max.get(0)));
            }
        } else {
            for (int i = segments; i >= 0; i--) {
                int[] distCopy = Arrays.copyOf(dist, dist.length);
                distCopy[index] = i;
                largestSegmentBF(radius, max, distCopy, index + 1, segments - i);
            }
        }
    };

// Solution 2 (bottom up dynamic programing) ===========================================================================
    public static String largestSegmentBottomUpDP(List<Integer> radius, int segments) {
        int n = radius.size();
        Collections.sort(radius);

        result = new double[n][segments];
        for (int i = 0; i < segments; i++) {
            result[0][i] = pi * radius.get(0) * radius.get(0) / (double)(i+1);
        }
        for (int i = 0; i < n; i++) {
            result[i][0] = pi * radius.get(i) * radius.get(i);
        }

        for (int j = 1; j < segments; j++) {
            for (int i = 1; i < n; i++) {
                result[i][j] = result[i][0] / (double)(j+1);

                for (int k = j; k > 0; k--) {
                    double v = Math.min(result[i][0] / (double)k, result[i-1][j - k]);
                    if (v > result[i][j]) {
                        result[i][j] = v;
                    }
                }
            }
        }
//        printResultMatrix();

        BigDecimal r = new BigDecimal(Double.toString(result[n-1][segments-1]));
        r = r.setScale(4, RoundingMode.HALF_EVEN);
        String s = r.toString();
        return s;
    }

// Solution 3 (top down dynamic programming) ===========================================================================
    public static String largestSegmentTopDownDP(List<Integer> radius, int segments) {
        int n = radius.size();
        Collections.sort(radius);

        result = new double[n][segments];
        r = new ArrayList<>(radius);

        double value = getResult(n - 1, segments - 1);
        System.out.println("executions: " + executions);
//        printResultMatrix();

        BigDecimal r = new BigDecimal(value);
        r = r.setScale(4, RoundingMode.HALF_EVEN);
        return r.toString();
    }

    public static double getResult(int row, int col) {
        if (result[row][col] == 0) {
            executions++;
            if (row == 0 || col == 0) {
                result[row][col] = pi * r.get(row) * r.get(row) / (double)(col+1);
            } else {
                double area = pi * r.get(row) * r.get(row);
                result[row][col] = area / (double)(col+1);

                int intervalStart = 0;
                int intervalEnd = col;
                while (intervalStart < intervalEnd) {
                    int middle = (intervalStart + intervalEnd) / 2;
                    double middleValue = getResult(row-1, middle);
                    double dividedArea = area / (double)(col - middle);
                    double smallerValue = Math.min(dividedArea, middleValue);

                    if (smallerValue > result[row][col]) {
                        result[row][col] = smallerValue;
                    }
                    if (dividedArea > middleValue) {
                        intervalEnd = middle == intervalEnd ? middle - 1 : middle;
                    } else {
                        intervalStart = middle == intervalStart ? middle + 1 : middle;
                    }
                }
            }
        }

        return result[row][col];
    }

    private static void printResultMatrix() {
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[0].length; j++) {
                System.out.print(result[i][j] + "\t");
            }
            System.out.println();
        }
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {

//        Integer[] radius = new Integer[] {2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 12, 14, 15}; int segments = 2;
//        Integer[] radius = new Integer[] {2, 2, 3, 3, 4, 5, 5, 6, 7, 8}; int segments = 8;
//        Integer[] radius = new Integer[] {2, 2, 3, 3, 4, 5, 5}; int segments = 7;
//        Integer[] radius = new Integer[] {2, 3, 3, 4, 4, 5}; int segments = 6;
//        Integer[] radius = new Integer[] {1, 1, 1, 2, 2, 3}; int segments = 6;
//        Integer[] radius = new Integer[] {1, 1, 1, 2}; int segments = 3;
//        Integer[] radius = new Integer[] {1, 1, 1, 2, 2}; int segments = 4;
//        Integer[] radius = new Integer[] {3, 3, 4}; int segments = 3;
//        Integer[] radius = new Integer[] {2, 7}; int segments = 16;

        int numberOfCircles = 100000;
        int segments = 100000;
        Integer[] radius = new Integer[numberOfCircles];
        for (int i = 0; i < numberOfCircles; i++) radius[i] = (int)(Math.random() * 10000.0);

        long startTime = System.currentTimeMillis();

//        String result1 = Result.largestSegmentBruteForce(Arrays.asList(radius), segments); System.out.println(result1);
        String result1 = Result.largestSegmentBottomUpDP(Arrays.asList(radius), segments); System.out.println(result1);
//        String result2 = Result.largestSegmentTopDownDP(Arrays.asList(radius), segments); System.out.println(result2);

        long endTime = System.currentTimeMillis();
        System.out.println("execution time: " + (endTime - startTime));
    }
}
