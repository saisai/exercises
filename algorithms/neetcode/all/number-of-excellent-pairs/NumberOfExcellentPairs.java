/*
 * https://leetcode.com/problems/number-of-excellent-pairs/
 * https://leetcode.com/problems/number-of-excellent-pairs/discuss/2324984/JavaC%2B%2BPython-Inclusion-Exclusion-Principle
 *
 */
import java.util.*;
import java.util.stream.*;

public class NumberOfExcellentPairs{

	public static void main(String[] args){
		int[] nums = {1,2,3,1};
		int k = 3;
		long result = countExcellentPairs(nums, k);	
		System.out.println(result);
	}

	public static long countExcellentPairs(int[] nums, int k) {
		long res = 0, cnt[] = new long[30];
		for(int n: Arrays.stream(nums).distinct().toArray()){
			++cnt[Integer.bitCount(n)];
    		}
    for (int i = 1; i < 30; ++i)
        for (int j = Math.max(i, k - i); j < 30; ++j)
            res += cnt[i] * cnt[j] * (i == j ? 1 : 2);
    return res;
}

}

