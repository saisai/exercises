package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8;


import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import static com.mycompany.github.douglascraigschmidt.LiveLessons.Java8.utils.ExceptionUtils.rethrowConsumer;

public class ex5 {
    static class MyThread extends Thread {
        MyThread(String name) {
            super(name);
        }

        @Override
        public void run() {
            System.out.println("[Thread "
                                + getId()
                                + "]"
                                + getName());
        }
    }

    public static void main(String[] args) {
        List<Thread> threads = Arrays.asList(
                new MyThread("Larry"),
                new MyThread("Curly"),
                new MyThread("Moe"));

        threads.forEach(System.out::println);

        threads.sort(Comparator.comparing(Thread::getName));

        threads.forEach(System.out::println);

        threads.sort(Comparator.comparing(Thread::getName).reversed());

        System.out.println("\n");
        threads.forEach(Thread::start);

        System.out.println();
        threads
                .forEach(rethrowConsumer(Thread::join));
    }


}
