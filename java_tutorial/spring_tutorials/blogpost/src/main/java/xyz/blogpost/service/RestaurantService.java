package xyz.blogpost.service;

import xyz.blogpost.model.onetoone.Restaurant;

public interface RestaurantService {

    void save(Restaurant restaurant);

    void deleteAllInBatch();
}
