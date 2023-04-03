package com.example.service;

import com.example.model.City;
import com.example.repository.CityRepository;

import java.util.List;

public interface CityService {
    List<City> findAll();
}
