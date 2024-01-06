package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.JobThai;
import club.snp.jobsapply.repository.JobThaiRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
@RestController
public class JobThaiController {

    @Autowired
    JobThaiRepository jobThaiRepository;

    @GetMapping(value="/jobthai")
    @CrossOrigin(origins = "http://localhost:3000")
    public List getJobThai() {
        List<JobThai> lstJobThai = jobThaiRepository.findAll();
        return lstJobThai;
    }
}
