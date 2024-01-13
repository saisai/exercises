package club.snp.jobsapply.service;

import club.snp.jobsapply.entity.JobThai;
import club.snp.jobsapply.entity.ThJobsDb;
import club.snp.jobsapply.repository.JobThaiRepository;
import club.snp.jobsapply.repository.JobsDbRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class JobsDBService {

    JobsDbRepository jobsDbRepository;

    JobsDBService(JobsDbRepository jobsDbRepository) {
        this.jobsDbRepository = jobsDbRepository;
    }

    public List<ThJobsDb> listAll(String keyword) {
        if (keyword != null) {
            System.out.println("keyword " + keyword);
            return jobsDbRepository.search(keyword);
        }
        return jobsDbRepository.findAll();
    }

    public List<ThJobsDb> getAll() {
        return jobsDbRepository.findAll();
    }

}
