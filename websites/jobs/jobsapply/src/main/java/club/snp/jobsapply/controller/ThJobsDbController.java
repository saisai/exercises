package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.ThJobsDb;
import club.snp.jobsapply.service.JobsDBService;
import io.lettuce.core.dynamic.annotation.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ThJobsDbController {

    @Autowired
    JobsDBService jobsDBService;
    @GetMapping(value="/hello")
    public String hello() {
        return "hello";
    }

    @GetMapping(value="/jobsdb")
    @CrossOrigin(origins = "http://localhost:3000")
    public List getJobsDb() {
        List<ThJobsDb> lstThJobsDb = jobsDBService.getAll();
        return lstThJobsDb;
    }

    @GetMapping(value="/jobsdbsearch/")
    @CrossOrigin(origins = "http://localhost:3000")
    public List searchJobsDB(@Param("keyword") String keyword){
        return jobsDBService.listAll(keyword);
    }


}
