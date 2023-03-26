package com.tutorial.R;

import java.util.function.IntConsumer;
import java.util.stream.DoubleStream;

import static java.util.stream.DoubleStream.generate;
import static java.lang.System.nanoTime;
import static java.lang.System.out;
public interface RateCounter {
    public static DoubleStream benchmark(final int n, final IntConsumer consumer, final int argument) {
        return generate(() -> {
            final long time = nanoTime();
            consumer.accept(argument);
            return nanoTime() - time;
        }).limit(n);
    }

    public static void main(String... args) {
        benchmark(
                10,
                x -> out.print(""),
                10
        ).forEach(out::println);
    }




}
