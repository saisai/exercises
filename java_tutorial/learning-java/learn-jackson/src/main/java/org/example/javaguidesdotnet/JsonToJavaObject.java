package org.example.javaguidesdotnet;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Iterator;

public class JsonToJavaObject {
    public static void main(String[] args) throws IOException {

        ObjectMapper mapper = new ObjectMapper();

        // read json file and convert it to java object
        InputStream inputStream = Files.newInputStream(Paths.get("post.json"));
        Post post = mapper.readValue(inputStream, Post.class);
        inputStream.close();

        System.out.println("Printing post details");
        System.out.println(post.getId());
        System.out.println(post.getTitle());
        System.out.println(post.getDescription());
        System.out.println(post.getContent());
        System.out.println(post.getLastUpdatedAt());
        System.out.println(post.getPostedAt());

        System.out.println("Printing tag details of post:: " + post.getTitle());
        for(Iterator<Tag> iterator = post.getTags().iterator(); iterator.hasNext();) {
            Tag tag = iterator.next();
            System.out.println(tag.getId());
            System.out.println(tag.getName());
        }


    }
}


// https://www.javaguides.net/2019/04/jackson-convert-java-object-tofrom-json-example.html