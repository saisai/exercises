package xyz.blogpost.controller;

import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.util.HtmlUtils;
import xyz.blogpost.pojo.Greeting;
import xyz.blogpost.pojo.HelloMessage;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

@EnableScheduling
@Controller
public class GreetingController {

    @Autowired
    SimpMessagingTemplate template;

    @GetMapping(value="/websocket")
    public ModelAndView index() {
        System.out.println("websocket");
        return new ModelAndView("websocket");
    }


//    @MessageMapping("/hello")
//    @SendTo("/topic/greetings")
//    public Greeting greet2(HelloMessage message) {
//        return new Greeting("Hello, " +
//                HtmlUtils.htmlEscape(message.getName()));
//
//    }


    //@Scheduled(fixedRate = 5000)
//    @Scheduled(fixedRate = 10000)
//    @MessageMapping("/hello")
//    @SendTo("/topic/greetings")
//    public void greet() {
//        String timeStamp = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new java.util.Date());
//        System.out.println("Hello" + timeStamp);
//        this.template.convertAndSend("/topic/greetings"
//                               new Greeting("Hello, " +  timeStamp ));
//
//    }

    @Scheduled(fixedRate = 10000)
    @MessageMapping("/hello")
    @SendTo("/topic/greetings")
    public ArrayList<Greeting> greet() {
        String timeStamp = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new java.util.Date());
        System.out.println("Hello" + timeStamp);
        //this.template.convertAndSend("/topic/greetings"
        //new Greeting("Hello, " +  timeStamp ));

        ArrayList<Greeting> lst = new ArrayList<>();
        lst.add(new Greeting("Hello 1"));
        lst.add(new Greeting("Hello 2"));
        return lst;
    }
}
