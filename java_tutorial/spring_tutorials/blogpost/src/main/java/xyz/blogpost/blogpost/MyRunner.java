package xyz.blogpost.blogpost;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import xyz.blogpost.blogpost.model.BlogPost;
import xyz.blogpost.blogpost.repository.BlogPostRepository;
import xyz.blogpost.blogpost.service.BlogPostService;

import javax.annotation.PostConstruct;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.Calendar;
import java.util.Date;

@Component
public class MyRunner implements CommandLineRunner {
    @Autowired
    BlogPostRepository blogPostRepository;
    @Override
    public void run(String... args){
        System.out.println("hello run");
    }

    @PostConstruct
    public void addBlogPost() {
        System.out.println("Save data");
        LocalDateTime today = LocalDateTime.now();
        Date now = new Date();

//        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
//        Date date = new Date();

        Calendar calendar = Calendar.getInstance();
        Date date =  calendar.getTime();
        blogPostRepository.save(new BlogPost("test", "link", "description",
                date));
    }
}
