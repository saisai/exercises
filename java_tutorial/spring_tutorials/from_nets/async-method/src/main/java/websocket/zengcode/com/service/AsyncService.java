package websocket.zengcode.com.service;

import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.AsyncResult;
import org.springframework.stereotype.Service;
import websocket.zengcode.com.model.Data;

import java.util.UUID;
import java.util.concurrent.Future;

@Service
public class AsyncService {

    @Async
    public Future<Data> getMessage() throws InterruptedException {

        // Artificial delay of 1s for demonstration purposes
        Thread.sleep(1000L);
        Data data = new Data();
        data.setValue(UUID.randomUUID().toString());
        return new AsyncResult<>(data);
    }
}
