package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.Position;
import club.snp.jobsapply.service.PositionService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@CrossOrigin(origins = "http://localhost:5173", maxAge = 3600)
@RestController
public class PositionController {

    PositionService positionService;

    PositionController(PositionService positionService) {
        this.positionService = positionService;
    }

    @GetMapping(value="/position")
    public List getApply() {
        return positionService.getAll();
    }
    @PostMapping("/position")
    public ResponseEntity<Object> createApply(@RequestBody Position position) {
        System.out.println(position.getTitle());
        Optional<Position> searchData = positionService.findByTitle(position.getTitle());
        System.out.println("apply.getTitle() " + position.getTitle());
        if(searchData.isPresent()) {
            Map<String, Object> map = new HashMap<>();
            map.put("message", "Already exites");
            return new ResponseEntity<>(map, HttpStatus.OK);
        }

        try {
            Position _position = positionService
                    .save(new Position(position.getTitle(), position.getDescription()));
            return new ResponseEntity<>(_position, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


    @PutMapping("/position/{id}")
    public ResponseEntity<Position> updatePosition(@PathVariable("id") long id, @RequestBody Position position) {
        Optional<Position> applyData = positionService.findById(id);
        if (applyData.isPresent()) {
            Position _position = applyData.get();
            _position.setTitle(position.getTitle());
            _position.setDescription(position.getDescription());
            return new ResponseEntity<>(positionService.save(_position), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping("/position/{id}")
    public ResponseEntity<HttpStatus> deletePosition(@PathVariable("id") long id) {
        try {
            positionService.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
