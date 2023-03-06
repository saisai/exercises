package com.springtutorials.tutorials.manytomany.repository;

import com.springtutorials.tutorials.manytomany.model.Tutorial3;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface Tutorial3Repository extends JpaRepository<Tutorial3, Long> {

    List<Tutorial3> findByPublished(boolean published);

    List<Tutorial3> findByTitleContaining(String title);

    List<Tutorial3> findTutorialsByTagsId(Long tagId);

}
