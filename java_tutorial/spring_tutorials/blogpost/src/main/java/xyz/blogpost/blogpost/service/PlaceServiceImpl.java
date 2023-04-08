package xyz.blogpost.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import xyz.blogpost.blogpost.model.onetoone.Place;
import xyz.blogpost.blogpost.repository.PlaceRepository;

@Service
public class PlaceServiceImpl implements PlaceService {

    @Autowired
    PlaceRepository placeRepository;

    @Override
    public void save(Place place) {
        placeRepository.save(place);
    }

    @Override
    public void deleteAllInBatch() {
        placeRepository.deleteAllInBatch();
    }
}
