package xyz.blogpost.service;

import xyz.blogpost.model.onetoone.Place;

public interface PlaceService {
    void save(Place place);

    void deleteAllInBatch();
}
