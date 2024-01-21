package club.snp.jobsapply.service;

import club.snp.jobsapply.entity.Apply;
import club.snp.jobsapply.repository.ApplyRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

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

    public Optional<Apply> findById(long id) {
        Optional<Apply> applyData = applyRepository.findById(id);
        return applyData;
    }

    public Optional<Apply> findByTitleAndLink(String title, String link) {
        Optional<Apply> applyData = applyRepository.findByTitleAndLink(title, link);
        return applyData;
    }


}
