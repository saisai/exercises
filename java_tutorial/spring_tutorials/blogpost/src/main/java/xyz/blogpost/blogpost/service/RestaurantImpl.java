package xyz.blogpost.blogpost.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import xyz.blogpost.blogpost.model.onetoone.Restaurant;
import xyz.blogpost.blogpost.repository.RestaurantRepository;

@Service
public class RestaurantImpl implements RestaurantService{

    @Autowired
    RestaurantRepository restaurantRepository;

    @Override
    public void save(Restaurant restaurant) {
        restaurantRepository.save(restaurant);
    }

    @Override
    public void deleteAllInBatch(){
        restaurantRepository.deleteAllInBatch();;
    }
}
