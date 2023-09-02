package xyz.blogpost.controller;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.MediaType;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.util.HtmlUtils;
import xyz.blogpost.model.BlogPost;
import xyz.blogpost.model.BlogPostCriteria;
import xyz.blogpost.pojo.Greeting;
import xyz.blogpost.pojo.HelloMessage;
import xyz.blogpost.repository.BlogPostRepository;

import javax.persistence.EntityManager;
import javax.persistence.TemporalType;
import javax.persistence.TypedQuery;
import java.sql.Timestamp;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@EnableScheduling
@Controller
public class GreetingController {

    @Autowired
    BlogPostRepository blogPostRepository;

    @Autowired
    EntityManager entityManager;

    @Autowired
    SimpMessagingTemplate template;

    @GetMapping(value="/websocket")
    public ModelAndView index() {

//        java.util.Date utilDate = new java.util.Date();
//        System.out.println("utilDate " + utilDate);
//        java.sql.Date sqlDate = new java.sql.Date(utilDate.getTime());
//        System.out.println("sqlDate " + sqlDate);

        java.util.Date utilDate = new java.util.Date();
        System.out.println("java.util.Date time    : " + utilDate);
        java.sql.Timestamp sqlTS = new java.sql.Timestamp(utilDate.getTime());
        System.out.println("java.sql.Timestamp time: " + sqlTS);

        DateFormat df = new SimpleDateFormat("dd/MM/YYYY hh:mm:ss:SSS");
        System.out.println("Date formatted         : " + df.format(utilDate));

        System.out.println("websocket");
        return new ModelAndView("websocket");
    }

//    @RequestMapping(value = "/loadCityByCountry", method = RequestMethod.POST, produces = MediaType.APPLICATION_JSON_VALUE, consumes = MediaType.APPLICATION_JSON_VALUE)
//    public @ResponseBody List<City> loadCityByCountry(@RequestBody CountryCriteria countryCriteria) {
//        List<City> cities = cityService.getCitiesByCountry(countryCriteria.getCountryId());
//        return cities;
//    }

//    @RequestMapping(value = "/updateDelete", method = RequestMethod.POST)
//    public @ResponseBody String updateDelete(@RequestBody String jsonString)
//    {
//        System.out.println("updateDelete " + jsonString);
//        return "success";
//
//    }

    //@RequestMapping(value = "/updateDelete", method = RequestMethod.POST)
    @RequestMapping(value = "/updateDelete", method = RequestMethod.POST, produces = MediaType.APPLICATION_JSON_VALUE, consumes = MediaType.APPLICATION_JSON_VALUE)
    public @ResponseBody String updateDelete(@RequestBody BlogPostCriteria blogPostCriteria)
    {
        System.out.println("updateDelete " + blogPostCriteria.getBlogPostID());
        blogPostRepository.updateDelete(blogPostCriteria.getBlogPostID());
        return "success" + blogPostCriteria.getBlogPostID();
    }

    @RequestMapping(value = "/deleteAll", method = RequestMethod.POST, produces = MediaType.APPLICATION_JSON_VALUE, consumes = MediaType.APPLICATION_JSON_VALUE)
    public @ResponseBody String deleteAll(@RequestBody BlogPostCriteria blogPostCriteria) throws InterruptedException {
//        java.sql.Timestamp.valueOf(blogPostCriteria.getEndTime());
        Timestamp ts = Timestamp.valueOf(blogPostCriteria.getEndTime());
        System.out.println("deleteall " + blogPostCriteria.getEndTime());
        Thread.sleep(1000);
        blogPostRepository.deleteAll(ts);
        return "success" + blogPostCriteria.getEndTime();

    }

    @GetMapping(value="/popup")
    public ModelAndView popup() {
        System.out.println("websocket");
        return new ModelAndView("popup");
    }

    public List<BlogPost> testDate(Long lastId) {
        java.util.Date date = new Date();
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
        String startDate = formatter.format(date);

        java.util.Date utilDate = new java.util.Date();
//        System.out.println("utilDate " + utilDate);
        java.sql.Timestamp endDate = new java.sql.Timestamp(utilDate.getTime());
//        System.out.println("java.sql.Timestamp time: " + endDate);


        TypedQuery<BlogPost> query = entityManager.createQuery("SELECT t FROM BlogPost t " +
                        "where t.delete != 1 and t.createdAt between :date1 and :date2 and t.id > :lastId order by id desc",
                BlogPost.class);

        List<BlogPost> blogPosts = query.setParameter("date1", java.sql.Timestamp.valueOf(startDate + " 00:00:00"))
                .setParameter("date2", endDate)
                .setParameter("lastId", lastId).getResultList();
        return blogPosts;
    }

    private Long count = 0L;
    @MessageMapping("/history")
    @SendTo("/topic/history")
    public Long history(Long to) {
        System.out.println("History " + to);
        this.count = to;
        return to;
    }

    @Scheduled(fixedRate = 1000)
    @MessageMapping("/hello")
    @SendTo("/topic/greetings")
    public void greet()  {
        //Thread.sleep(1000);
        System.out.println("greeting count " + this.count);
        List<BlogPost> result = testDate(this.count);
        JSONArray mainJa = new JSONArray();

        if(result.size() > 0) {
            result = testDate(0L);
        }

        for(BlogPost obj : result) {
            JSONArray a = new JSONArray();
            a.put(obj.getId());
            a.put(obj.getCreatedAt());
            a.put(obj.getLink());

            mainJa.put(a);
        }
        //System.out.println(mainJa.toString());
        this.template.convertAndSend("/topic/greetings", mainJa.toString());

    }

}
