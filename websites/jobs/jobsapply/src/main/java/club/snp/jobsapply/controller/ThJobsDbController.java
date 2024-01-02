package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.ThJobsDb;
import club.snp.jobsapply.repository.JobsDbRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ThJobsDbController {
    @Autowired
    JobsDbRepository jobsDbRepository;
    @GetMapping(value="/hello")
    public String hello() {
        return "hello";
    }

    @GetMapping(value="/jobsdb")
    @CrossOrigin(origins = "http://localhost:3000")
    public List getJobsDb() {
        List<ThJobsDb> lstThJobsDb = jobsDbRepository.findAll();
        return lstThJobsDb;
    }


}
