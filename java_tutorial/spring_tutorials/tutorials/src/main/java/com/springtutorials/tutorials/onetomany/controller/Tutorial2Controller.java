package com.springtutorials.tutorials.onetomany.controller;

import com.springtutorials.tutorials.onetomany.model.Tutorial2;
import com.springtutorials.tutorials.onetomany.repository.Tutorial2Repository;
import com.springtutorials.tutorials.onetoone.exception.ResourceNotFoundException;
import com.springtutorials.tutorials.onetoone.model.Tutorial;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@CrossOrigin(origins = "http://localhost:8080")
@RestController
@RequestMapping("/api/tutorials2/")
public class Tutorial2Controller {

    @Autowired
    Tutorial2Repository tutorial2Repository;

    @GetMapping("/tutorials")
    public ResponseEntity<List<Tutorial2>> getAllTutorials(@RequestParam(required = false) String title) {
        List<Tutorial2> tutorials = new ArrayList<Tutorial2>();

        if(title == null){
            tutorial2Repository.findAll().forEach(tutorials::add);
        } else {
            tutorial2Repository.findByTitleContaining(title).forEach(tutorials::add);
        }

        if(tutorials.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }

        return new ResponseEntity<>(tutorials, HttpStatus.OK);
    }

    @GetMapping("/tutorials/{id}")
    public ResponseEntity<Tutorial2> getTutorialById(@PathVariable("id") long id) {
        Tutorial2 tutorial = tutorial2Repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial2 with id = " + id));

        return new ResponseEntity<>(tutorial, HttpStatus.OK);
    }

    @PostMapping("/tutorials")
    public ResponseEntity<Tutorial2> createTutorial(@RequestBody  Tutorial2 tutorial) {
        Tutorial2 _tutorial = tutorial2Repository.save(new Tutorial2(tutorial.getTitle(), tutorial.getDescription(), true));
        return new ResponseEntity<>(_tutorial, HttpStatus.CREATED);
    }

    @PutMapping("/tutorials/{id}")
    public ResponseEntity<Tutorial2> updateTutorial(@PathVariable("id") long id, @RequestBody  Tutorial2 tutorial) {

        Tutorial2 _tutorial = tutorial2Repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial2 with id = " + id));

        _tutorial.setTitle(tutorial.getTitle());
        _tutorial.setDescription(tutorial.getDescription());
        _tutorial.setPublished(tutorial.isPublished());

        return new ResponseEntity<>(tutorial2Repository.save(_tutorial), HttpStatus.OK);
    }

    @DeleteMapping("/tutorials/{id}")
    public ResponseEntity<HttpStatus> deleteTutorial(@PathVariable("id") long id) {
        tutorial2Repository.deleteById(id);

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @DeleteMapping("/tutorials")
    public ResponseEntity<HttpStatus> deleteAllTutorials() {
        tutorial2Repository.deleteAll();

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @GetMapping("/tutorials/published")
    public ResponseEntity<List<Tutorial2>> findByPublished() {
        List<Tutorial2> tutorials = tutorial2Repository.findByPublished(true);

        if(tutorials.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }

        return new ResponseEntity<>(tutorials, HttpStatus.OK);
    }


}
