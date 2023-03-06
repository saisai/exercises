package com.springtutorials.tutorials.onetoone.repository;

import com.springtutorials.tutorials.onetoone.model.TutorialDetails;
import org.springframework.data.jpa.repository.JpaRepository;

import javax.transaction.Transactional;

public interface TutorialDetailsRepository extends JpaRepository<TutorialDetails, Long> {

    @Transactional
    void deleteById(long id);

    @Transactional
    void deleteByTutorialId(long tutorialId);
}
