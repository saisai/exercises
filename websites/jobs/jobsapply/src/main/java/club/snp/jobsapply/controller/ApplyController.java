package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.service.ApplyService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@CrossOrigin(origins = "http://localhost:5173", maxAge = 3600)
@RestController
public class ApplyController {

    ApplyService applyService;
    ApplyController(ApplyService applyService) {
        this.applyService = applyService;
    }

    @GetMapping(value="/apply")
    public List getApply() {
        return applyService.getAll();
    }

    @DeleteMapping("/apply/{id}")
    public ResponseEntity<HttpStatus> deleteApply(@PathVariable("id") long id) {
        try {
            applyService.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/apply")
    public ResponseEntity<Object> createApply(@RequestBody Apply apply) {
        System.out.println(apply.getLink());
        Optional<Apply> searchData = applyService.findByTitleAndLink(apply.getTitle(), apply.getLink());
        System.out.println("apply.getLink() " + apply.getLink());
        System.out.println("apply.getTitle() " + apply.getTitle());
        if(searchData.isPresent()) {
            Map<String, Object> map = new HashMap<>();
            map.put("message", "Already exites");
            return new ResponseEntity<>(map, HttpStatus.OK);
        }

        try {
            Apply _apply = applyService
                    .save(new Apply(apply.getTitle(), apply.getLink(), apply.getTime()));
            return new ResponseEntity<>(_apply, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/apply/{id}")
    public ResponseEntity<Apply> updateTutorial(@PathVariable("id") long id, @RequestBody Apply tutorial) {
        Optional<Apply> applyData = applyService.findById(id);

        if (applyData.isPresent()) {
            Apply _apply = applyData.get();
            _apply.setEmail(tutorial.getEmail());
            _apply.setUpdatedAt(new Date());
            _apply.setDescription(tutorial.getDescription());
//            _tutorial.setDescription(tutorial.getDescription());
//            _tutorial.setPublished(tutorial.isPublished());
            return new ResponseEntity<>(applyService.save(_apply), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
