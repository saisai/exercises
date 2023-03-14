package websocket.zengcode.com.scheduler;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import websocket.zengcode.com.model.Data;
import websocket.zengcode.com.service.AsyncService;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

@Component
public class SchedulerTask {

    private static Logger log = LoggerFactory.getLogger(SchedulerTask.class);

    @Autowired
    private AsyncService asyncService;

    @Scheduled(fixedRate = 10000)
    public void executingScheduler() throws InterruptedException, ExecutionException {
        Instant start = Instant.now();

        Future<Data> str1 = asyncService.getMessage();
        Future<Data> str2 = asyncService.getMessage();
        Future<Data> str3 = asyncService.getMessage();
        Future<Data> str4 = asyncService.getMessage();
        Future<Data> str5 = asyncService.getMessage();

        while (!(str1.isDone() && str2.isDone() && str3.isDone() && str4.isDone() && str5.isDone())) {
            Thread.sleep(10); //10-millisecond pause between each check
        }


        Instant end = Instant.now();
        log.info("total execution times ========> " + ChronoUnit.MILLIS.between(start, end));
        log.info("str1 = {} ", str1.get().getValue());
        log.info("str2 = {} ", str2.get().getValue());
        log.info("str3 = {} ", str3.get().getValue());
        log.info("str4 = {} ", str4.get().getValue());
        log.info("str5 = {} ", str5.get().getValue());
        log.info("=====================================");
        log.info("=====================================");
    }

}
