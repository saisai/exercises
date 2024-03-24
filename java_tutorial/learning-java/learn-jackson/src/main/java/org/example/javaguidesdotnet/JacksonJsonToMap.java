package org.example.javaguidesdotnet;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.util.Map;

public class JacksonJsonToMap {
    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);

        String json = "{" +
                "  \"THU\" : 5," +
                "  \"TUE\" : 3," +
                "  \"WED\" : 4," +
                "  \"SAT\" : 7," +
                "  \"FRI\" : 6," +
                "  \"MON\" : 2," +
                "  \"SUN\" : 1" +
                "}";

        Map<String, Integer> days = mapper.readValue(json, Map.class);
        for (Map.Entry< String, Integer > day: days.entrySet()) {
            System.out.println(day.getKey() + "=" + day.getValue());
        }
    }
}

// https://www.javaguides.net/2019/04/jackson-list-set-and-map-serialization-and-deseialization-in-java-example.html
