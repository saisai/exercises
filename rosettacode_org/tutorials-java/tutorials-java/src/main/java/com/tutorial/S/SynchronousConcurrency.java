package com.tutorial.S;

import com.tutorial.Utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Objects;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicLong;

public class SynchronousConcurrency {

     public static void main(String... args) throws Exception {
        final AtomicLong lineCount = new AtomicLong(0);
        final BlockingQueue<String> queue = new LinkedBlockingQueue<String>();
        final String EOF = new String();

        String fileName = new Utils().getFilename("foobar.txt");
        final Thread writerThread = new Thread(new Runnable() {
            @Override
            public void run() {
                long linesWrote = 0;
                while(true) {
                    try {
                        String line =queue.take();
                        // Reference equality
                        if(line == EOF)
                            break;
                        System.out.println(line);
                        linesWrote++;
                    } catch (InterruptedException ie)
                    { }
                }
                lineCount.set(linesWrote);
            }
        });

        writerThread.start();
        // No need to start a third thread for the reader, just use this thread
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        String line;
        while((line = br.readLine()) != null)
            queue.put(line);
        br.close();
        queue.put(EOF);
        writerThread.join();
        // AtomicLong is not needed here due to memory barrier created by thread join, but still need a mutable long since lineCount must be final to access it from an anonymous class
        System.out.println("Line count: " + lineCount.get());
        return;

    }
}
