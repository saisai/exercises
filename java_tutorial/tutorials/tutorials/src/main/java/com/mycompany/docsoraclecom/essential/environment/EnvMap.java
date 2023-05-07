package com.mycompany.docsoraclecom.essential.environment;

import java.util.Map;

public class EnvMap {

    static String threadMessage() {
        String threadName = Thread.currentThread().getName();
        return threadName;
    }
    public static void main(String[] args) {
//        Map<String, String> env = System.getenv();
//        for(String envName : env.keySet()) {
//            System.out.format("%s=%s%n", envName, env.get(envName));
//        }

        Thread a = new Thread(new TestThread());
        Thread b = new Thread(new TestThread());
        a.start();
        b.start();
    }

    static class TestThread implements Runnable {
        Map<String, String> env = System.getenv();
        @Override
        public void run() {
            for(String envName : env.keySet()) {
                System.out.format("I am %s on %s=%s%n", threadMessage(), envName, env.get(envName));
            }

        }
    }
}
