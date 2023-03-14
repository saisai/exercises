package zengcode.medium.com;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import zengcode.medium.com.model.Person;
import zengcode.medium.com.repository.PersonRepository;

@SpringBootApplication
public class Application {

    private final static Logger log = LoggerFactory.getLogger(Application.class);


    public static void main(String[] args) throws Exception {

        SpringApplication.run(Application.class);
    }

    @Bean
    CommandLineRunner demo(PersonRepository personRepository) {
        return args -> {

            personRepository.deleteAll();

            personRepository.save(new Person("Pea", "L1"));
            personRepository.save(new Person("Pea", "L2"));
            personRepository.save(new Person("Nee", "L"));
            personRepository.save(new Person("Bee", "LL"));


            System.out.println(personRepository.findByFirstName("Pea"));
        };
    }


}
