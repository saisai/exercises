package xyz.blogpost;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.CommonsRequestLoggingFilter;
import xyz.blogpost.model.BlogPost;
import xyz.blogpost.model.manytomany.MPost;
import xyz.blogpost.model.manytomany.MTag;
import xyz.blogpost.model.onetoone.Place;
import xyz.blogpost.model.onetoone.Restaurant;
import xyz.blogpost.repository.BlogPostRepository;
import xyz.blogpost.service.MPostService;
import xyz.blogpost.service.MTagService;
import xyz.blogpost.service.PlaceService;
import xyz.blogpost.service.RestaurantService;

import javax.annotation.PostConstruct;
import java.time.LocalDateTime;
import java.util.Calendar;
import java.util.Date;

@Component
public class MyRunner implements CommandLineRunner {
    @Autowired
    BlogPostRepository blogPostRepository;

    @Autowired
    PlaceService placeService;

    @Autowired
    RestaurantService restaurantService;

    @Autowired
    MPostService mPostService;
    @Autowired
    MTagService mTagService;

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

    @Bean
    void savePlace() {

        // Clean up database tables
        restaurantService.deleteAllInBatch();
        placeService.deleteAllInBatch();

        Restaurant r1 = new Restaurant(true, false);
        //restaurantService.save(r1);

        Restaurant r2 = new Restaurant(true, true);
        //restaurantService.save(r2);

        Place place = new Place("Demon Dogs", "944 W. Fullerton");
        place.setRestaurant(r1);
        r1.setPlace(place);
        placeService.save(place);
        //restaurantService.save(r1);

//        Place place2 = new Place("Ace Hardware", "1013 N. Ashland");
//        place2.setRestaurant(r2);
//        placeService.save(place);
        //restaurantService.save(r2);
    }

    @Bean
    public CommonsRequestLoggingFilter logFilter() {
        CommonsRequestLoggingFilter filter
                = new CommonsRequestLoggingFilter();
        filter.setIncludeQueryString(true);
        filter.setIncludePayload(true);
        filter.setMaxPayloadLength(10000);
        filter.setIncludeHeaders(false);
        filter.setAfterMessagePrefix("REQUEST DATA: ");
        return filter;
    }

    @Bean
    void saveManyToMany() {
        mPostService.deleteAllInBatch();
        mTagService.deleteAllInBatch();

        // Create a Post
        MPost post = new MPost("Hibernate Many to Many Example with Spring Boot",
                "Learn how to map a many to many relationship using hibernate",
                "Entire Post content with Sample code");

        // Create two tags
        MTag tag1 = new MTag("Spring Boot");
        MTag tag2 = new MTag("Hibernate");

        // Add tag references in the post
        post.getMTags().add(tag1);
        post.getMTags().add(tag2);

        // Add post reference in the tags
        tag1.getMPosts().add(post);
        tag2.getMPosts().add(post);

        mPostService.save(post);


    }
}
