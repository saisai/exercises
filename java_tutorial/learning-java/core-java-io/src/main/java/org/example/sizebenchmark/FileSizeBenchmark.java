package org.example.sizebenchmark;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.Blackhole;

import java.io.File;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.SingleShotTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 3, time = 10, timeUnit = TimeUnit.NANOSECONDS)
@Measurement(iterations = 3, time = 10, timeUnit = TimeUnit.NANOSECONDS)
public class FileSizeBenchmark {
    public static void main(String[] args) throws Exception {
        org.openjdk.jmh.Main.main(args);
    }

    @Benchmark
    public void getFileSizeUsingLengthMethod(Blackhole blackhole) throws Exception {
        File file = new File("src/test/resources/size/sample_file_1.in");
        blackhole.consume(file.length());
    }

}
