package org.example.javaguidesdotnet;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class JacksonJsonToSet {
    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);

        String json = "[ \"C\", \"C++\", \"Java\", \"Java EE\", \"Python\", \"Scala\", \"JavaScript\" ]";

        Set<String> progLangs = new HashSet<>();
        progLangs = mapper.readValue(json, Set.class);

        for (Iterator< String > iterator = progLangs.iterator(); iterator.hasNext();) {
            String progLang = (String) iterator.next();
            System.out.println(progLang);
        }
    }
}
