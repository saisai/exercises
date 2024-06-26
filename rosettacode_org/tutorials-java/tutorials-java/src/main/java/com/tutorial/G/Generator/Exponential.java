package com.tutorial.G.Generator;


import java.util.function.LongSupplier;
import static java.util.stream.LongStream.generate;

class SquareGen implements LongSupplier {
    private long n;

    @Override
    public long getAsLong() {
        return n * n++;
    }
}

class CubesGen implements LongSupplier {
    private long n;

    @Override
    public long getAsLong() {
        return n * n * n++;
    }
}
public class Exponential implements LongSupplier {

    private LongSupplier source, filter;
    private long s, f;

    public Exponential(LongSupplier source, LongSupplier filter) {
        this.source = source;
        this.filter = filter;
        f = filter.getAsLong();
    }

    @Override
    public long getAsLong() {
        s = source.getAsLong();

        while(s == f) {
            s = source.getAsLong();
            f = filter.getAsLong();
        }

        while( s > f) {
            f = filter.getAsLong();
        }
        //System.out.printf("%d t", s);
        return s;
    }

    public static void main(String... args) {
        generate(new Exponential(new SquareGen(), new CubesGen()))
                .skip(20).limit(10)
                .forEach(n -> System.out.printf("%d ", n));
    }
}
