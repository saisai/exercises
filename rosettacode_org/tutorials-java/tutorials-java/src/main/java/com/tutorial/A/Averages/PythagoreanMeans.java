package com.tutorial.A.Averages;

import com.sun.java.browser.plugin2.DOM;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.DoubleStream;

public class PythagoreanMeans {
    public static double arithmeticMean(List<Double> numbers) {
        if(numbers.isEmpty()) return Double.NaN;
        double mean = 0.0;
        for(Double number : numbers) {
            mean += number;
        }
        return mean / numbers.size();
    }

    public static double arithmeticMeanJava8(double array[]) {
        if(array == null || array.length == 0) {
            return 0.0;
        } else {
            return DoubleStream.of(array).average().getAsDouble();
        }
    }

    public static double geometricMean(List<Double> numers) {
        if(numers.isEmpty()) return Double.NaN;
        double mean = 1.0;
        for(Double number : numers) {
            mean *= number;
        }
        return Math.pow(mean, 1.0 / numers.size());
    }

    public static double geomAverageJava8(double array[]) {
        if(array == null || array.length == 0) {
            return 0.0;
        } else {
            double aver = DoubleStream.of(array).reduce(1, (x, y) -> x * y);
            return Math.pow(aver, 1.0 / array.length);
        }
    }

    public static double harmoniceMean(List<Double> numbers) {
        if(numbers.isEmpty() || numbers.contains(0.0)) return Double.NaN;
        double mean = 0.0;
        for(Double number : numbers) {
            mean += (1.0 / number);
        }
        return numbers.size() / mean;
    }

    public static double harmAverageJava8(double array[]) {
        if(array == null || array.length == 0) {
            return 0.0;
        } else {
            double aver = DoubleStream.of(array)
                    // removes null values
                    .filter(n -> n > 0.0)
                    // generate 1/n array
                    .map( n -> 1.0 / n)
                    // accumulating
                    .reduce(0, (x, y) -> x + y);
                    // just this reduce is not working- need to do in 2 steps
                    // .reduce(0, (x, y) -> 1.0/x + 1.0/y);
            return array.length / aver;
        }
    }

    public static void main(String... args) {
        Double[] array = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};
        List<Double> list = Arrays.asList(array);
        double arithmetic = arithmeticMean(list);
        double geometric = geometricMean(list);
        double harmonic = harmoniceMean(list);
        System.out.format("A = %f G = %f H = %f%n", arithmetic, geometric, harmonic);
        System.out.format("A >= G is %b, G >= H is %b%n", (arithmetic >= geometric), (geometric >= harmonic));
    }
}
