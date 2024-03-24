package org.example.javaguidesdotnet;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.util.HashSet;
import java.util.Set;

public class JacksonSetToJson {
    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);

        Set< String > progLangs = new HashSet<>();
        progLangs.add("C");
        progLangs.add("C++");
        progLangs.add("Java");
        progLangs.add("Java EE");
        progLangs.add("Python");
        progLangs.add("Scala");
        progLangs.add("JavaScript");
        // Serialize Object to JSON.
        String json = mapper.writeValueAsString(progLangs);

        // Print json
        System.out.println(json);
    }
}
