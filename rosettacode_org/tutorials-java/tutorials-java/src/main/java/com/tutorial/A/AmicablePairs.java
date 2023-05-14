package com.tutorial.A;

import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class AmicablePairs {
    public static Long properDivSum(Long n) {
        return LongStream.rangeClosed(1, (n + 1) / 2).filter(i -> n % i == 0).sum();
    }

    public static void main(String[] args) {
        int limit = 20_000;

        Map<Long, Long> map = LongStream.rangeClosed(1, limit)
                .parallel()
                .boxed()
                .collect(Collectors.toMap(Function.identity(), AmicablePairs::properDivSum));

        LongStream.rangeClosed(1, limit)
                .forEach(n -> {
                    long m = map.get(n);
                    if(m > n && m <= limit && map.get(m) == n)
                        System.out.printf("%s %s %n", n, m);
                });
    }
}
