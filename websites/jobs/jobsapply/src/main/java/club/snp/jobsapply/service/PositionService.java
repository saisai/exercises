package club.snp.jobsapply.service;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.entity.Position;
import club.snp.jobsapply.repository.PositionRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class PositionService {
    PositionRepository positionRepository;

    PositionService(PositionRepository positionRepository) {
        this.positionRepository = positionRepository;
    }

    public Position save(Position position) {
        positionRepository.save(position);
        return position;
    }

    public Optional<Position> findByTitle(String title) {
        Optional<Position> positionData = positionRepository.findByTitle(title);
        return positionData;
    }
}
