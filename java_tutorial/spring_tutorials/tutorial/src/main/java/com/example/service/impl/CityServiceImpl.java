package com.example.service.impl;

import com.example.model.City;
import com.example.repository.CityRepository;
import com.example.service.CityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CityServiceImpl implements CityService {
    @Autowired
    private CityRepository cityRepository;

    @Override
    public List<City> findAll() {
        List<City> cities = (List<City>) cityRepository.findAll();
        return cities;
    }
}
