package com.springtutorials.tutorials.manytomany.controller;

import com.springtutorials.tutorials.manytomany.model.Tutorial3;
import com.springtutorials.tutorials.manytomany.repository.Tutorial3Repository;
import com.springtutorials.tutorials.onetoone.exception.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@CrossOrigin(origins="http://localhost:8080")
@RestController
@RequestMapping("/api/tutorials3")
public class Tutorial3Controller {

    @Autowired
    Tutorial3Repository tutorial3Repository;

    @GetMapping("/tutorials")
    public ResponseEntity<List<Tutorial3>> getAllTutorials(@RequestParam(required = false) String title) {
        List<Tutorial3> tutorials = new ArrayList<>();

        if (title == null)
            tutorial3Repository.findAll().forEach(tutorials::add);
        else
            tutorial3Repository.findByTitleContaining(title).forEach(tutorials::add);

        if (tutorials.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }

        return new ResponseEntity<>(tutorials, HttpStatus.OK);
    }

    @GetMapping("/tutorials/{id}")
    public ResponseEntity<Tutorial3> getTutorialById(@PathVariable("id") long id) {
        Tutorial3 tutorial = tutorial3Repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial with id = " + id));

        return new ResponseEntity<>(tutorial, HttpStatus.OK);
    }

    @PostMapping("/tutorials")
    public ResponseEntity<Tutorial3> createTutorial(@RequestBody Tutorial3 tutorial) {
        Tutorial3 _tutorial = tutorial3Repository.save(new Tutorial3(tutorial.getTitle(), tutorial.getDescription(), true));
        return new ResponseEntity<>(_tutorial, HttpStatus.CREATED);
    }

    @PutMapping("/tutorials/{id}")
    public ResponseEntity<Tutorial3> updateTutorial(@PathVariable("id") long id, @RequestBody Tutorial3 tutorial) {
        Tutorial3 _tutorial = tutorial3Repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial with id = " + id));

        _tutorial.setTitle(tutorial.getTitle());
        _tutorial.setDescription(tutorial.getDescription());
        _tutorial.setPublished(tutorial.isPublished());

        return new ResponseEntity<>(tutorial3Repository.save(_tutorial), HttpStatus.OK);
    }

    @DeleteMapping("/tutorials/{id}")
    public ResponseEntity<HttpStatus> deleteTutorial(@PathVariable("id") long id) {
        tutorial3Repository.deleteById(id);

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @DeleteMapping("/tutorials")
    public ResponseEntity<HttpStatus> deleteAllTutorials() {
        tutorial3Repository.deleteAll();

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @GetMapping("/tutorials/published")
    public ResponseEntity<List<Tutorial3>> findByPublished() {
        List<Tutorial3> tutorials = tutorial3Repository.findByPublished(true);

        if (tutorials.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }

        return new ResponseEntity<>(tutorials, HttpStatus.OK);
    }

}
