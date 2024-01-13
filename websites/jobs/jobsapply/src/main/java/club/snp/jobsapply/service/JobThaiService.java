package club.snp.jobsapply.service;

import club.snp.jobsapply.entity.JobThai;
import club.snp.jobsapply.repository.JobThaiRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobThaiService {
    @Autowired
    JobThaiRepository jobThaiRepository;

    public List<JobThai> listAll(String keyword) {
        if (keyword != null) {
            System.out.println("keyword " + keyword);
            return jobThaiRepository.search(keyword);
        }
        return jobThaiRepository.findAll();
    }

    public List<JobThai> getAll() {
        return jobThaiRepository.findAll();
    }
}
