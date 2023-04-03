package com.example;

import com.example.model.City;
import com.example.service.MyRespository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class MyRunner implements CommandLineRunner {

    private static Logger LOG = LoggerFactory.getLogger(MyRunner.class);

    @Autowired
    MyRespository myRespository;

    @Override
    public void run(String... args) {
        System.out.println("Hello");
        LOG.info("EXECUTING : comand line runner");

        List<City> cities = myRespository.findAll();

        cities.stream().forEach(e -> System.out.println(e.getName()));
    }
}
