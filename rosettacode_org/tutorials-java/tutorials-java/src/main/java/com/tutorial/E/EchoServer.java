package com.tutorial.E;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

/*
 printf 'echo hello\r\n' | nc localhost 12321
 */

public class EchoServer {
    private static void handleClient(Socket connArg) {
        Charset utf8 = StandardCharsets.UTF_8;
        try(Socket conn = connArg) {
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), utf8)
            );
            PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(conn.getOutputStream(), utf8), true);
            String line;
            while((line = in.readLine()) != null) {
                out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        try(ServerSocket listener = new ServerSocket(12321)) {
            while(true) {
                Socket conn = listener.accept();
                Thread clientThread = new Thread(() -> handleClient(conn));
                clientThread.start();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
