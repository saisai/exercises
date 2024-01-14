package club.snp.jobsapply.service;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.repository.ApplyRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ApplyService {
    ApplyRepository applyRepository;
    ApplyService(ApplyRepository applyRepository) {
        this.applyRepository = applyRepository;
    }

    public List<Apply> getAll() {
        return applyRepository.findAll();
    }

    public Apply save(Apply apply) {
        applyRepository.save(apply);
        return apply;
    }
    public void deleteById(long id) {
        applyRepository.deleteById(id);
    }


}
