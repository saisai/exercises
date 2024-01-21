package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.Apply;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ApplyRepository extends JpaRepository<Apply, Long> {

    Optional<Apply> findByTitleAndLink(String title, String link);
}
