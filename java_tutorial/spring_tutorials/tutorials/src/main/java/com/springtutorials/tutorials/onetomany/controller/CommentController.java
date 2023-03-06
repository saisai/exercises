package com.springtutorials.tutorials.onetomany.controller;

import com.springtutorials.tutorials.onetomany.model.Comment;
import com.springtutorials.tutorials.onetomany.repository.CommentRepository;
import com.springtutorials.tutorials.onetomany.repository.Tutorial2Repository;
import com.springtutorials.tutorials.onetoone.exception.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "http://localhost:8080")
@RestController
@RequestMapping("/api/tutorials2/")
public class CommentController {

    @Autowired
    private Tutorial2Repository tutorial2Repository;

    @Autowired
    private CommentRepository commentRepository;

    @GetMapping("/tutorials/{tutorials2Id}/comments")
    public ResponseEntity<List<Comment>> getAllCommentsByTutorialId(@PathVariable(value = "tutorials2Id") Long tutorials2Id) {
        if (!tutorial2Repository.existsById(tutorials2Id)) {
            throw new ResourceNotFoundException("Not found Tutorial with id = " + tutorials2Id);
        }

        List<Comment> comments = commentRepository.findByTutorials2_Id(tutorials2Id);
        return new ResponseEntity<>(comments, HttpStatus.OK);
    }

    @GetMapping("/comments/{id}")
    public ResponseEntity<Comment> getCommentsByTutorialId(@PathVariable(value = "id") Long id) {
        Comment comment = commentRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Not found Comment with id = " + id));

        return new ResponseEntity<>(comment, HttpStatus.OK);
    }

    @PostMapping("/tutorials/{tutorials2Id}/comments")
    public ResponseEntity<Comment> createComment(@PathVariable(value = "tutorials2Id") Long tutorials2Id,
                                                 @RequestBody Comment commentRequest) {
        Comment comment = tutorial2Repository.findById(tutorials2Id).map(tutorial -> {
            commentRequest.setTutorial(tutorial);
            return commentRepository.save(commentRequest);
        }).orElseThrow(() -> new ResourceNotFoundException("Not found Tutorial2 with id = " + tutorials2Id));

        return new ResponseEntity<>(comment, HttpStatus.CREATED);
    }

    @PutMapping("/comments/{id}")
    public ResponseEntity<Comment> updateComment(@PathVariable("id") long id, @RequestBody Comment commentRequest) {
        Comment comment = commentRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("CommentId " + id + "not found"));

        comment.setContent(commentRequest.getContent());

        return new ResponseEntity<>(commentRepository.save(comment), HttpStatus.OK);
    }

    @DeleteMapping("/comments/{id}")
    public ResponseEntity<HttpStatus> deleteComment(@PathVariable("id") long id) {
        commentRepository.deleteById(id);

        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @DeleteMapping("/tutorials/{tutorials2Id}/comments")
    public ResponseEntity<List<Comment>> deleteAllCommentsOfTutorial(@PathVariable(value = "tutorialId") Long tutorialId) {
        if (!tutorial2Repository.existsById(tutorialId)) {
            throw new ResourceNotFoundException("Not found Tutorial with id = " + tutorialId);
        }

        commentRepository.deleteByTutorials2_Id(tutorialId);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

}
