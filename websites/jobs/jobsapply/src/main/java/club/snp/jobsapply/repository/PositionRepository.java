package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.entity.Position;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface PositionRepository extends JpaRepository<Position, Long> {

    Optional<Position> findByTitle(String title);
}
