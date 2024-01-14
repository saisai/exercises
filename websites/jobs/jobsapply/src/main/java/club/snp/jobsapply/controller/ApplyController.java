package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.repository.ApplyRepository;
import club.snp.jobsapply.service.ApplyService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class ApplyController {

    ApplyService applyService;
    ApplyController(ApplyService applyService) {
        this.applyService = applyService;
    }

    @GetMapping(value="/apply")
    @CrossOrigin(origins = "http://localhost:3000")
    public List getApply() {
        return applyService.getAll();
    }

    @DeleteMapping("/apply/{id}")
    @CrossOrigin(origins = "http://localhost:3000")
    public ResponseEntity<HttpStatus> deleteApply(@PathVariable("id") long id) {
        try {
            applyService.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/apply")
    @CrossOrigin(origins = "http://localhost:3000")
    public ResponseEntity<Apply> createApply(@RequestBody Apply apply) {
        System.out.println(apply.getLink());
        try {
            Apply _apply = applyService
                    .save(new Apply(apply.getTitle(), apply.getLink(), apply.getTime()));
            return new ResponseEntity<>(_apply, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
