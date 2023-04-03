package com.example.service;

import com.example.model.City;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MyRespository extends JpaRepository<City, Long> {
}
