package org.example.javaguidesdotnet;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class JacksonJsonToList {
    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);

        String json = "[ \"C\", \"C++\", \"Java\", \"Java EE\", \"Python\", \"Scala\", \"JavaScript\" ]";

        List<String> progLangs = new ArrayList<>();
        progLangs = mapper.readValue(json, List.class);

        for(Iterator<String> iterator = progLangs.iterator(); iterator.hasNext();) {
            String progLang = iterator.next();
            System.out.println(progLang);
        }
    }
}
