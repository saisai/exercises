package com.tutorial.A.Averages;

import java.util.LinkedList;
import java.util.Queue;

public class SimpleMovingAverage {
    private final Queue<Double> window = new LinkedList<Double>();
    private final int period;
    private double sum;

    public SimpleMovingAverage(int period) {
        assert period > 0 : "Period must be a positive integer";
        this.period = period;
    }

    public void newNum(double num) {
        sum += num;
        window.add(num);
        if(window.size() > period) {
            sum -= window.remove();
        }
    }

    public double getAvg() {
        if(window.isEmpty()) return 0.0; // technically the average is undefined
        return sum / window.size();
    }

    public static void main(String[] args) {
        double[] testData = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
        int[] windowSizes = {3, 5};
        for(int windSize : windowSizes) {
            SimpleMovingAverage ma = new SimpleMovingAverage(windSize);
            for(double x : testData) {
                ma.newNum(x);
                System.out.println("Next number =" + x + ", SMA = " + ma.getAvg());
            }
            System.out.println();
        }
    }
}
