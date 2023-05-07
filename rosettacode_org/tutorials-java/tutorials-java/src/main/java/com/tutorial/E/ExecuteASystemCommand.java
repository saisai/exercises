package com.tutorial.E;

import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;

import java.io.IOException;
import java.io.InputStream;

public class ExecuteASystemCommand {

    static class StreamGobber implements Runnable {
        private InputStream Pipe;
        public StreamGobber(InputStream pipe) {
            if(pipe == null) {
                throw  new NullPointerException("bad pipe");
            }
            Pipe = pipe;
        }

        @Override
        public void run() {
            try {
                byte buffer[] = new byte[2048];
                int read = Pipe.read(buffer);
                while(read >= 0) {
                    System.out.write(buffer, 0, read);
                    read = Pipe.read(buffer);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
              if(Pipe != null) {
                  try {
                      Pipe.close();
                  } catch (IOException e) {

                  }
              }
            }
        }
    }

    private static void executeCmd(String string) {
        InputStream pipeOut = null;
        try {
            Process aProcess = Runtime.getRuntime().exec(string);

            //These two thread shall stop by themself when the process end
            Thread pipeThread = new Thread(new StreamGobber(aProcess.getInputStream()));
            Thread errorThread = new Thread(new StreamGobber(aProcess.getErrorStream()));

            pipeThread.start();
            errorThread.start();

            aProcess.waitFor();
        } catch(IOException e) {
            e.printStackTrace();
        } catch(InterruptedException ie) {
            ie.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // the command to execute
        executeCmd("ls -oa");
        System.out.println();
        executeCmd("ls -oa D:\\");
    }

}
