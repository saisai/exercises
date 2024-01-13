package club.snp.jobsapply.repository;

import club.snp.jobsapply.entity.JobThai;
import io.lettuce.core.dynamic.annotation.Param;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import java.util.List;
@Repository
public interface JobThaiRepository extends JpaRepository<JobThai, Long> {


    @Query("SELECT j FROM JobThai j WHERE j.title LIKE %?1%")
    public List<JobThai> search(String keyword);

    // correct in native query
//    @Query(value="Select * from th_jobthai c where c.title like %:keyword%", nativeQuery=true)
//    public List<JobThai> search(@Param("keyword") String keyword);
}
