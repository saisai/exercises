package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.entity.Position;
import club.snp.jobsapply.service.PositionService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:5173", maxAge = 3600)
@RestController
public class PositionController {

    PositionService positionService;

    PositionController(PositionService positionService) {
        this.positionService = positionService;
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
}
