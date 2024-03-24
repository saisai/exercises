package org.example.javaguidesdotnet;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class JsonPropertyAnnotationTest {
    public static void main(String[] args) throws JsonProcessingException {
        // Create ObjectMapper object.
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);

        User bean = new User(1, "Ramesh", "Fadatare", "Ramesh Fadatare");
        String result = mapper.writeValueAsString(bean);

        System.out.println(result);
    }
}


 // https://www.javaguides.net/2019/04/change-field-name-in-json-using-jackson.html