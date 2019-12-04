import java.util.Arrays;

public class Solution2 {

    public static int findSolution(int[] a, int[] b, int d) {
        Arrays.sort(a);
        Arrays.sort(b);

        int result = 0;
        for (int i = 0; i < a.length; i++) {
            int aIntervalStart = (a[i]-d) < 0 ? 0 : (a[i]-d);
            int aIntervalEnd = (a[i]+d) >= a.length ? a.length-1 : (a[i]+d);

            // find location of a in array b
            int bIntervalStart = 0;
            int bIntervalEnd = b.length;
            if (aIntervalEnd < bIntervalStart || aIntervalStart > bIntervalEnd) {
                result++;
            } else {
                while (bIntervalEnd - bIntervalStart > 1) {
                    int middle = (bIntervalStart + bIntervalEnd) / 2;
                    if (b[middle] < a[i]) {
                        bIntervalStart = middle;
                    } else {
                        bIntervalEnd = middle;
                    }
                }

                if (bIntervalStart < aIntervalStart && bIntervalEnd > aIntervalEnd) {
                    result++;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] a = {};
        int[] b = {};
        int d = 2;

        int result = findSolution(a, b, d);
        System.out.println(result);
    }
}
