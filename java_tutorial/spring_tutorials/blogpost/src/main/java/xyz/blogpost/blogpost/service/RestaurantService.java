package xyz.blogpost.blogpost.service;

import xyz.blogpost.blogpost.model.onetoone.Restaurant;

public interface RestaurantService {

    void save(Restaurant restaurant);

    void deleteAllInBatch();
}
