package xyz.blogpost.blogpost.service;

import org.springframework.stereotype.Service;
import xyz.blogpost.blogpost.model.onetoone.Place;

public interface PlaceService {
    void save(Place place);

    void deleteAllInBatch();
}
