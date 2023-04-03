package com.example.controller;

import com.example.model.City;
import com.example.service.CityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class MyController {
    @Autowired
    private CityService cityService;

    @GetMapping("/showCities")
    public String findCities(Model model) {
        List<City> cities = (List<City>) cityService.findAll();

        model.addAttribute("cities", cities);
        return "showCities";
    }
}
