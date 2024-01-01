package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.ThJobsDb;
import org.springframework.data.jpa.repository.JpaRepository;

public interface  JobsDbRepository extends JpaRepository<ThJobsDb, Integer> {
}
