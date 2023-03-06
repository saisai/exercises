package com.springtutorials.tutorials.onetomany.repository;

import com.springtutorials.tutorials.onetomany.model.Tutorial2;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface Tutorial2Repository extends JpaRepository<Tutorial2, Long> {
    List<Tutorial2> findByPublished(boolean published);

    List<Tutorial2> findByTitleContaining(String title);

}
