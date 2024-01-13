package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.ThJobsDb;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface  JobsDbRepository extends JpaRepository<ThJobsDb, Integer> {
    @Query("SELECT j FROM ThJobsDb j WHERE j.title LIKE %?1%")
    List<ThJobsDb> search(String keyword);
}
