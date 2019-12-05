import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Solution2 {

    public static int comparatorValue(List<Integer> a, List<Integer> b, int d) {
        Collections.sort(a);
        Collections.sort(b);

        int result = 0;
        for (int i = 0; i < a.size(); i++) {
            int aIntervalStart = a.get(i) - d;
            int aIntervalEnd = a.get(i) + d;

            // find location of a in array b
            int bIntervalStart = 0;
            int bIntervalEnd = b.size() - 1;
            if (aIntervalEnd < b.get(bIntervalStart) || aIntervalStart > b.get(bIntervalEnd)) {
                result++;
            } else {
                while (bIntervalEnd - bIntervalStart > 1) {
                    int middle = (bIntervalStart + bIntervalEnd) / 2;
                    if (b.get(middle) < a.get(i)) {
                        bIntervalStart = middle;
                    } else {
                        bIntervalEnd = middle;
                    }
                }

                if (b.get(bIntervalStart) < aIntervalStart && b.get(bIntervalEnd) > aIntervalEnd) {
                    result++;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Integer[] a = {3, 1, 5};
        Integer[] b = {5, 6, 7};
        int d = 3;

        int result = comparatorValue(Arrays.asList(a), Arrays.asList(b), d);
        System.out.println(result);
    }
}
