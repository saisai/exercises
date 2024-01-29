package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.File;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface FileRepository extends JpaRepository<File, Long> {
    Optional<File> findByTitle(String title);
}
