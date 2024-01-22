package club.snp.jobsapply.controller;

import club.snp.jobsapply.entity.JobThai;
import club.snp.jobsapply.repository.JobThaiRepository;
import club.snp.jobsapply.service.JobThaiService;
import io.lettuce.core.dynamic.annotation.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
@CrossOrigin(origins = "*", maxAge = 3600)
@RestController
public class JobThaiController {

    @Autowired
    JobThaiService jobThaiService;

    @GetMapping(value="/jobthai")
    public List getJobThai() {
        return jobThaiService.getAll();
    }

    @GetMapping(value="/jobthaisearach/")
    public List searchJobThai(@Param("keyword") String keyword){
        return jobThaiService.listAll(keyword);
    }
}
